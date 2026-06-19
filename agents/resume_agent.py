"""
Resume Analysis Agent
---------------------
Parses raw resume text into structured JSON using Groq LLaMA3.
"""

import os
import json
import re
from groq import Groq
from dotenv import load_dotenv
from utils.parser import extract_email, extract_name_heuristic

load_dotenv()

# ─── Groq Client ──────────────────────────────────────────────────────────────
def get_groq_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file!")
    return Groq(api_key=api_key)

# ─── Skill Keyword Bank ───────────────────────────────────────────────────────
SKILL_KEYWORDS = [
    "python","java","javascript","typescript","c++","c#","go","rust","r","scala","kotlin","swift",
    "machine learning","deep learning","nlp","computer vision","transformers","pytorch","tensorflow",
    "keras","scikit-learn","xgboost","lightgbm","hugging face","langchain","openai",
    "sql","mysql","postgresql","mongodb","sqlite","pandas","numpy","spark","hadoop",
    "power bi","tableau","excel","data analysis","data science","etl",
    "react","angular","vue","node.js","django","flask","fastapi","spring boot",
    "html","css","rest api","graphql",
    "aws","gcp","azure","docker","kubernetes","ci/cd","git","github","jenkins",
    "terraform","linux","agile","scrum","microservices","system design","object oriented"
]

def extract_skills_from_text(text: str) -> list[str]:
    text_lower = text.lower()
    found = []
    for skill in SKILL_KEYWORDS:
        if skill in text_lower:
            found.append(skill.title() if len(skill.split()) > 1 else skill.upper())
    return list(set(found))

# ─── Domain Detection ─────────────────────────────────────────────────────────
DOMAIN_RULES = {
    "Data Scientist": ["machine learning","deep learning","pytorch","tensorflow","statistics","r","data science"],
    "Data Analyst": ["power bi","tableau","sql","excel","data analysis","etl","reporting"],
    "ML Engineer": ["mlops","model deployment","pytorch","tensorflow","kubeflow","feature store"],
    "AI/NLP Engineer": ["nlp","transformers","hugging face","bert","gpt","langchain","llm"],
    "Backend Developer": ["django","flask","fastapi","node.js","spring boot","postgresql","rest api"],
    "Frontend Developer": ["react","angular","vue","html","css","javascript","typescript"],
    "Full Stack Developer": ["react","node.js","django","postgresql","javascript","rest api"],
    "DevOps Engineer": ["docker","kubernetes","ci/cd","terraform","aws","jenkins","linux"],
    "Cloud Engineer": ["aws","gcp","azure","terraform","cloud architecture","serverless"],
    "Data Engineer": ["spark","hadoop","kafka","airflow","etl","data pipeline","sql"],
}

def detect_domain(skills: list[str]) -> dict:
    skills_lower = [s.lower() for s in skills]
    scores = {}
    for domain, keywords in DOMAIN_RULES.items():
        match_count = sum(1 for kw in keywords if any(kw in s for s in skills_lower))
        scores[domain] = match_count
    sorted_domains = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_domain, top_score = sorted_domains[0]
    total_keywords = len(DOMAIN_RULES.get(top_domain, [1]))
    confidence = min(int((top_score / total_keywords) * 100), 98)
    return {
        "primary": top_domain,
        "alternatives": [d for d, s in sorted_domains[1:3] if s > 0],
        "confidence": confidence
    }

# ─── Main Analysis ────────────────────────────────────────────────────────────
def analyze_resume(raw_text: str) -> dict:
    client = get_groq_client()
    prompt = f"""
You are an expert resume parser. Extract structured information from this resume text.

Return ONLY a valid JSON object with these exact keys:
{{
  "name": "Full name of the candidate",
  "email": "email address",
  "phone": "phone number or empty string",
  "skills": ["list", "of", "technical", "skills"],
  "experience": ["Brief description of each job/role"],
  "education": ["Degree, Institution, Year"],
  "projects": ["Project name and brief description"],
  "summary": "2-3 sentence professional summary"
}}

RESUME TEXT:
{raw_text[:4000]}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # ✅ updated model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=1500
        )
        response_text = response.choices[0].message.content.strip()
        response_text = re.sub(r"```json|```", "", response_text).strip()
        profile = json.loads(response_text)
    except Exception as e:
        print(f"[Resume Agent] Groq parsing failed: {e}. Using fallback.")
        profile = {
            "name": extract_name_heuristic(raw_text),
            "email": extract_email(raw_text),
            "phone": "",
            "skills": [],
            "experience": [],
            "education": [],
            "projects": [],
            "summary": ""
        }

    if not profile.get("email"):
        profile["email"] = extract_email(raw_text)
    if not profile.get("name") or profile["name"] == "Unknown":
        profile["name"] = extract_name_heuristic(raw_text)

    groq_skills = profile.get("skills", [])
    keyword_skills = extract_skills_from_text(raw_text)
    all_skills = list({s.lower(): s for s in groq_skills + keyword_skills}.values())
    profile["skills"] = all_skills[:40]

    domain_info = detect_domain(profile["skills"])
    profile["domain"] = domain_info["primary"]
    profile["domain_alternatives"] = domain_info["alternatives"]
    profile["domain_confidence"] = domain_info["confidence"]
    profile["raw_text"] = raw_text

    return profile

"""
Resume Analysis Agent
---------------------
Parses raw resume text into structured JSON using Groq LLaMA3.

FIXED VERSION — changes from original:
  1. max_tokens raised 1500 -> 3000 (long resumes were getting truncated
     mid-JSON, which threw a JSONDecodeError and silently triggered the
     empty fallback profile -- this is the most likely cause of
     "only name + skills" showing up downstream).
  2. raw_text truncation raised 4000 -> 8000 chars so more of the resume
     (especially experience/projects, which usually come after the
     summary) actually reaches the model.
  3. On any failure, the raw Groq response is now printed BEFORE the
     fallback fires, so you can see exactly what went wrong instead of
     just "Groq parsing failed".
  4. After a "successful" parse, we sanity-check that experience/projects
     aren't suspiciously empty and warn loudly if so -- this catches the
     case where Groq returns valid JSON but with thin/empty sections.
  5. response_format={"type": "json_object"} added -- this tells Groq to
     guarantee valid JSON output, which eliminates most JSONDecodeError
     failures outright (this is the single biggest fix).
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

    # FIX: 4000 -> 8000 chars. Experience/projects sections usually come
    # after the summary/skills, so a short truncation was cutting them
    # off before the model ever saw them.
    resume_excerpt = raw_text[:8000]

    prompt = f"""
You are an expert resume parser. Extract structured information from this resume text.

Return ONLY a valid JSON object with these exact keys:
{{
  "name": "Full name of the candidate",
  "email": "email address",
  "phone": "phone number or empty string",
  "skills": ["list", "of", "technical", "skills"],
  "experience": ["Detailed description of each job/role, including company, title, duration, and 2-3 key responsibilities/achievements per role"],
  "education": ["Degree, Institution, Year"],
  "projects": ["Project name and detailed description including technologies used"],
  "summary": "2-3 sentence professional summary"
}}

IMPORTANT:
- Extract EVERY job/role found in the resume, not just the most recent one.
- Extract EVERY project found in the resume.
- Do not omit or summarize away the experience/projects sections — list each one as a separate array entry.
- If a section genuinely does not exist in the resume, return an empty array for it, but do not guess it's empty just because it's far down the page.

RESUME TEXT:
{resume_excerpt}
"""
    profile = None
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=3000,  # FIX: was 1500 — too low for full resumes, caused mid-JSON truncation
            response_format={"type": "json_object"},  # FIX: forces valid JSON, eliminates most parse failures
        )
        response_text = response.choices[0].message.content.strip()
        response_text = re.sub(r"```json|```", "", response_text).strip()
        profile = json.loads(response_text)

    except json.JSONDecodeError as e:
        # FIX: log the actual raw text that failed to parse, so the real
        # problem (truncation, malformed JSON, etc.) is visible instead
        # of silently vanishing into the fallback.
        print(f"[Resume Agent] JSON parsing failed: {e}")
        print(f"[Resume Agent] Raw response that failed to parse:\n{response_text[:2000]}")
        profile = None

    except Exception as e:
        print(f"[Resume Agent] Groq API call failed: {e}")
        profile = None

    if profile is None:
        print("[Resume Agent] Using fallback profile (name/email/skills only via regex+keywords).")
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

    # FIX: sanity check — warn loudly if experience/projects came back
    # empty even though parsing "succeeded". This is the symptom you're
    # seeing (name + skills only) and now it will at least be visible
    # in your terminal/logs instead of failing silently.
    if not profile.get("experience") and not profile.get("projects"):
        print("[Resume Agent] WARNING: experience and projects are both empty after parsing. "
              "Check that your resume text actually contains these sections, and check the "
              "raw Groq response above if this is unexpected.")

    return profile
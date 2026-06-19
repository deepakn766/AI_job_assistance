"""
agents/resume_optimizer_agent.py
---------------------------------
AGENT 4: ATS Resume Optimization Agent

Responsibilities:
  1. Take the candidate's original resume + selected job description
  2. Use Groq to rewrite/optimize sections for ATS alignment
  3. Improve keywords, bullet points, summary
  4. NEVER fabricate experience or skills
  5. Output as text and save as DOCX

ATS = Applicant Tracking System
  Many companies use ATS software to scan resumes before a human reads them.
  Key factors: keyword matching, clean formatting, clear section headers.
"""

import os
import json
import re
from groq import Groq
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from dotenv import load_dotenv

load_dotenv()

GENERATED_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "generated")
os.makedirs(GENERATED_DIR, exist_ok=True)


def get_groq_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set in .env")
    return Groq(api_key=api_key)


# ─── Core Optimization Function ───────────────────────────────────────────────

def optimize_resume(profile: dict, job: dict) -> dict:
    """
    Main entry point for the Resume Optimizer Agent.

    Flow:
    1. Build a targeted prompt with profile + JD
    2. Ask Groq to optimize each resume section
    3. Return structured optimized resume dict
    4. Also save as DOCX file

    Args:
        profile: Candidate profile dict from Resume Agent
        job:     Selected job dict (title, company, description)

    Returns:
        optimized dict with sections + DOCX file path
    """
    client = get_groq_client()

    # Prepare compact versions to fit in context window
    skills_str = ", ".join(profile.get("skills", [])[:30])
    experience_str = "\n".join([f"- {exp}" for exp in profile.get("experience", [])[:5]])
    projects_str = "\n".join([f"- {proj}" for proj in profile.get("projects", [])[:4]])
    education_str = "\n".join([f"- {edu}" for edu in profile.get("education", [])[:3]])

    prompt = f"""
You are an expert ATS resume writer and career coach.

Your task: Optimize this candidate's resume for the specific job below.

STRICT RULES (NEVER BREAK THESE):
1. Do NOT invent, fabricate, or add fake experience, skills, or projects.
2. Only IMPROVE wording, professionalism, and keyword alignment.
3. Use strong action verbs (Developed, Built, Optimized, Implemented, etc.)
4. Mirror keywords from the job description naturally.
5. Keep bullet points concise: max 2 lines each.

CANDIDATE PROFILE:
Name: {profile.get('name', '')}
Current Skills: {skills_str}

Experience:
{experience_str}

Projects:
{projects_str}

Education:
{education_str}

TARGET JOB:
Title: {job.get('title', '')}
Company: {job.get('company', '')}
Job Description:
{job.get('description', '')[:1500]}

OUTPUT: Return ONLY a valid JSON object with these keys:
{{
  "summary": "3-4 sentence ATS-optimized professional summary tailored to this role",
  "skills_section": ["skill1", "skill2", ...],
  "experience_bullets": ["• Improved bullet 1", "• Improved bullet 2", ...],
  "projects_bullets": ["• Project bullet 1", "• Project bullet 2", ...],
  "keywords_added": ["keyword1", "keyword2", ...]
}}

No markdown, no extra text. Valid JSON only.
"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1800
        )
        text = response.choices[0].message.content.strip()
        text = re.sub(r"```json|```", "", text).strip()
        optimized = json.loads(text)

    except (json.JSONDecodeError, Exception) as e:
        print(f"[Optimizer Agent] Groq failed: {e}. Using basic optimization.")
        # Fallback: Return lightly formatted original data
        optimized = {
            "summary": profile.get("summary", "Experienced professional seeking new opportunities."),
            "skills_section": profile.get("skills", [])[:20],
            "experience_bullets": [f"• {exp}" for exp in profile.get("experience", [])],
            "projects_bullets": [f"• {proj}" for proj in profile.get("projects", [])],
            "keywords_added": []
        }

    # Add metadata
    optimized["candidate_name"] = profile.get("name", "Candidate")
    optimized["candidate_email"] = profile.get("email", "")
    optimized["target_job"] = f"{job.get('title', '')} at {job.get('company', '')}"
    optimized["education"] = profile.get("education", [])

    # Save DOCX
    docx_path = save_as_docx(optimized, profile, job)
    optimized["docx_path"] = docx_path

    return optimized


# ─── DOCX Export ──────────────────────────────────────────────────────────────

def save_as_docx(optimized: dict, profile: dict, job: dict) -> str:
    """
    Create a clean, ATS-friendly DOCX resume from the optimized data.

    ATS-friendly design principles:
    - No tables, no text boxes (ATS can't read them)
    - Standard fonts (Calibri)
    - Clear section headers
    - Simple formatting
    """
    doc = Document()

    # Set document margins
    from docx.shared import Inches
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    def add_heading(text, level=1):
        para = doc.add_paragraph()
        run = para.add_run(text)
        run.bold = True
        run.font.size = Pt(14 if level == 1 else 11)
        if level == 2:
            # Section header with underline effect via border
            run.font.color.rgb = RGBColor(0x1a, 0x56, 0xdb)  # Professional blue
        para.space_after = Pt(4)
        return para

    def add_body(text, bold=False):
        para = doc.add_paragraph()
        run = para.add_run(text)
        run.font.size = Pt(10)
        run.bold = bold
        para.space_after = Pt(2)
        return para

    # --- Header: Name + Contact ---
    name_para = doc.add_paragraph()
    name_run = name_para.add_run(optimized.get("candidate_name", "Candidate"))
    name_run.bold = True
    name_run.font.size = Pt(18)
    name_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    contact_para = doc.add_paragraph()
    contact_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    email = optimized.get("candidate_email", "")
    phone = profile.get("phone", "")
    contact_text = " | ".join(filter(None, [email, phone]))
    contact_run = contact_para.add_run(contact_text)
    contact_run.font.size = Pt(10)

    doc.add_paragraph()  # Spacer

    # --- Professional Summary ---
    add_heading("PROFESSIONAL SUMMARY", level=2)
    add_body(optimized.get("summary", ""))
    doc.add_paragraph()

    # --- Skills ---
    add_heading("TECHNICAL SKILLS", level=2)
    skills = optimized.get("skills_section", [])
    if skills:
        add_body("  •  ".join(skills[:20]))
    doc.add_paragraph()

    # --- Experience ---
    if optimized.get("experience_bullets"):
        add_heading("EXPERIENCE", level=2)
        for bullet in optimized["experience_bullets"]:
            add_body(bullet)
        doc.add_paragraph()

    # --- Projects ---
    if optimized.get("projects_bullets"):
        add_heading("PROJECTS", level=2)
        for bullet in optimized["projects_bullets"]:
            add_body(bullet)
        doc.add_paragraph()

    # --- Education ---
    add_heading("EDUCATION", level=2)
    for edu in optimized.get("education", []):
        add_body(edu)

    # --- ATS Footer ---
    doc.add_paragraph()
    footer = doc.add_paragraph()
    footer_run = footer.add_run(
        f"Optimized for: {optimized.get('target_job', '')} | Generated by Job Assistant"
    )
    footer_run.font.size = Pt(8)
    footer_run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    # Save file
    safe_name = re.sub(r"[^\w]", "_", optimized.get("candidate_name", "resume"))
    file_path = os.path.join(GENERATED_DIR, f"optimized_resume_{safe_name}.docx")
    doc.save(file_path)
    print(f"[Optimizer Agent] DOCX saved: {file_path}")
    return file_path

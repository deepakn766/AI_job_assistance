"""
agents/matching_agent.py
------------------------
AGENT 3: Matching Agent

Responsibilities:
  1. Convert resume text → embedding vector
  2. Convert each job description → embedding vector
  3. Calculate cosine similarity (match %)
  4. Identify strong skills and missing skills
  5. Return ranked job list with scores

Why embeddings for matching?
  - Keyword matching misses synonyms ("ML" vs "machine learning")
  - Embeddings capture semantic meaning
  - Cosine similarity is fast even for 100+ jobs
"""

from utils.embeddings import batch_similarity, get_embedding
from utils.database import save_jobs
import numpy as np


# ─── Skill Gap Analysis ───────────────────────────────────────────────────────

def analyze_skill_gap(candidate_skills: list[str], job_description: str) -> dict:
    """
    Simple keyword-based skill gap analysis.

    Checks which of the candidate's skills appear in the job description,
    and scans the job description for skills the candidate might be missing.

    Returns:
        {
          "matching_skills": [...],
          "missing_skills":  [...],
          "ats_score":       int (0-100)
        }
    """
    jd_lower = job_description.lower()
    candidate_lower = [s.lower() for s in candidate_skills]

    # Skills the candidate has that appear in JD
    matching = [s for s in candidate_skills if s.lower() in jd_lower]

    # Common skills mentioned in JD that candidate doesn't have
    common_tech = [
        "aws", "docker", "kubernetes", "spark", "kafka", "airflow",
        "terraform", "react", "typescript", "graphql", "redis",
        "postgresql", "mongodb", "fastapi", "pytorch", "tensorflow",
        "mlflow", "dbt", "tableau", "power bi", "azure", "gcp"
    ]
    missing = [
        tech.upper() if len(tech) <= 3 else tech.title()
        for tech in common_tech
        if tech in jd_lower and tech not in candidate_lower
    ][:5]  # Max 5 missing skills shown

    # ATS score: based on how many candidate skills appear in JD
    if candidate_skills:
        ats_score = min(int((len(matching) / len(candidate_skills)) * 100) + 20, 95)
    else:
        ats_score = 30

    return {
        "matching_skills": matching[:8],   # Show top 8
        "missing_skills": missing,
        "ats_score": ats_score
    }


# ─── Main Matching Function ───────────────────────────────────────────────────

def match_jobs(resume_text: str, jobs: list[dict], candidate_skills: list[str]) -> list[dict]:
    """
    Main entry point for the Matching Agent.

    Flow:
    1. Prepare resume text (combine resume + skills for better embedding)
    2. Batch compute similarity scores for all jobs at once
    3. Enrich each job with match score and skill gap analysis
    4. Sort by match score (highest first)
    5. Update DB with scores
    6. Return enriched job list

    Args:
        resume_text:      Raw text of the resume
        jobs:             List of job dicts from Jobs Agent
        candidate_skills: Extracted skills list

    Returns:
        Jobs sorted by match_score (descending), each enriched with analysis
    """
    if not jobs:
        return []

    # --- Enrich resume text with skills for better matching ---
    # Adding skills explicitly helps the embedding focus on technical relevance
    skills_text = " ".join(candidate_skills)
    enriched_resume = f"{resume_text}\n\nKey Skills: {skills_text}"

    # --- Extract job descriptions for batch embedding ---
    job_descriptions = []
    for job in jobs:
        # Combine title + description for richer job embedding
        combined = f"{job['title']} at {job['company']}\n{job['description']}"
        job_descriptions.append(combined)

    # --- Batch similarity computation (efficient — one model call) ---
    print(f"[Matching Agent] Computing similarity for {len(jobs)} jobs...")
    scores = batch_similarity(enriched_resume, job_descriptions)

    # --- Enrich jobs with scores and analysis ---
    enriched_jobs = []
    for job, score in zip(jobs, scores):
        # Convert 0-1 cosine score to 0-100 percentage
        # Cosine scores for semantic matches typically range 0.3–0.7
        # We scale to make it more intuitive
        match_pct = round(min(score * 130, 99), 1)  # Scale up slightly, cap at 99

        gap_analysis = analyze_skill_gap(candidate_skills, job["description"])

        enriched_job = {
            **job,
            "match_score":      match_pct,
            "matching_skills":  gap_analysis["matching_skills"],
            "missing_skills":   gap_analysis["missing_skills"],
            "ats_score":        gap_analysis["ats_score"]
        }
        enriched_jobs.append(enriched_job)

    # --- Sort by match score descending ---
    enriched_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    # --- Update DB with match scores ---
    save_jobs(enriched_jobs)

    print(f"[Matching Agent] Top match: {enriched_jobs[0]['title']} at {enriched_jobs[0]['match_score']}%")
    return enriched_jobs

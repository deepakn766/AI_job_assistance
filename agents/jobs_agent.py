"""
agents/jobs_agent.py
--------------------
AGENT 2: Job Search Agent

Responsibilities:
  1. Take the detected domain/role from the Resume Agent
  2. Build optimized search queries
  3. Fetch real jobs from RemoteOK, Arbeitnow, Adzuna
  4. Clean and normalize job data
  5. Save to SQLite

The agent is intentionally simple — it's a smart wrapper around
the API client utility with domain-specific query generation.
"""

from utils.api_client import fetch_all_jobs
from utils.database import save_jobs


# ─── Query Generation ─────────────────────────────────────────────────────────

# Map detected domains to job-board-friendly search terms
DOMAIN_TO_QUERIES = {
    "Data Scientist":      ["data scientist", "machine learning engineer", "ML scientist"],
    "Data Analyst":        ["data analyst", "business analyst", "BI analyst"],
    "ML Engineer":         ["machine learning engineer", "MLOps engineer", "AI engineer"],
    "AI/NLP Engineer":     ["NLP engineer", "AI engineer", "LLM engineer"],
    "Backend Developer":   ["backend developer", "python developer", "software engineer backend"],
    "Frontend Developer":  ["frontend developer", "react developer", "UI developer"],
    "Full Stack Developer":["full stack developer", "software engineer", "web developer"],
    "DevOps Engineer":     ["devops engineer", "site reliability engineer", "platform engineer"],
    "Cloud Engineer":      ["cloud engineer", "AWS engineer", "cloud architect"],
    "Data Engineer":       ["data engineer", "ETL developer", "big data engineer"],
}

DEFAULT_QUERIES = ["software engineer", "developer", "engineer"]


def get_search_queries(domain: str, custom_skills: list[str] = None) -> list[str]:
    """
    Generate 2-3 search queries for the given domain.
    Optionally adds a skills-based query if custom skills are provided.
    """
    base_queries = DOMAIN_TO_QUERIES.get(domain, DEFAULT_QUERIES)
    queries = base_queries[:2]  # Use top 2 domain queries

    # Add a skills-based query for better coverage
    if custom_skills:
        # Pick the 2 most specific skills
        top_skills = custom_skills[:2]
        skill_query = " ".join(top_skills)
        queries.append(skill_query)

    return queries


# ─── Main Search Function ─────────────────────────────────────────────────────

def search_jobs(domain: str, skills: list[str] = None, max_per_query: int = 15) -> list[dict]:
    """
    Main entry point for the Job Search Agent.

    Flow:
    1. Generate search queries based on domain
    2. Fetch from all job APIs for each query
    3. Deduplicate across queries
    4. Save to database
    5. Return cleaned job list

    Args:
        domain: Detected role from Resume Agent (e.g., "Data Scientist")
        skills: Candidate's skills list (used to refine queries)
        max_per_query: Max jobs to fetch per search query

    Returns:
        List of normalized job dicts
    """
    queries = get_search_queries(domain, skills)
    all_jobs = []
    seen_keys = set()

    print(f"[Jobs Agent] Searching for: {queries}")

    for query in queries:
        # fetch_all_jobs handles calling all 3 APIs and deduplication within that call
        jobs = fetch_all_jobs(query, max_per_source=max_per_query)

        for job in jobs:
            # Deduplicate across all queries using (title, company) key
            key = (job["title"].lower().strip(), job["company"].lower().strip())
            if key not in seen_keys:
                seen_keys.add(key)
                all_jobs.append(job)

    print(f"[Jobs Agent] Found {len(all_jobs)} unique jobs total.")

    # Save to DB (clears old jobs and inserts fresh ones)
    save_jobs(all_jobs)

    return all_jobs

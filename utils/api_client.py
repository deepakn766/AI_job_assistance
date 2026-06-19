"""
utils/api_client.py
-------------------
Fetches real job listings from 3 free APIs:

1. RemoteOK    — Remote tech jobs (no key needed)
2. Arbeitnow   — Remote/EU jobs (no key needed)
3. Adzuna      — Global jobs (free key from developer.adzuna.com)

Each function returns a list of normalized job dicts:
  {
    "title":       str,
    "company":     str,
    "location":    str,
    "description": str,
    "url":         str,
    "source":      str
  }
"""

import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

ADZUNA_APP_ID  = os.getenv("ADZUNA_APP_ID", "")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY", "")

HEADERS = {
    "User-Agent": "JobAssistantBot/1.0 (personal project)"
}


# ─── RemoteOK ─────────────────────────────────────────────────────────────────

def fetch_remoteok(query: str, max_results: int = 20) -> list[dict]:
    """
    RemoteOK returns all remote tech jobs as JSON.
    We filter by matching the query against job tags and titles.
    No API key required.
    """
    url = "https://remoteok.com/api"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()

        # First item is a legal notice, skip it
        jobs_raw = [item for item in data if isinstance(item, dict) and "position" in item]

        query_lower = query.lower()
        results = []

        for job in jobs_raw:
            title = job.get("position", "")
            tags  = " ".join(job.get("tags", []))
            # Simple keyword match
            if query_lower in title.lower() or query_lower in tags.lower():
                results.append({
                    "title":       title,
                    "company":     job.get("company", "Unknown"),
                    "location":    "Remote",
                    "description": job.get("description", "")[:2000],  # Trim long descriptions
                    "url":         job.get("url", ""),
                    "source":      "RemoteOK"
                })
            if len(results) >= max_results:
                break

        return results

    except Exception as e:
        print(f"[RemoteOK Error] {e}")
        return []


# ─── Arbeitnow ────────────────────────────────────────────────────────────────

def fetch_arbeitnow(query: str, max_results: int = 20) -> list[dict]:
    """
    Arbeitnow is a free job board API with remote-friendly listings.
    Supports keyword search via `?search=` query param.
    No API key required.
    """
    url = "https://www.arbeitnow.com/api/job-board-api"
    params = {"search": query}

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        jobs_raw = data.get("data", [])

        results = []
        for job in jobs_raw[:max_results]:
            results.append({
                "title":       job.get("title", ""),
                "company":     job.get("company_name", "Unknown"),
                "location":    job.get("location", "Remote"),
                "description": job.get("description", "")[:2000],
                "url":         job.get("url", ""),
                "source":      "Arbeitnow"
            })
        return results

    except Exception as e:
        print(f"[Arbeitnow Error] {e}")
        return []


# ─── Adzuna ───────────────────────────────────────────────────────────────────

def fetch_adzuna(query: str, max_results: int = 20) -> list[dict]:
    """
    Adzuna is a global job aggregator with a free API tier.
    Requires ADZUNA_APP_ID and ADZUNA_APP_KEY in .env
    Get a free key at: https://developer.adzuna.com/
    """
    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        print("[Adzuna] No API keys found. Skipping.")
        return []

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"  # 'in' = India
    params = {
        "app_id":    ADZUNA_APP_ID,
        "app_key":   ADZUNA_APP_KEY,
        "what":      query,
        "results_per_page": max_results,
        "content-type": "application/json"
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        jobs_raw = data.get("results", [])

        results = []
        for job in jobs_raw:
            results.append({
                "title":       job.get("title", ""),
                "company":     job.get("company", {}).get("display_name", "Unknown"),
                "location":    job.get("location", {}).get("display_name", "Unknown"),
                "description": job.get("description", "")[:2000],
                "url":         job.get("redirect_url", ""),
                "source":      "Adzuna"
            })
        return results

    except Exception as e:
        print(f"[Adzuna Error] {e}")
        return []


# ─── Combined Fetcher ─────────────────────────────────────────────────────────

def fetch_all_jobs(query: str, max_per_source: int = 15) -> list[dict]:
    """
    Fetch jobs from all three sources and deduplicate by title+company.
    Returns a combined, deduplicated list.
    """
    all_jobs = []

    # Fetch from each source
    all_jobs.extend(fetch_remoteok(query, max_per_source))
    time.sleep(0.5)  # Polite delay between API calls
    all_jobs.extend(fetch_arbeitnow(query, max_per_source))
    time.sleep(0.5)
    all_jobs.extend(fetch_adzuna(query, max_per_source))

    # Deduplicate by (title, company) pair
    seen = set()
    unique_jobs = []
    for job in all_jobs:
        key = (job["title"].lower().strip(), job["company"].lower().strip())
        if key not in seen and job["title"] and job["description"]:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs

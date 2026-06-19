"""
utils/database.py
-----------------
Handles all SQLite database operations for the Job Application Tracker.

Tables:
  - profiles     : Parsed resume data (skills, domain, etc.)
  - jobs         : Fetched jobs from APIs
  - applications : Tracked job applications with status
"""

import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "app.db")


def get_connection():
    """Return a SQLite connection with row_factory for dict-like rows."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn


def init_db():
    """Create all tables if they don't exist. Call once on app startup."""
    conn = get_connection()
    cursor = conn.cursor()

    # --- Profile Table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT,
            email       TEXT,
            skills      TEXT,   -- JSON list
            domain      TEXT,
            experience  TEXT,   -- JSON list
            education   TEXT,   -- JSON list
            raw_text    TEXT,
            created_at  TEXT
        )
    """)

    # --- Jobs Table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT,
            company     TEXT,
            location    TEXT,
            description TEXT,
            url         TEXT,
            source      TEXT,
            match_score REAL DEFAULT 0,
            fetched_at  TEXT
        )
    """)

    # --- Application Tracker Table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            company      TEXT,
            role         TEXT,
            status       TEXT DEFAULT 'Saved',
            match_score  REAL,
            apply_url    TEXT,
            notes        TEXT,
            applied_date TEXT
        )
    """)

    conn.commit()
    conn.close()


# ─── Profile Operations ───────────────────────────────────────────────────────

def save_profile(profile: dict) -> int:
    """Insert or replace the candidate profile. Returns the row id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO profiles (name, email, skills, domain, experience, education, raw_text, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        profile.get("name", ""),
        profile.get("email", ""),
        json.dumps(profile.get("skills", [])),
        profile.get("domain", ""),
        json.dumps(profile.get("experience", [])),
        json.dumps(profile.get("education", [])),
        profile.get("raw_text", ""),
        datetime.now().isoformat()
    ))
    row_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return row_id


def get_latest_profile() -> dict | None:
    """Fetch the most recently saved profile."""
    conn = get_connection()
    cursor = conn.cursor()
    row = cursor.execute(
        "SELECT * FROM profiles ORDER BY id DESC LIMIT 1"
    ).fetchone()
    conn.close()
    if not row:
        return None
    profile = dict(row)
    # Deserialize JSON fields
    profile["skills"] = json.loads(profile.get("skills") or "[]")
    profile["experience"] = json.loads(profile.get("experience") or "[]")
    profile["education"] = json.loads(profile.get("education") or "[]")
    return profile


# ─── Jobs Operations ──────────────────────────────────────────────────────────

def save_jobs(jobs: list[dict]):
    """Bulk-insert fetched jobs. Clears old jobs first to avoid stale data."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs")  # Fresh slate each search
    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, description, url, source, match_score, fetched_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job.get("title", ""),
            job.get("company", ""),
            job.get("location", "Remote"),
            job.get("description", ""),
            job.get("url", ""),
            job.get("source", ""),
            job.get("match_score", 0.0),
            datetime.now().isoformat()
        ))
    conn.commit()
    conn.close()


def get_jobs(min_score: float = 0.0) -> list[dict]:
    """Retrieve jobs, optionally filtered by minimum match score."""
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute(
        "SELECT * FROM jobs WHERE match_score >= ? ORDER BY match_score DESC",
        (min_score,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ─── Application Tracker Operations ──────────────────────────────────────────

def add_application(app: dict) -> int:
    """Add a new job application to the tracker."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO applications (company, role, status, match_score, apply_url, notes, applied_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        app.get("company", ""),
        app.get("role", ""),
        app.get("status", "Saved"),
        app.get("match_score", 0.0),
        app.get("apply_url", ""),
        app.get("notes", ""),
        datetime.now().strftime("%Y-%m-%d")
    ))
    row_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return row_id


def get_applications() -> list[dict]:
    """Fetch all tracked applications ordered by most recent."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM applications ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_application_status(app_id: int, status: str):
    """Update the status of a tracked application."""
    conn = get_connection()
    conn.execute(
        "UPDATE applications SET status = ? WHERE id = ?",
        (status, app_id)
    )
    conn.commit()
    conn.close()


def delete_application(app_id: int):
    """Remove an application from the tracker."""
    conn = get_connection()
    conn.execute("DELETE FROM applications WHERE id = ?", (app_id,))
    conn.commit()
    conn.close()

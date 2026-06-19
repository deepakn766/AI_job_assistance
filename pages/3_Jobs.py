# """
# pages/3_Jobs.py
# ---------------
# Page 3: Job Matches

# 1. Fetches real jobs from APIs based on detected domain
# 2. Runs semantic matching against resume
# 3. Displays ranked job cards with match scores
# 4. Allows adding jobs to Application Tracker
# """
# from utils.ui_theme import apply_theme, render_header, render_footer

# apply_theme()
# render_header()
# import streamlit as st
# import os, sys

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# from utils.database import get_latest_profile, get_jobs, add_application
# from agents.jobs_agent import search_jobs
# from agents.matching_agent import match_jobs

# st.set_page_config(page_title="Job Matches", page_icon="🔍", layout="wide")

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
# html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
# .stButton > button {
#     background: linear-gradient(135deg, #3b82f6, #2563eb);
#     color: white; border: none; border-radius: 8px; font-weight: 600;
# }
# .job-card {
#     background:white;border-radius:12px;padding:20px;margin:10px 0;
#     box-shadow:0 1px 3px rgba(0,0,0,0.08);border-left:4px solid #3b82f6;
# }
# .skill-tag { background:#f1f5f9;color:#475569;padding:2px 8px;border-radius:12px;font-size:12px;margin:2px;display:inline-block; }
# .match-tag { background:#dbeafe;color:#1e40af;padding:2px 8px;border-radius:12px;font-size:12px;margin:2px;display:inline-block; }
# .missing-tag { background:#fee2e2;color:#991b1b;padding:2px 8px;border-radius:12px;font-size:12px;margin:2px;display:inline-block; }
# #MainMenu, footer { visibility: hidden; }
# </style>
# """, unsafe_allow_html=True)

# # ─── Load Profile ─────────────────────────────────────────────────────────────

# profile = st.session_state.get("profile") or get_latest_profile()

# if not profile:
#     st.warning("⚠️ No resume analyzed yet. Please go to **Upload Resume** first.")
#     st.stop()

# # ─── Header ──────────────────────────────────────────────────────────────────

# st.markdown("# 🔍 Job Matches")
# st.markdown(f"Finding jobs for **{profile.get('name', 'you')}** — Detected role: **{profile.get('domain', 'Unknown')}**")
# st.markdown("---")

# # ─── Search Controls ──────────────────────────────────────────────────────────

# col1, col2, col3 = st.columns([2, 1, 1])

# with col1:
#     custom_query = st.text_input(
#         "🔎 Override search query (optional)",
#         placeholder=f"Default: {profile.get('domain', 'software engineer')}",
#         help="Leave empty to use auto-detected domain"
#     )

# with col2:
#     min_score = st.slider("Min Match Score %", min_value=0, max_value=80, value=0, step=5)

# with col3:
#     st.markdown("<br>", unsafe_allow_html=True)
#     search_clicked = st.button("🚀 Search Jobs", use_container_width=True)

# # ─── Job Search + Matching Pipeline ──────────────────────────────────────────

# if search_clicked:
#     domain = custom_query.strip() if custom_query.strip() else profile.get("domain", "software engineer")
#     skills = profile.get("skills", [])

#     with st.spinner("🌐 Fetching real jobs from APIs..."):
#         jobs = search_jobs(domain, skills, max_per_query=15)

#     if not jobs:
#         st.error("No jobs found. APIs may be temporarily unavailable. Try again or check your internet connection.")
#         st.stop()

#     st.info(f"✅ Found **{len(jobs)}** jobs. Running semantic matching...")

#     with st.spinner("🧮 Computing AI match scores (embeddings)..."):
#         raw_text = profile.get("raw_text", " ".join(skills))
#         matched_jobs = match_jobs(raw_text, jobs, skills)

#     # Store in session for other pages
#     st.session_state["matched_jobs"] = matched_jobs
#     st.success(f"🎯 Matching complete! Showing {len(matched_jobs)} jobs sorted by relevance.")

# # ─── Display Jobs ──────────────────────────────────────────────────────────────

# # Load from session or DB
# jobs_to_show = st.session_state.get("matched_jobs") or get_jobs(min_score=min_score / 100)

# # Apply min score filter
# if min_score > 0:
#     jobs_to_show = [j for j in jobs_to_show if j.get("match_score", 0) >= min_score]

# if not jobs_to_show:
#     st.markdown("""
#     <div style="text-align:center;padding:60px;color:#94a3b8">
#         <div style="font-size:64px">🔍</div>
#         <div style="font-size:18px;margin-top:16px">No jobs loaded yet</div>
#         <div style="font-size:14px;margin-top:8px">Click "Search Jobs" to fetch real listings</div>
#     </div>
#     """, unsafe_allow_html=True)
# else:
#     st.markdown(f"### Showing {len(jobs_to_show)} jobs (sorted by match score)")
#     st.markdown("---")

#     for i, job in enumerate(jobs_to_show[:30]):  # Show max 30
#         score = job.get("match_score", 0)

#         # Color-code by score
#         if score >= 60:
#             border_color = "#22c55e"
#             score_bg = "#dcfce7"
#             score_color = "#166534"
#             score_label = "Strong Match"
#         elif score >= 35:
#             border_color = "#f59e0b"
#             score_bg = "#fef9c3"
#             score_color = "#854d0e"
#             score_label = "Good Match"
#         else:
#             border_color = "#ef4444"
#             score_bg = "#fee2e2"
#             score_color = "#991b1b"
#             score_label = "Partial Match"

#         st.markdown(f"""
#         <div style="background:white;border-radius:12px;padding:20px;margin:10px 0;
#                     box-shadow:0 1px 3px rgba(0,0,0,0.08);border-left:4px solid {border_color}">
#             <div style="display:flex;justify-content:space-between;align-items:flex-start">
#                 <div style="flex:1">
#                     <div style="font-size:18px;font-weight:700;color:#0f172a">{job.get('title','')}</div>
#                     <div style="font-size:14px;color:#64748b;margin-top:4px">
#                         🏢 {job.get('company','')} &nbsp;|&nbsp; 📍 {job.get('location','Remote')} &nbsp;|&nbsp; 🌐 {job.get('source','')}
#                     </div>
#                 </div>
#                 <div style="text-align:right;margin-left:20px">
#                     <div style="background:{score_bg};color:{score_color};padding:8px 16px;border-radius:20px;font-weight:700;font-size:20px">
#                         {score:.0f}%
#                     </div>
#                     <div style="font-size:11px;color:{score_color};margin-top:4px">{score_label}</div>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

#         # Skills matching
#         matching = job.get("matching_skills", [])
#         missing = job.get("missing_skills", [])

#         if matching:
#             match_badges = " ".join([f'<span class="match-tag">✓ {s}</span>' for s in matching[:6]])
#             st.markdown(f"<div style='margin-top:10px'><b style='font-size:12px;color:#166534'>Your matching skills:</b><br>{match_badges}</div>", unsafe_allow_html=True)

#         if missing:
#             miss_badges = " ".join([f'<span class="missing-tag">✗ {s}</span>' for s in missing[:4]])
#             st.markdown(f"<div style='margin-top:6px'><b style='font-size:12px;color:#991b1b'>Skills to develop:</b><br>{miss_badges}</div>", unsafe_allow_html=True)

#         # Description preview
#         desc = job.get("description", "")
#         if desc:
#             st.markdown(f"""
#             <div style="margin-top:12px;font-size:13px;color:#64748b;line-height:1.5">
#                 {desc[:300]}{'...' if len(desc) > 300 else ''}
#             </div>
#             """, unsafe_allow_html=True)

#         st.markdown("</div>", unsafe_allow_html=True)

#         # Action buttons
#         col_a, col_b, col_c = st.columns([1, 1, 2])
#         with col_a:
#             if st.button(f"💾 Save to Tracker", key=f"save_{i}"):
#                 add_application({
#                     "company": job.get("company", ""),
#                     "role": job.get("title", ""),
#                     "status": "Saved",
#                     "match_score": score,
#                     "apply_url": job.get("url", ""),
#                     "notes": f"Source: {job.get('source', '')}"
#                 })
#                 st.toast(f"✅ Saved: {job.get('title')} at {job.get('company')}")

#         with col_b:
#             if job.get("url"):
#                 st.link_button("🔗 Apply Now", job["url"])

#         with col_c:
#             if st.button(f"🎯 Use for Optimization", key=f"opt_{i}"):
#                 st.session_state["selected_job"] = job
#                 st.toast("✅ Job selected! Go to ATS Optimizer.")

#         st.markdown("&nbsp;")  # Spacer

# render_footer()

"""
pages/3_Jobs.py
---------------
Page 3: Job Matches

1. Fetches real jobs from APIs based on detected domain
2. Runs semantic matching against resume
3. Displays ranked job cards with match scores
4. Allows adding jobs to Application Tracker
"""
import streamlit as st
import os, sys

st.set_page_config(page_title="Job Matches", page_icon="🔍", layout="wide")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.ui_theme import apply_theme, render_header, render_footer

from utils.database import get_latest_profile, get_jobs, add_application
from agents.jobs_agent import search_jobs
from agents.matching_agent import match_jobs

apply_theme()
render_header()
st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

# ─── Load Profile ─────────────────────────────────────────────────────────────

profile = st.session_state.get("profile") or get_latest_profile()

if not profile:
    st.warning("⚠️ No resume analyzed yet. Please go to **Upload Resume** first.")
    st.stop()

# ─── Header ──────────────────────────────────────────────────────────────────

st.markdown(f"""
<div class="jobs-hero">
    <div>
        <h1>🔍 Job Matches</h1>
        <p>Finding jobs for <b>{profile.get('name', 'you')}</b> — detected role: <b>{profile.get('domain', 'Unknown')}</b></p>
    </div>
    <div class="page-badge">AI Job Matching</div>
</div>
""", unsafe_allow_html=True)

# ─── Search Controls ──────────────────────────────────────────────────────────

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    custom_query = st.text_input(
        "🔎 Override search query (optional)",
        placeholder=f"Default: {profile.get('domain', 'software engineer')}",
        help="Leave empty to use auto-detected domain"
    )

with col2:
    min_score = st.slider("Min Match Score %", min_value=0, max_value=80, value=0, step=5)

with col3:
    st.markdown("<br>", unsafe_allow_html=True)
    search_clicked = st.button("🚀 Search Jobs", use_container_width=True)

# ─── Job Search + Matching Pipeline ──────────────────────────────────────────

if search_clicked:
    domain = custom_query.strip() if custom_query.strip() else profile.get("domain", "software engineer")
    skills = profile.get("skills", [])

    with st.spinner("🌐 Fetching real jobs from APIs..."):
        jobs = search_jobs(domain, skills, max_per_query=15)

    if not jobs:
        st.error("No jobs found. APIs may be temporarily unavailable. Try again or check your internet connection.")
        st.stop()

    st.info(f"✅ Found **{len(jobs)}** jobs. Running semantic matching...")

    with st.spinner("🧮 Computing AI match scores (embeddings)..."):
        raw_text = profile.get("raw_text", " ".join(skills))
        matched_jobs = match_jobs(raw_text, jobs, skills)

    # Store in session for other pages
    st.session_state["matched_jobs"] = matched_jobs
    st.success(f"🎯 Matching complete! Showing {len(matched_jobs)} jobs sorted by relevance.")

# ─── Display Jobs ──────────────────────────────────────────────────────────────

# Load from session or DB
jobs_to_show = st.session_state.get("matched_jobs") or get_jobs(min_score=min_score / 100)

# Apply min score filter
if min_score > 0:
    jobs_to_show = [j for j in jobs_to_show if j.get("match_score", 0) >= min_score]

if not jobs_to_show:
    st.markdown("""
    <div style="text-align:center;padding:60px;color:#94a3b8">
        <div style="font-size:64px">🔍</div>
        <div style="font-size:18px;margin-top:16px">No jobs loaded yet</div>
        <div style="font-size:14px;margin-top:8px">Click "Search Jobs" to fetch real listings</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"### Showing {len(jobs_to_show)} jobs (sorted by match score)")
    st.markdown("---")

    for i, job in enumerate(jobs_to_show[:30]):  # Show max 30
        score = job.get("match_score", 0)

        # Color-code by score
        if score >= 60:
            border_color = "#22c55e"
            score_bg = "#dcfce7"
            score_color = "#166534"
            score_label = "Strong Match"
        elif score >= 35:
            border_color = "#f59e0b"
            score_bg = "#fef9c3"
            score_color = "#854d0e"
            score_label = "Good Match"
        else:
            border_color = "#ef4444"
            score_bg = "#fee2e2"
            score_color = "#991b1b"
            score_label = "Partial Match"

        st.markdown(f"""
        <div style="background:white;border-radius:12px;padding:20px;margin:10px 0;
                    box-shadow:0 1px 3px rgba(0,0,0,0.08);border-left:4px solid {border_color}">
            <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <div style="flex:1">
                    <div style="font-size:18px;font-weight:700;color:#0f172a">{job.get('title','')}</div>
                    <div style="font-size:14px;color:#64748b;margin-top:4px">
                        🏢 {job.get('company','')} &nbsp;|&nbsp; 📍 {job.get('location','Remote')} &nbsp;|&nbsp; 🌐 {job.get('source','')}
                    </div>
                </div>
                <div style="text-align:right;margin-left:20px">
                    <div style="background:{score_bg};color:{score_color};padding:8px 16px;border-radius:20px;font-weight:700;font-size:20px">
                        {score:.0f}%
                    </div>
                    <div style="font-size:11px;color:{score_color};margin-top:4px">{score_label}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Skills matching
        matching = job.get("matching_skills", [])
        missing = job.get("missing_skills", [])

        if matching:
            match_badges = " ".join([f'<span class="match-tag">✓ {s}</span>' for s in matching[:6]])
            st.markdown(f"<div style='margin-top:10px'><b style='font-size:12px;color:#166534'>Your matching skills:</b><br>{match_badges}</div>", unsafe_allow_html=True)

        if missing:
            miss_badges = " ".join([f'<span class="missing-tag">✗ {s}</span>' for s in missing[:4]])
            st.markdown(f"<div style='margin-top:6px'><b style='font-size:12px;color:#991b1b'>Skills to develop:</b><br>{miss_badges}</div>", unsafe_allow_html=True)

        # Description preview
        desc = job.get("description", "")
        if desc:
            st.markdown(f"""
            <div style="margin-top:12px;font-size:13px;color:#64748b;line-height:1.5">
                {desc[:300]}{'...' if len(desc) > 300 else ''}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Action buttons
        col_a, col_b, col_c = st.columns([1, 1, 2])
        with col_a:
            if st.button(f"💾 Save to Tracker", key=f"save_{i}"):
                add_application({
                    "company": job.get("company", ""),
                    "role": job.get("title", ""),
                    "status": "Saved",
                    "match_score": score,
                    "apply_url": job.get("url", ""),
                    "notes": f"Source: {job.get('source', '')}"
                })
                st.toast(f"✅ Saved: {job.get('title')} at {job.get('company')}")

        with col_b:
            if job.get("url"):
                st.link_button("🔗 Apply Now", job["url"])

        with col_c:
            if st.button(f"🎯 Use for Optimization", key=f"opt_{i}"):
                st.session_state["selected_job"] = job
                st.toast("✅ Job selected! Go to ATS Optimizer.")

        st.markdown("&nbsp;")  # Spacer

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
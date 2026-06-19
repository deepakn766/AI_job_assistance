# """
# pages/4_Resume_Optimizer.py
# ---------------------------
# Page 4: ATS Resume Optimizer

# Takes the candidate's profile + a selected job description.
# Uses Groq to generate an ATS-optimized version of the resume.
# Outputs: formatted text view + downloadable DOCX.
# """
# from utils.ui_theme import apply_theme, render_header, render_footer

# apply_theme()
# render_header()
# import streamlit as st
# import os, sys

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# from utils.database import get_latest_profile, get_jobs
# from agents.resume_optimizer_agent import optimize_resume

# st.set_page_config(page_title="ATS Optimizer", page_icon="✨", layout="wide")

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
# html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
# .stButton > button {
#     background: linear-gradient(135deg, #3b82f6, #2563eb);
#     color: white; border: none; border-radius: 8px; font-weight: 600;
# }
# .resume-section {
#     background:white;border-radius:12px;padding:20px;margin:10px 0;
#     box-shadow:0 1px 3px rgba(0,0,0,0.08);
# }
# .keyword-badge {
#     background:#dcfce7;color:#166534;padding:3px 10px;border-radius:12px;
#     font-size:12px;margin:2px;display:inline-block;
# }
# #MainMenu, footer { visibility: hidden; }
# </style>
# """, unsafe_allow_html=True)

# # ─── Load Data ────────────────────────────────────────────────────────────────

# profile = st.session_state.get("profile") or get_latest_profile()

# if not profile:
#     st.warning("⚠️ No resume analyzed yet. Please go to **Upload Resume** first.")
#     st.stop()

# # ─── Header ──────────────────────────────────────────────────────────────────

# st.markdown("# ✨ ATS Resume Optimizer")
# st.markdown("Generate an ATS-friendly, tailored resume for a specific job using AI.")
# st.markdown("---")

# # ─── Job Selection ─────────────────────────────────────────────────────────────

# st.markdown("## 1. Select Target Job")

# # Check if a job was pre-selected from the Jobs page
# preselected = st.session_state.get("selected_job")
# jobs_from_db = get_jobs()

# # Build job options
# job_options = {}
# if preselected:
#     key = f"✅ [Pre-selected] {preselected.get('title', '')} at {preselected.get('company', '')}"
#     job_options[key] = preselected

# for job in jobs_from_db[:20]:  # Limit dropdown to 20
#     key = f"{job.get('title', 'Unknown')} at {job.get('company', 'Unknown')} [{job.get('source', '')}] — {job.get('match_score', 0):.0f}% match"
#     job_options[key] = job

# col1, col2 = st.columns([3, 1])

# with col1:
#     if job_options:
#         selected_key = st.selectbox("Choose a job to optimize for:", options=list(job_options.keys()))
#         selected_job = job_options[selected_key]
#     else:
#         st.info("No jobs fetched yet. Go to **Job Matches** first, or paste a job description below.")
#         selected_job = None

# # Option to paste custom job description
# st.markdown("**Or paste a custom job description:**")
# custom_jd = st.text_area(
#     "Custom Job Description",
#     height=150,
#     placeholder="Paste any job description here to optimize your resume for it..."
# )

# if custom_jd.strip():
#     selected_job = {
#         "title": "Custom Role",
#         "company": "Target Company",
#         "description": custom_jd,
#         "url": "",
#         "source": "Custom"
#     }
#     st.success("✅ Using custom job description")

# st.markdown("---")

# # ─── Generate Button ──────────────────────────────────────────────────────────

# st.markdown("## 2. Generate Optimized Resume")

# if selected_job:
#     st.markdown(f"""
#     <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:12px 16px">
#         <b>Target:</b> {selected_job.get('title', '')} at {selected_job.get('company', '')}
#         &nbsp;|&nbsp; <b>Match Score:</b> {selected_job.get('match_score', 0):.0f}%
#     </div>
#     """, unsafe_allow_html=True)
# else:
#     st.warning("Please select a job or paste a job description above.")

# st.markdown("")

# generate_clicked = st.button("🤖 Generate ATS-Optimized Resume", use_container_width=True, disabled=not selected_job)

# # ─── Generation + Results ─────────────────────────────────────────────────────

# if generate_clicked and selected_job:

#     with st.spinner("🧠 AI is optimizing your resume... (this takes 15-30 seconds)"):
#         optimized = optimize_resume(profile, selected_job)

#     st.success("✅ Resume optimized! Scroll down to see the result.")
#     st.session_state["optimized_resume"] = optimized
#     st.markdown("---")

# # Show results if available
# if st.session_state.get("optimized_resume"):
#     opt = st.session_state["optimized_resume"]

#     st.markdown("## 3. Your Optimized Resume")

#     # Download button
#     docx_path = opt.get("docx_path", "")
#     if docx_path and os.path.exists(docx_path):
#         with open(docx_path, "rb") as f:
#             docx_bytes = f.read()
#         st.download_button(
#             label="📥 Download as DOCX",
#             data=docx_bytes,
#             file_name=os.path.basename(docx_path),
#             mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
#             use_container_width=False
#         )

#     st.markdown("---")

#     # Professional Summary
#     st.markdown("""
#     <div class="resume-section">
#         <h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">PROFESSIONAL SUMMARY</h3>
#     """, unsafe_allow_html=True)
#     st.markdown(f'<p style="color:#374151;line-height:1.7">{opt.get("summary", "")}</p>', unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)

#     # Skills
#     skills = opt.get("skills_section", [])
#     if skills:
#         st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">TECHNICAL SKILLS</h3>""", unsafe_allow_html=True)
#         badges = " ".join([f'<span style="background:#f1f5f9;color:#475569;padding:4px 10px;border-radius:8px;font-size:13px;margin:3px;display:inline-block">{s}</span>' for s in skills])
#         st.markdown(badges, unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Experience
#     exp_bullets = opt.get("experience_bullets", [])
#     if exp_bullets:
#         st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">EXPERIENCE</h3>""", unsafe_allow_html=True)
#         for bullet in exp_bullets:
#             st.markdown(f'<p style="color:#374151;margin:6px 0">{bullet}</p>', unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Projects
#     proj_bullets = opt.get("projects_bullets", [])
#     if proj_bullets:
#         st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">PROJECTS</h3>""", unsafe_allow_html=True)
#         for bullet in proj_bullets:
#             st.markdown(f'<p style="color:#374151;margin:6px 0">{bullet}</p>', unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Education
#     education = opt.get("education", [])
#     if education:
#         st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">EDUCATION</h3>""", unsafe_allow_html=True)
#         for edu in education:
#             st.markdown(f'<p style="color:#374151;margin:6px 0">{edu}</p>', unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Keywords added
#     kw = opt.get("keywords_added", [])
#     if kw:
#         st.markdown("---")
#         st.markdown("### 🔑 Keywords Added for ATS Alignment")
#         badges = " ".join([f'<span class="keyword-badge">+ {k}</span>' for k in kw])
#         st.markdown(badges, unsafe_allow_html=True)
#         st.caption("These keywords were naturally woven in from the job description to improve ATS ranking.")

#     st.markdown("---")
#     st.info("💡 **Tip:** Download the DOCX and submit it. The formatting is ATS-safe (no tables or text boxes).")
# render_footer()
"""
pages/4_Resume_Optimizer.py
---------------------------
Page 4: ATS Resume Optimizer

Takes the candidate's profile + a selected job description.
Uses Groq to generate an ATS-optimized version of the resume.
Outputs: formatted text view + downloadable DOCX.
"""
import streamlit as st
import os, sys

st.set_page_config(page_title="ATS Optimizer", page_icon="✨", layout="wide")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.ui_theme import apply_theme, render_header, render_footer

from utils.database import get_latest_profile, get_jobs
from agents.resume_optimizer_agent import optimize_resume

apply_theme()
render_header()
st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

# ─── Load Data ────────────────────────────────────────────────────────────────

profile = st.session_state.get("profile") or get_latest_profile()

if not profile:
    st.warning("⚠️ No resume analyzed yet. Please go to **Upload Resume** first.")
    st.stop()

# ─── Header ──────────────────────────────────────────────────────────────────

st.markdown("""
<div class="optimizer-hero">
    <div>
        <h1>✨ ATS Resume Optimizer</h1>
        <p>Generate an ATS-friendly, tailored resume for a specific job using AI.</p>
    </div>
    <div class="page-badge">ATS Optimizer</div>
</div>
""", unsafe_allow_html=True)

# ─── Job Selection ─────────────────────────────────────────────────────────────

st.markdown("## 1. Select Target Job")

# Check if a job was pre-selected from the Jobs page
preselected = st.session_state.get("selected_job")
jobs_from_db = get_jobs()

# Build job options
job_options = {}
if preselected:
    key = f"✅ [Pre-selected] {preselected.get('title', '')} at {preselected.get('company', '')}"
    job_options[key] = preselected

for job in jobs_from_db[:20]:  # Limit dropdown to 20
    key = f"{job.get('title', 'Unknown')} at {job.get('company', 'Unknown')} [{job.get('source', '')}] — {job.get('match_score', 0):.0f}% match"
    job_options[key] = job

col1, col2 = st.columns([3, 1])

with col1:
    if job_options:
        selected_key = st.selectbox("Choose a job to optimize for:", options=list(job_options.keys()))
        selected_job = job_options[selected_key]
    else:
        st.info("No jobs fetched yet. Go to **Job Matches** first, or paste a job description below.")
        selected_job = None

# Option to paste custom job description
st.markdown("**Or paste a custom job description:**")
custom_jd = st.text_area(
    "Custom Job Description",
    height=150,
    placeholder="Paste any job description here to optimize your resume for it..."
)

if custom_jd.strip():
    selected_job = {
        "title": "Custom Role",
        "company": "Target Company",
        "description": custom_jd,
        "url": "",
        "source": "Custom"
    }
    st.success("✅ Using custom job description")

st.markdown("---")

# ─── Generate Button ──────────────────────────────────────────────────────────

st.markdown("## 2. Generate Optimized Resume")

if selected_job:
    st.markdown(f"""
    <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:12px 16px">
        <b>Target:</b> {selected_job.get('title', '')} at {selected_job.get('company', '')}
        &nbsp;|&nbsp; <b>Match Score:</b> {selected_job.get('match_score', 0):.0f}%
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("Please select a job or paste a job description above.")

st.markdown("")

generate_clicked = st.button("🤖 Generate ATS-Optimized Resume", use_container_width=True, disabled=not selected_job)

# ─── Generation + Results ─────────────────────────────────────────────────────

if generate_clicked and selected_job:

    with st.spinner("🧠 AI is optimizing your resume... (this takes 15-30 seconds)"):
        optimized = optimize_resume(profile, selected_job)

    st.success("✅ Resume optimized! Scroll down to see the result.")
    st.session_state["optimized_resume"] = optimized
    st.markdown("---")

# Show results if available
if st.session_state.get("optimized_resume"):
    opt = st.session_state["optimized_resume"]

    st.markdown("## 3. Your Optimized Resume")

    # Download button
    docx_path = opt.get("docx_path", "")
    if docx_path and os.path.exists(docx_path):
        with open(docx_path, "rb") as f:
            docx_bytes = f.read()
        st.download_button(
            label="📥 Download as DOCX",
            data=docx_bytes,
            file_name=os.path.basename(docx_path),
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=False
        )

    st.markdown("---")

    # Professional Summary
    st.markdown("""
    <div class="resume-section">
        <h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">PROFESSIONAL SUMMARY</h3>
    """, unsafe_allow_html=True)
    st.markdown(f'<p style="color:#374151;line-height:1.7">{opt.get("summary", "")}</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Skills
    skills = opt.get("skills_section", [])
    if skills:
        st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">TECHNICAL SKILLS</h3>""", unsafe_allow_html=True)
        badges = " ".join([f'<span style="background:#f1f5f9;color:#475569;padding:4px 10px;border-radius:8px;font-size:13px;margin:3px;display:inline-block">{s}</span>' for s in skills])
        st.markdown(badges, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Experience
    exp_bullets = opt.get("experience_bullets", [])
    if exp_bullets:
        st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">EXPERIENCE</h3>""", unsafe_allow_html=True)
        for bullet in exp_bullets:
            st.markdown(f'<p style="color:#374151;margin:6px 0">{bullet}</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Projects
    proj_bullets = opt.get("projects_bullets", [])
    if proj_bullets:
        st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">PROJECTS</h3>""", unsafe_allow_html=True)
        for bullet in proj_bullets:
            st.markdown(f'<p style="color:#374151;margin:6px 0">{bullet}</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Education
    education = opt.get("education", [])
    if education:
        st.markdown("""<div class="resume-section"><h3 style="color:#1e40af;border-bottom:2px solid #bfdbfe;padding-bottom:8px">EDUCATION</h3>""", unsafe_allow_html=True)
        for edu in education:
            st.markdown(f'<p style="color:#374151;margin:6px 0">{edu}</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Keywords added
    kw = opt.get("keywords_added", [])
    if kw:
        st.markdown("---")
        st.markdown("### 🔑 Keywords Added for ATS Alignment")
        badges = " ".join([f'<span class="keyword-badge">+ {k}</span>' for k in kw])
        st.markdown(badges, unsafe_allow_html=True)
        st.caption("These keywords were naturally woven in from the job description to improve ATS ranking.")

    st.markdown("---")
    st.info("💡 **Tip:** Download the DOCX and submit it. The formatting is ATS-safe (no tables or text boxes).")
st.markdown('</div>', unsafe_allow_html=True)
render_footer()
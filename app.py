"""
app.py
------
Main entry point for the Job Application Assistant.

Run with:
    streamlit run app.py

This file:
1. Initializes the database
2. Sets up the Streamlit page config and custom theme
3. Renders the home/landing page
4. Navigation is handled via Streamlit's multipage feature (pages/ folder)
"""

import streamlit as st
import sys
import os

# Ensure project root is in Python path
sys.path.insert(0, os.path.dirname(__file__))

from utils.database import init_db
from utils.ui_theme import apply_theme, render_header, render_footer

# ─── Page Configuration ───────────────────────────────────────────────────────

st.set_page_config(
    page_title="AI Job Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()
render_header()
# ─── Custom CSS Theme ─────────────────────────────────────────────────────────

st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

st.markdown("""
<div class="hero-section">
    <div>
        <p class="eyebrow">🚀 AI POWERED CAREER AUTOMATION</p>
        <h1>AI Job Application Assistant</h1>
        <p>
            Analyze resumes, match jobs, optimize ATS content, generate outreach messages,
            and track applications — all in one smart dashboard.
        </p>
        <div class="hero-actions">
            <span>⚡ Fast Resume Analysis</span>
            <span>🎯 Smart Job Matching</span>
            <span>📊 Application Tracker</span>
        </div>
    </div>
    <div class="hero-visual">
        <div class="circle-score">92%</div>
        <p>Resume Match Score</p>
        <small>AI-ready profile detected</small>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-grid">

<div class="feature-card">
<div class="feature-icon">📄</div>
<div class="feature-title">Resume Analysis</div>
<div class="feature-desc">Extract skills and experience instantly.</div>
</div>

<div class="feature-card">
<div class="feature-icon">🎯</div>
<div class="feature-title">Job Matching</div>
<div class="feature-desc">AI powered job recommendations.</div>
</div>

<div class="feature-card">
<div class="feature-icon">✨</div>
<div class="feature-title">ATS Optimizer</div>
<div class="feature-desc">Improve ATS score automatically.</div>
</div>

<div class="feature-card">
<div class="feature-icon">📊</div>
<div class="feature-title">Tracker</div>
<div class="feature-desc">Track all applications in one place.</div>
</div>



<div class="feature-card">
<div class="feature-icon">📧</div>
<div class="feature-title">Outreach</div>
<div class="feature-desc">Generate email, cover letter and LinkedIn message.</div>
</div>

<div class="feature-card">
<div class="feature-icon">🤖</div>
<div class="feature-title">AI Pipeline</div>
<div class="feature-desc">Parse → Analyze → Search → Match → Generate.</div>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stats-grid">
    <div class="stat-card"><h2>6</h2><p>AI Modules</p></div>
    <div class="stat-card"><h2>3+</h2><p>Job Sources</p></div>
    <div class="stat-card"><h2>ATS</h2><p>Resume Optimizer</p></div>
    <div class="stat-card"><h2>24/7</h2><p>Career Assistant</p></div>
</div>
""", unsafe_allow_html=True)
# features = [
#     ("📄", "Resume Analysis", "Extract skills, experience and domain from resume."),
#     ("🔍", "Job Matching", "Match resume with real jobs using AI score."),
#     ("✨", "ATS Optimizer", "Improve resume for job description."),
#     ("📧", "Outreach", "Generate email, cover letter and LinkedIn message."),
#     ("📊", "Tracker", "Track Saved, Applied, Interview and Offer status."),
#     ("🤖", "AI Pipeline", "Parse → Analyze → Search → Match → Generate."),
# ]


# st.markdown('<div class="compact-grid">', unsafe_allow_html=True)

# for icon, title, desc in features:
#     st.markdown(f"""
#     <div class="compact-card">
#         <div class="compact-icon">{icon}</div>
#         <div>
#             <h3>{title}</h3>
#             <p>{desc}</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
# st.markdown("""
# <div class="feature-grid">
#     <div class="feature-card">
#         <h3>📄 Resume Analysis</h3>
#         <p>Upload PDF or DOCX resume and extract skills, experience, role, and domain instantly.</p>
#     </div>

#     <div class="feature-card">
#         <h3>🔍 Job Matching</h3>
#         <p>Find suitable jobs and calculate AI-based match scores using resume information.</p>
#     </div>

#     <div class="feature-card">
#         <h3>✨ ATS Optimizer</h3>
#         <p>Generate ATS-friendly resume improvements tailored to job descriptions.</p>
#     </div>

#     <div class="feature-card">
#         <h3>📧 Outreach Generator</h3>
#         <p>Create recruiter emails, cover letters, and LinkedIn messages automatically.</p>
#     </div>

#     <div class="feature-card">
#         <h3>📊 Application Tracker</h3>
#         <p>Track Saved, Applied, Interview, Offer, and Rejected application statuses.</p>
#     </div>

#     <div class="feature-card">
#         <h3>🤖 Agentic Pipeline</h3>
#         <p>AI agents work step-by-step: Parse → Analyze → Search → Match → Generate.</p>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("""
# <div class="timeline-box">
#     <h2>🚀 How It Works</h2>
#     <div class="timeline">
#         <div><b>1</b><span>Upload Resume</span></div>
#         <div><b>2</b><span>Analyze Profile</span></div>
#         <div><b>3</b><span>Match Jobs</span></div>
#         <div><b>4</b><span>Optimize Resume</span></div>
#         <div><b>5</b><span>Generate Outreach</span></div>
#         <div><b>6</b><span>Track Progress</span></div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
# """
# pages/2_Profile.py
# ------------------
# Page 2: Resume Profile Viewer
# """

# import streamlit as st
# import os
# import sys
# import json

# st.set_page_config(page_title="Resume Profile", page_icon="👤", layout="wide")

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# from utils.ui_theme import apply_theme, render_header, render_footer
# from utils.database import get_latest_profile

# apply_theme()
# render_header()

# st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

# profile = st.session_state.get("profile") or get_latest_profile()

# if not profile:
#     st.markdown("""
#     <div class="empty-upload">
#         <div>👤</div>
#         <h3>No Resume Profile Found</h3>
#         <p>Please upload and analyze your resume first.</p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)
#     render_footer()
#     st.stop()

# name = profile.get("name", "Candidate")
# email = profile.get("email", "Not found")
# domain = profile.get("domain", "Unknown")
# confidence = profile.get("domain_confidence", 0)
# skills = profile.get("skills", [])

# st.markdown(f"""
# <div class="profile-hero">
#     <div>
#         <h1>👤 {name}</h1>
#         <p>Resume profile summary generated from AI resume analysis.</p>
#     </div>
#     <div class="profile-domain">
#         <span>{domain}</span>
#         <b>{confidence}% Confidence</b>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# m1, m2, m3, m4 = st.columns(4, gap="medium")

# with m1:
#     st.metric("📧 Email", email)
# with m2:
#     st.metric("🎯 Domain", domain)
# with m3:
#     st.metric("🛠️ Skills", len(skills))
# with m4:
#     st.metric("📊 Confidence", f"{confidence}%")

# left, right = st.columns([1, 1.5], gap="large")

# with left:
#     st.markdown("""
#     <div class="profile-card">
#         <h2>🎯 Domain Detection</h2>
#     """, unsafe_allow_html=True)

#     color = "#16a34a" if confidence >= 70 else "#ca8a04" if confidence >= 40 else "#dc2626"

#     st.markdown(f"""
#         <div class="domain-circle">
#             <div>🏷️</div>
#             <h3 style="color:{color} !important;">{domain}</h3>
#             <p>Primary Role</p>
#             <h2 style="color:{color} !important;">{confidence}%</h2>
#             <small>Confidence Score</small>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with right:
#     st.markdown("""
#     <div class="profile-card">
#         <h2>🔎 Detection Method</h2>
#         <p>The system scans your resume skills, keywords, project terms and role-related phrases.</p>
#         <div class="method-grid">
#             <span>Skill Keywords</span>
#             <span>Project Terms</span>
#             <span>Role Matching</span>
#             <span>Confidence Score</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     alternatives = profile.get("domain_alternatives", [])
#     if alternatives:
#         alt_html = "".join([f"<span class='skill-badge'>🔸 {alt}</span>" for alt in alternatives])
#         st.markdown(f"""
#         <div class="profile-card small-card">
#             <h2>🔄 Alternative Roles</h2>
#             {alt_html}
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown("""
# <div class="profile-card">
#     <h2>🛠️ Extracted Skills</h2>
# """, unsafe_allow_html=True)

# if skills:
#     badges_html = " ".join([f'<span class="skill-badge">{s}</span>' for s in skills])
#     st.markdown(badges_html, unsafe_allow_html=True)
#     st.caption(f"Total: {len(skills)} skills extracted")
# else:
#     st.warning("No skills extracted. Your resume may need more technical detail.")

# st.markdown("</div>", unsafe_allow_html=True)

# col1, col2 = st.columns(2, gap="large")

# with col1:
#     st.markdown("""
#     <div class="profile-card">
#         <h2>💼 Experience</h2>
#     """, unsafe_allow_html=True)

#     experience = profile.get("experience", [])
#     if experience:
#         for exp in experience:
#             st.markdown(f"<div class='mini-section'>{exp}</div>", unsafe_allow_html=True)
#     else:
#         st.info("No experience entries extracted.")

#     st.markdown("</div>", unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="profile-card">
#         <h2>🎓 Education</h2>
#     """, unsafe_allow_html=True)

#     education = profile.get("education", [])
#     if education:
#         for edu in education:
#             st.markdown(f"<div class='mini-section'>{edu}</div>", unsafe_allow_html=True)
#     else:
#         st.info("No education entries extracted.")

#     st.markdown("</div>", unsafe_allow_html=True)

# projects = profile.get("projects", [])
# st.markdown("""
# <div class="profile-card">
#     <h2>🚀 Projects</h2>
# """, unsafe_allow_html=True)

# if projects:
#     for i, proj in enumerate(projects):
#         st.markdown(f"""
#         <div class="mini-section">
#             <b>Project {i+1}</b><br>
#             {proj}
#         </div>
#         """, unsafe_allow_html=True)
# else:
#     st.info("No projects extracted. Consider adding a projects section to your resume.")

# st.markdown("</div>", unsafe_allow_html=True)

# summary = profile.get("summary", "")
# if summary:
#     st.markdown(f"""
#     <div class="profile-card">
#         <h2>📝 AI Summary</h2>
#         <p class="summary-text">"{summary}"</p>
#     </div>
#     """, unsafe_allow_html=True)

# with st.expander("🔧 View Raw Profile JSON"):
#     display_profile = {k: v for k, v in profile.items() if k != "raw_text"}
#     st.json(display_profile)

# st.success("✅ Profile loaded! Go to **Job Matches** to find relevant jobs.")

# st.markdown('</div>', unsafe_allow_html=True)
# render_footer()

"""
pages/2_Profile.py
------------------
Page 2: Resume Profile Viewer
"""

import streamlit as st
import os
import sys
import json

st.set_page_config(page_title="Resume Profile", page_icon="👤", layout="wide")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.ui_theme import apply_theme, render_header, render_footer
from utils.database import get_latest_profile

apply_theme()
render_header()

st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

profile = st.session_state.get("profile") or get_latest_profile()

if not profile:
    st.markdown("""
    <div class="empty-upload">
        <div>👤</div>
        <h3>No Resume Profile Found</h3>
        <p>Please upload and analyze your resume first.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    render_footer()
    st.stop()

name = profile.get("name", "Candidate")
email = profile.get("email", "Not found")
domain = profile.get("domain", "Unknown")
confidence = profile.get("domain_confidence", 0)
skills = profile.get("skills", [])

st.markdown(f"""
<div class="profile-hero">
    <div>
        <h1>👤 {name}</h1>
        <p>Resume profile summary generated from AI resume analysis.</p>
    </div>
    <div class="profile-domain">
        <span>{domain}</span>
        <b>{confidence}% Confidence</b>
    </div>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4, gap="medium")

with m1:
    st.metric("📧 Email", email)
with m2:
    st.metric("🎯 Domain", domain)
with m3:
    st.metric("🛠️ Skills", len(skills))
with m4:
    st.metric("📊 Confidence", f"{confidence}%")

left, right = st.columns([1, 1.5], gap="large")

with left:
    st.markdown("""<div class="profile-card"><h2>🎯 Domain Detection</h2>""", unsafe_allow_html=True)

    color = "#16a34a" if confidence >= 70 else "#ca8a04" if confidence >= 40 else "black"

    st.markdown(f"""
        <div class="domain-circle">
            <div>🏷️</div>
            <h3 style="color:{color}">{domain}</h3>
            <p>Primary Role</p>
            <h3 style="color:{color}">{confidence}%</h3>
            <small>Confidence Score</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="profile-card">
        <h2>🔎 Detection Method</h2>
        <p>The system scans your resume skills, keywords, project terms and role-related phrases.</p>
        <div class="method-grid">
            <span>Skill Keywords</span>
            <span>Project Terms</span>
            <span>Role Matching</span>
            <span>Confidence Score</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    alternatives = profile.get("domain_alternatives", [])
    if alternatives:
        alt_html = "".join([f"<span class='skill-badge'>🔸 {alt}</span>" for alt in alternatives])
        st.markdown(f"""
        <div class="profile-card small-card">
            <h2>🔄 Alternative Roles</h2>
            {alt_html}
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="profile-card">
    <h2>🛠️ Extracted Skills</h2>
""", unsafe_allow_html=True)

if skills:
    badges_html = " ".join([f'<span class="skill-badge">{s}</span>' for s in skills])
    st.markdown(badges_html, unsafe_allow_html=True)
    st.caption(f"Total: {len(skills)} skills extracted")
else:
    st.warning("No skills extracted. Your resume may need more technical detail.")

st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="profile-card">
        <h2>💼 Experience</h2>
    """, unsafe_allow_html=True)

    experience = profile.get("experience", [])
    if experience:
        for exp in experience:
            st.markdown(f"<div class='mini-section'>{exp}</div>", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="custom-info">📋 No experience entries extracted.</div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="profile-card">
        <h2>🎓 Education</h2>
    """, unsafe_allow_html=True)

    education = profile.get("education", [])
    if education:
        for edu in education:
            st.markdown(f"<div class='mini-section'>{edu}</div>", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="custom-info">📋 No education entries extracted.</div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

projects = profile.get("projects", [])
st.markdown("""
<div class="profile-card">
    <h2>🚀 Projects</h2>
""", unsafe_allow_html=True)

if projects:
    for i, proj in enumerate(projects):
        st.markdown(f"""
        <div class="mini-section">
            <b>Project {i+1}</b><br>
            {proj}
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""<div class="custom-info">No projects extracted. Consider adding a projects section to your resume.</div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

summary = profile.get("summary", "")
if summary:
    st.markdown(f"""
    <div class="profile-card">
        <h2>📝 AI Summary</h2>
        <p class="summary-text">"{summary}"</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("🔧 View Raw Profile JSON"):
    display_profile = {k: v for k, v in profile.items() if k != "raw_text"}
    st.json(display_profile)

st.markdown("""<div class="custom-info">✅ Profile loaded! Go to **Job Matches** to find relevant jobs.</div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
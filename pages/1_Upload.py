# """
# pages/1_Upload.py
# -----------------
# Page 1: Resume Upload
# """

# import streamlit as st
# import os
# import sys
# import time

# st.set_page_config(page_title="Upload Resume", page_icon="📄", layout="wide")

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# from utils.ui_theme import apply_theme, render_header, render_footer
# from utils.parser import extract_text
# from utils.database import save_profile, get_latest_profile
# from agents.resume_agent import analyze_resume

# apply_theme()
# render_header()

# st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

# st.markdown("""
# <div class="upload-hero">
#     <div>
#         <h1>📄 Upload Your Resume</h1>
#         <p>Upload your resume and let AI extract your skills, profile, experience and domain.</p>
#     </div>
#     <div class="upload-badge">AI Resume Analyzer</div>
# </div>
# """, unsafe_allow_html=True)

# col1, col2 = st.columns([2.1, 1], gap="large")

# with col1:
#     uploaded_file = st.file_uploader(
#         "Choose your resume file",
#         type=["pdf", "docx"],
#         help="Supported formats: PDF and DOCX. Max size: 10MB.",
#         key="resume_upload"
#     )

# with col2:
#     st.markdown("""
#     <div class="tips-card">
#         <b>💡 Tips for Best Results</b><br><br>
#         ✅ Use text-based PDF<br>
#         ✅ Include technical skills<br>
#         ✅ Add projects with technologies<br>
#         ✅ Mention job responsibilities<br>
#         ✅ Keep resume ATS-friendly
#     </div>
#     """, unsafe_allow_html=True)

# if uploaded_file is not None:
#     resume_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resumes")
#     os.makedirs(resume_dir, exist_ok=True)
#     file_path = os.path.join(resume_dir, uploaded_file.name)

#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     st.success(f"✅ File uploaded: **{uploaded_file.name}** ({uploaded_file.size // 1024} KB)")

#     if st.button("🤖 Analyze Resume with AI", use_container_width=True):
#         with st.spinner(""):
#             progress = st.progress(0)
#             status = st.empty()

#             status.markdown("📖 **Step 1/4:** Extracting text from resume...")
#             progress.progress(15)
#             time.sleep(0.3)

#             raw_text = extract_text(file_path)
#             if not raw_text.strip():
#                 st.error("❌ Could not extract text from this file. Please ensure it's not a scanned/image PDF.")
#                 st.stop()

#             status.markdown("🧠 **Step 2/4:** Analyzing with AI (Groq LLaMA3)...")
#             progress.progress(40)

#             profile = analyze_resume(raw_text)

#             status.markdown("🎯 **Step 3/4:** Detecting your domain...")
#             progress.progress(70)
#             time.sleep(0.3)

#             save_profile(profile)

#             st.session_state["profile"] = profile
#             st.session_state["profile_loaded"] = True

#             status.markdown("✅ **Step 4/4:** Profile ready!")
#             progress.progress(100)
#             time.sleep(0.5)

#         progress.empty()
#         status.empty()

#         st.markdown('<div class="result-section">', unsafe_allow_html=True)
#         st.markdown("## ✨ Analysis Complete!")

#         m1, m2, m3, m4 = st.columns(4)

#         with m1:
#             st.metric("👤 Name", profile.get("name", "Unknown"))
#         with m2:
#             st.metric("🎯 Domain", profile.get("domain", "Unknown"))
#         with m3:
#             st.metric("🛠️ Skills Found", len(profile.get("skills", [])))
#         with m4:
#             st.metric("📊 Confidence", f"{profile.get('domain_confidence', 0)}%")

#         st.markdown("### 🛠️ Extracted Skills")
#         skills = profile.get("skills", [])

#         if skills:
#             badges = " ".join([
#                 f'<span style="background:#dbeafe;color:#1e40af;padding:4px 10px;border-radius:20px;font-size:13px;margin:3px;display:inline-block">{s}</span>'
#                 for s in skills[:25]
#             ])
#             st.markdown(badges, unsafe_allow_html=True)
#         else:
#             st.warning("No skills detected. Try a more detailed resume.")

#         alts = profile.get("domain_alternatives", [])
#         if alts:
#             st.info(f"🔄 **Alternative roles detected:** {', '.join(alts)}")

#         st.success("🎉 **Next step:** Go to **Job Matches** in the sidebar to find relevant jobs!")
#         st.markdown('</div>', unsafe_allow_html=True)

# else:
#     existing = get_latest_profile()

#     if existing:
#         pcol1, pcol2 = st.columns([3.2, 1], gap="medium")

#         with pcol1:
#             st.markdown(f"""
#             <div class="previous-card">
#                 <h4>📋 Previous Resume Found</h4>
#                 <p>{existing.get('name', 'Unknown')} • {existing.get('domain', 'Unknown domain')}</p>
#             </div>
#             """, unsafe_allow_html=True)

#         with pcol2:
#             st.markdown("<div class='profile-btn-space'></div>", unsafe_allow_html=True)
#             if st.button("🚀 Load Profile", use_container_width=True):
#                 st.session_state["profile"] = existing
#                 st.session_state["profile_loaded"] = True
#                 st.success("✅ Previous profile loaded!")

#     else:
#         st.markdown("""
#         <div class="empty-upload">
#             <div>📂</div>
#             <h3>Upload a resume to get started</h3>
#             <p>Supports PDF and DOCX formats</p>
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# render_footer()

"""
pages/1_Upload.py
-----------------
Page 1: Resume Upload
"""

import streamlit as st
import os
import sys
import time

st.set_page_config(page_title="Upload Resume", page_icon="📄", layout="wide")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.ui_theme import apply_theme, render_header, render_footer
from utils.parser import extract_text
from utils.database import save_profile, get_latest_profile
from agents.resume_agent import analyze_resume

apply_theme()
render_header()

st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

st.markdown("""
<div class="upload-hero">
    <div>
        <h1>📄 Upload Your Resume</h1>
        <p>Upload your resume and let AI extract your skills, profile, experience and domain.</p>
    </div>
    <div class="upload-badge">AI Resume Analyzer</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2.1, 1], gap="large")

with col1:
    uploaded_file = st.file_uploader(
        "Choose your resume file",
        type=["pdf", "docx"],
        help="Supported formats: PDF and DOCX. Max size: 10MB.",
        key="resume_upload"
    )

with col2:
    st.markdown("""
    <div class="tips-card">
        <b>💡 Tips for Best Results</b><br><br>
        ✅ Use text-based PDF<br>
        ✅ Include technical skills<br>
        ✅ Add projects with technologies<br>
        ✅ Mention job responsibilities<br>
        ✅ Keep resume ATS-friendly
    </div>
    """, unsafe_allow_html=True)

if uploaded_file is not None:
    resume_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resumes")
    os.makedirs(resume_dir, exist_ok=True)
    file_path = os.path.join(resume_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.markdown(f"""<div class="profile-card"><b>✅ File Uploaded</b><br><br>📄 {uploaded_file.name}<br>📦 {uploaded_file.size // 1024} KB </div>""", unsafe_allow_html=True)
    if st.button("🤖 Analyze Resume with AI", use_container_width=True):
        with st.spinner(""):
            progress = st.progress(0)
            status = st.empty()

            status.markdown("📖 **Step 1/4:** Extracting text from resume...")
            progress.progress(15)
            time.sleep(0.3)

            raw_text = extract_text(file_path)
            if not raw_text.strip():
                st.error("❌ Could not extract text from this file. Please ensure it's not a scanned/image PDF.")
                st.stop()

            status.markdown("🧠 **Step 2/4:** Analyzing with AI (Groq LLaMA3)...")
            progress.progress(40)

            profile = analyze_resume(raw_text)

            status.markdown("🎯 **Step 3/4:** Detecting your domain...")
            progress.progress(70)
            time.sleep(0.3)

            save_profile(profile)

            st.session_state["profile"] = profile
            st.session_state["profile_loaded"] = True

            status.markdown("✅ **Step 4/4:** Profile ready!")
            progress.progress(100)
            time.sleep(0.5)

        progress.empty()
        status.empty()

        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        st.markdown("## ✨ Analysis Complete!")

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric("👤 Name", profile.get("name", "Unknown"))
        with m2:
            st.metric("🎯 Domain", profile.get("domain", "Unknown"))
        with m3:
            st.metric("🛠️ Skills Found", len(profile.get("skills", [])))
        with m4:
            st.metric("📊 Confidence", f"{profile.get('domain_confidence', 0)}%")

        st.markdown("### 🛠️ Extracted Skills")
        skills = profile.get("skills", [])

        if skills:
            badges = " ".join([
                f'<span style="background:#dbeafe;color:#1e40af;padding:4px 10px;border-radius:20px;font-size:13px;margin:3px;display:inline-block">{s}</span>'
                for s in skills[:25]
            ])
            st.markdown(badges, unsafe_allow_html=True)
        else:
            st.warning("No skills detected. Try a more detailed resume.")

        alts = profile.get("domain_alternatives", [])
        if alts:
            
            st.markdown(f"""<div class="profile-card" style="background: orange;">🔄 <b>Alternative roles detected</b>: {', '.join(alts)}</div>""", unsafe_allow_html=True)

        st.markdown(f"""<div class="profile-card">🎉 <b>Next step:</b> Go to <b>Job Matches</b> in the sidebar to find relevant jobs!</div>""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

else:
    existing = get_latest_profile()

    if existing:
        pcol1, pcol2 = st.columns([3.2, 1], gap="medium")

        with pcol1:
            st.markdown(f"""
            <div class="previous-card">
                <h4>📋 Previous Resume Found</h4>
                <p>{existing.get('name', 'Unknown')} • {existing.get('domain', 'Unknown domain')}</p>
            </div>
            """, unsafe_allow_html=True)

        with pcol2:
            st.markdown("<div class='profile-btn-space'></div>", unsafe_allow_html=True)
            if st.button("🚀 Load Profile", use_container_width=True):
                st.session_state["profile"] = existing
                st.session_state["profile_loaded"] = True
                st.success("✅ Previous profile loaded!")

    else:
        st.markdown("""
        <div class="empty-upload">
            <div>📂</div>
            <h3>Upload a resume to get started</h3>
            <p>Supports PDF and DOCX formats</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
render_footer()
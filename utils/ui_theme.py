# import streamlit as st

# def apply_theme():
#     st.markdown("""
    
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

#     html, body, [class*="css"] {
#         font-family: 'Inter', sans-serif;
#     }

#     .stApp {
#         background: #f8fafc;
#     }

# .block-container {
#     padding-top: 0rem !important;
#     padding-left: 1rem !important;
#     padding-right: 1rem !important;
#     padding-bottom: 3rem !important;
#     max-width: 100% !important;
# }

#     div[data-testid="stAppViewContainer"] > .main {
#     padding-top: 0px !important;
# }

# div[data-testid="stVerticalBlock"] {
#     gap: 0rem !important;
# }

# /* Fix Streamlit normal text visibility */
# .stMarkdown h1,
# .stMarkdown h2,
# .stMarkdown h3,
# .stMarkdown h4,
# .stMarkdown p,
# .stMarkdown span,
# .stWrite,
# p, h1, h2, h3 {
#     color: #0f172a !important;
# }

# /* Feature text */
# [data-testid="column"] h3 {
#     color: #0f172a !important;
#     font-size: 28px !important;
#     font-weight: 900 !important;
# }

# [data-testid="column"] p {
#     color: #334155 !important;
#     font-size: 17px !important;
#     font-weight: 500 !important;
# }

# .compact-grid {
#     display: grid;
#     grid-template-columns: repeat(3, 1fr);
#     gap: 16px;
#     margin-top: 18px;
#     margin-bottom: 60px;
# }

# .compact-card {
#     background: white;
#     border-radius: 18px;
#     padding: 16px;
#     display: flex;
#     gap: 14px;
#     align-items: center;
#     border: 1px solid #e2e8f0;
#     box-shadow: 0 8px 24px rgba(15,23,42,0.08);
# }

# .compact-icon {
#     font-size: 30px;
# }

# .compact-card h3 {
#     font-size: 21px !important;
#     margin: 0 0 4px 0 !important;
#     color: #0f172a !important;
# }

# .compact-card p {
#     font-size: 14px !important;
#     margin: 0 !important;
#     color: #475569 !important;
# }

# .feature-grid{
#     display:grid;
#     grid-template-columns:repeat(4,1fr);
#     gap:20px;
#     margin-top:25px;
# }

# .feature-card{
#     background:white;
#     border-radius:22px;
#     padding:25px;
#     text-align:center;
#     border:1px solid #e2e8f0;
#     box-shadow:0 10px 30px rgba(15,23,42,.08);
#     transition:.3s;
# }

# .feature-card:hover{
#     transform:translateY(-8px);
#     box-shadow:0 18px 45px rgba(255,107,0,.20);
# }

# .feature-icon{
#     font-size:48px;
#     margin-bottom:10px;
# }

# .feature-title{
#     font-size:22px;
#     font-weight:800;
#     color:#0f172a;
# }

# .feature-desc{
#     color:#64748b;
#     font-size:14px;
# }

#     #MainMenu, footer, header {
#         visibility: hidden;
#     }

#     section[data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #020617, #172554);
#     }

#     section[data-testid="stSidebar"] * {
#         color: #ffffff !important;
#         font-weight: 700;
#         font-size: 18px !important;
#     }

# /* Reduce sidebar width */
# section[data-testid="stSidebar"] {
#     width: 210px !important;
#     min-width: 210px !important;
#     max-width: 210px !important;
#     background: linear-gradient(180deg, #020617, #172554);
# }

# section[data-testid="stSidebar"] * {
#     font-size: 15px !important;
# }

# .ai-header {
#     position: fixed;
#     top: 0;
#     left: 210px;
#     right: 0;
#     z-index: 9999;
#     background: linear-gradient(90deg, #050505, #111827);
#     border-radius: 0;
#     padding: 12px 32px;
#     min-height: 76px;
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     box-shadow: 0 14px 35px rgba(0,0,0,0.28);
# }

#     .brand {
#         display: flex;
#         align-items: center;
#         gap: 16px;
#     }

#    .brand-icon {
#     width: 58px;
#     height: 58px;
#     border: 4px solid #ff6b00;
#     color: #ff6b00 !important;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     font-weight: 900;
#     font-size: 34px;
# }

#    .brand-text {
#     font-size: 38px;
#     font-weight: 900;
#     color: #ffffff !important;
# }

#     .brand-text span {
#         color: #ff6b00 !important;
#     }

#     .nav-items {
#         display: flex;
#         align-items: center;
#         gap: 12px;
#     }

#     .nav-items span {
#     color: #ffffff !important;
#     font-size: 15px;
#     font-weight: 700;
#     padding: 12px 24px;
#     border-radius: 999px;
#     background: linear-gradient(135deg, #1f2937, #374151);
#     box-shadow: inset 0 1px 0 rgba(255,255,255,.12);
#     transition: all .25s ease;
# }

# .nav-items span:hover {
#     background: linear-gradient(135deg, #ff6b00, #f97316);
#     transform: translateY(-3px);
# }

# .page-wrap {
#     padding: 32px 28px 70px 28px;
# }
#     .hero-title {
#         font-size: 58px;
#         font-weight: 900;
#         color: #0f172a !important;
#         margin: 0;
#     }
# #     .timeline-box h2 {
# #     color: #0f172a !important;
# # }

# # .timeline-box {
# #     color: #0f172a !important;
# # }

#     .hero-subtitle {
#         font-size: 20px;
#         color: #334155 !important;
#         margin-top: 10px;
#         font-weight: 600;
#     }

#     .feature-card {
#         background: #ffffff;
#         border-radius: 24px;
#         padding: 28px;
#         min-height: 190px;
#         border: 1px solid #e2e8f0;
#         box-shadow: 0 12px 32px rgba(15,23,42,0.10);
#         transition: .3s ease;
#     }

#     .feature-card:hover {
#         transform: translateY(-7px);
#         box-shadow: 0 20px 45px rgba(15,23,42,0.16);
#     }

#     .feature-card h3 {
#         color: #0f172a !important;
#         font-size: 30px;
#         margin-bottom: 14px;
#     }

#     .feature-card p {
#         color: #334155 !important;
#         font-size: 18px;
#         line-height: 1.6;
#         font-weight: 500;
#     }

# .ai-footer {
#     position: fixed !important;
#     bottom: 0 !important;
#     left: 210px !important;
#     right: 0 !important;
#     height: 42px !important;
#     background: #050505 !important;
#     color: #ffffff !important;
#     display: flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     font-size: 14px !important;
#     font-weight: 800 !important;
#     z-index: 99999999 !important;
# }

# .page-wrap{
#     padding-bottom:70px;
# }
#     .stButton > button {
#     background: linear-gradient(135deg, #ff6b00, #f97316) !important;
#     color: white !important;
#     border: none !important;
#     border-radius: 14px !important;
#     padding: 12px 22px !important;
#     font-size: 16px !important;
#     font-weight: 800 !important;
#     box-shadow: 0 10px 25px rgba(249,115,22,0.35);
#     transition: all .25s ease;
# }

# .stButton > button:hover {
#     transform: translateY(-3px);
#     box-shadow: 0 16px 35px rgba(249,115,22,0.45);
# }

# [data-testid="stFileUploader"] {
#     background: #ffffff !important;
#     border: 2px dashed #fb923c !important;
#     border-radius: 20px !important;
#     padding: 16px !important;
#     box-shadow: 0 10px 25px rgba(15,23,42,0.08) !important;
#     margin-bottom: 14px !important;
# }

# [data-testid="stFileUploader"] section {
#     background: #111827 !important;
#     border-radius: 14px !important;
#     padding: 12px !important;
# }

# [data-testid="stFileUploader"] * {
#     color: #ffffff !important;
# }

# [data-testid="stFileUploader"] label {
#     color: #0f172a !important;
#     font-weight: 700 !important;
# }

# .hero-section {
#     display: grid;
#     grid-template-columns: 1.8fr 1fr;
#     gap: 28px;
#     background: linear-gradient(135deg, #ffffff, #f1f5f9);
#     border-radius: 28px;
#     padding: 20px;
#     gap: 20px;
#     box-shadow: 0 18px 45px rgba(15,23,42,0.12);
#     border: 1px solid #e2e8f0;
#     animation: fadeUp .7s ease;
#     margin-left: 15px !important;
#     margin-right: 15px !important;
#     margin-top: 10px !important;

# }

# .hero-section,
# .stats-grid,
# .feature-grid,
# .timeline-box {
#     margin-left: 15px;
#     margin-right: 15px;
# }

# .eyebrow {
#     color: #ff6b00 !important;
#     font-weight: 900;
#     letter-spacing: 1px;
#     font-size: 14px;
# }

# .hero-section h1 {
#     font-size: 42px;
#     font-weight: 900;
#     color: #0f172a !important;
#     margin: 8px 0;
# }

# .hero-section p {
#     font-size: 19px;
#     color: #334155 !important;
#     line-height: 1.6;
# }

# .hero-actions {
#     display: flex;
#     gap: 14px;
#     margin-top: 22px;
#     flex-wrap: wrap;
# }

# .hero-actions span {
#     background: #111827;
#     color: white !important;
#     padding: 11px 18px;
#     border-radius: 999px;
#     font-weight: 800;
# }



# .circle-score {
#     width: 110px;
#     height: 110px;
#     font-size: 32px;
#     margin: auto;
#     border-radius: 50%;
#     border: 12px solid #ff6b00;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     font-weight: 900;
#     color: white !important;
# }

# # .hero-visual p, .hero-visual small {
# #     color: white !important;
# # }


# .hero-visual {
#     background: linear-gradient(135deg, #111827, #020617);
#     border-radius: 22px;
#     padding: 28px;
#     text-align: center;
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
# }

# .hero-visual p {
#     color: #ffffff !important;
#     font-size: 22px !important;
#     font-weight: 800 !important;
#     margin: 16px 0 6px 0 !important;
#     text-align: center !important;
# }

# .hero-visual small {
#     color: #cbd5e1 !important;
#     font-size: 15px !important;
#     font-weight: 600 !important;
#     text-align: center !important;
# }

# .circle-score {
#     width: 120px;
#     height: 120px;
#     border-radius: 50%;
#     border: 12px solid #ff6b00;
#     color: white !important;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     font-size: 34px;
#     font-weight: 900;
# }

# .stats-grid {
#     display: grid;
#     grid-template-columns: repeat(4, 1fr);
#     gap: 18px;
#     margin: 24px 0;
# }

# .stat-card {
#     background: white;
#     border-radius: 22px;
#     padding: 12px;
#     text-align: center;
#     box-shadow: 0 12px 30px rgba(15,23,42,0.09);
#     border: 1px solid #e2e8f0;
# }

# .stat-card h2 {
#     font-size: 28px;
#     color: #ff6b00 !important;
#     margin: 0;
# }

# .stat-card p {
#     font-weight: 800;
#     color: #334155 !important;
# }

# .feature-grid {
#     display: grid;
#     grid-template-columns: repeat(3, 1fr);
#     gap: 22px;
# }

# .timeline-box {
#     background: white;
#     margin-top: 26px;
#     border-radius: 24px;
#     padding: 26px;
#     box-shadow: 0 14px 35px rgba(15,23,42,0.10);
# }

# .timeline {
#     display: grid;
#     grid-template-columns: repeat(6, 1fr);
#     gap: 14px;
# }

# .timeline div {
#     background: #fff7ed;
#     border: 1px solid #fed7aa;
#     border-radius: 18px;
#     padding: 18px;
#     text-align: center;
# }

# .timeline b {
#     background: #ff6b00;
#     color: white !important;
#     padding: 8px 13px;
#     border-radius: 50%;
#     display: inline-block;
#     margin-bottom: 10px;
# }

# .timeline span {
#     display: block;
#     font-weight: 800;
#     color: #0f172a !important;
# }

# /* Upload Page */

# .upload-hero {
#     background: linear-gradient(135deg, #ffffff, #fff7ed);
#     border-radius: 20px;
#     padding: 14px 22px;
#     margin-bottom: 14px;
#     border: 1px solid #fed7aa;
#     box-shadow: 0 8px 22px rgba(15,23,42,0.08);
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
# }

# .upload-hero h1 {
#     color: #0f172a !important;
#     font-size: 32px !important;
#     margin: 0 !important;
# }

# .upload-hero p {
#     color: #475569 !important;
#     font-size: 14px !important;
#     margin-top: 5px !important;
# }

# .upload-badge {
#     background: #111827;
#     color: white !important;
#     padding: 10px 16px;
#     border-radius: 999px;
#     font-weight: 800;
#     font-size: 13px;
# }

# .tips-card {
#     background: #ffffff;
#     border: 1px solid #fed7aa;
#     border-radius: 18px;
#     padding: 18px;
#     box-shadow: 0 8px 24px rgba(15,23,42,0.08);
#     min-height: 150px;
# }

# .tips-card b {
#     color: #ff6b00 !important;
#     font-size: 17px;
# }

# .tips-card,
# .tips-card * {
#     color: #0f172a !important;
#     line-height: 1.75;
# }

# [data-testid="stFileUploader"] {
#     background: #ffffff !important;
#     border: 2px dashed #fb923c !important;
#     border-radius: 20px !important;
#     padding: 16px !important;
#     box-shadow: 0 10px 25px rgba(15,23,42,0.08) !important;
#     margin-bottom: 14px !important;
# }

# [data-testid="stFileUploader"] section {
#     background: #111827 !important;
#     border-radius: 14px !important;
#     padding: 12px !important;
# }

# [data-testid="stFileUploader"] section * {
#     color: #ffffff !important;
# }

# [data-testid="stFileUploader"] label {
#     color: #0f172a !important;
#     font-weight: 700 !important;
# }

# .previous-card {
#     background: #ffffff;
#     border-left: 5px solid #ff6b00;
#     border-radius: 16px;
#     padding: 16px 18px;
#     margin-top: 16px;
#     box-shadow: 0 8px 22px rgba(15,23,42,0.08);
# }

# .previous-card h4 {
#     color: #0f172a !important;
#     margin: 0 0 6px 0 !important;
#     font-size: 18px !important;
# }

# .previous-card p {
#     color: #475569 !important;
#     margin: 0 !important;
#     font-size: 15px !important;
# }

# .profile-btn-space {
#     height: 28px;
# }

# [data-testid="stMetric"] {
#     background: white !important;
#     border-radius: 16px !important;
#     padding: 14px !important;
#     box-shadow: 0 8px 20px rgba(15,23,42,0.08) !important;
# }

# .result-section {
#     margin-top: 18px;
#     padding-bottom: 55px;
# }

# .empty-upload {
#     text-align: center;
#     padding: 38px;
#     color: #64748b !important;
# }

# .empty-upload div {
#     font-size: 56px;
# }

# .empty-upload h3 {
#     color: #0f172a !important;
#     font-size: 22px;
#     margin: 8px 0;
# }

# .empty-upload p {
#     color: #64748b !important;
# }



# /* Profile Page */

# .profile-hero {
#     background: linear-gradient(135deg, #ffffff, #eef2ff);
#     border-radius: 22px;
#     padding: 18px 24px;
#     margin-bottom: 16px;
#     border: 1px solid #c7d2fe;
#     box-shadow: 0 8px 22px rgba(15,23,42,0.08);
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
# }

# .profile-hero h1 {
#     color: #0f172a !important;
#     font-size: 34px !important;
#     margin: 0 !important;
# }

# .profile-hero p {
#     color: #475569 !important;
#     font-size: 14px !important;
#     margin-top: 6px !important;
# }

# .profile-domain {
#     background: #111827;
#     color: white !important;
#     padding: 12px 18px;
#     border-radius: 18px;
#     text-align: center;
# }

# .profile-domain span {
#     display: block;
#     color: white !important;
#     font-weight: 900;
# }

# .profile-domain b {
#     color: #fb923c !important;
#     font-size: 13px;
# }

# .profile-card {
#     background: white;
#     border-radius: 20px;
#     padding: 20px;
#     margin-top: 16px;
#     border: 1px solid #e2e8f0;
#     box-shadow: 0 8px 24px rgba(15,23,42,0.08);

# }

# .profile-card h2 {
#     color: #0f172a !important;
#     font-size: 22px !important;
#     margin: 0 0 12px 0 !important;
# }

# .profile-card p {
#     color: #475569 !important;
#     font-size: 15px !important;
# }

# .domain-circle {
#     text-align: center;
#     background: #f8fafc;
#     border-radius: 18px;
#     padding: 20px;
# }

# .domain-circle div {
#     font-size: 34px;
# }

# .domain-circle h3 {
#     font-size: 24px !important;
#     margin: 8px 0 2px 0 !important;
#     font-weight: 900 !important;
# }

# .domain-circle h2 {
#     font-size: 32px !important;
#     margin: 10px 0 0 0 !important;
# }

# .domain-circle p,
# .domain-circle small {
#     color: #64748b !important;
# }

# .method-grid {
#     display: grid;
#     grid-template-columns: repeat(2, 1fr);
#     gap: 10px;
#     margin-top: 12px;
# }

# .method-grid span {
#     background: #fff7ed;
#     color: #9a3412 !important;
#     padding: 10px 12px;
#     border-radius: 14px;
#     font-weight: 800;
#     text-align: center;
# }

# .skill-badge {
#     background: #dbeafe;
#     color: #1e40af !important;
#     padding: 6px 12px;
#     border-radius: 999px;
#     font-size: 13px;
#     margin: 4px;
#     display: inline-block;
#     font-weight: 700;
# }

# .mini-section {
#     background: #f8fafc;
#     border-left: 4px solid #ff6b00;
#     border-radius: 14px;
#     padding: 12px 14px;
#     margin: 10px 0;
#     color: #334155 !important;
#     font-size: 14px;
#     line-height: 1.6;
# }

# .summary-text {
#     font-style: italic;
#     line-height: 1.7;
#     color: #334155 !important;
# }

# .small-card {
#     margin-top: 12px;
# }
#     </style>
#     """, unsafe_allow_html=True)


# def render_header():
#     st.markdown("""
#     <div class="ai-header">
#         <div class="brand">
#             <div class="brand-icon">Y</div>
#             <div class="brand-text">AI<span>Youth</span></div>
#         </div>
#         <div class="nav-items">
#             <span>Resume</span>
#             <span>Jobs</span>
#             <span>ATS</span>
#             <span>Tracker</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# def render_footer():
#     st.markdown("""
#     <div class="ai-footer">
#         © 2026 AIYouth.ai · aiyouth.ai
#     </div>
#     """, unsafe_allow_html=True)

import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --sidebar-width: 210px;
        --header-height: 78px;
        --footer-height: 42px;
        --orange: #ff6b00;
        --orange-2: #f97316;
        --dark: #050505;
        --navy: #111827;
        --text: #0f172a;
        --muted: #475569;
        --border: #e2e8f0;
        --soft: #f8fafc;
    }

    * {
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
    }

    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        color: var(--text);
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    div[data-testid="stAppViewContainer"] > .main {
        padding-top: 0 !important;
    }

    div[data-testid="stVerticalBlock"] {
        gap: 0.85rem !important;
    }

    section[data-testid="stSidebar"] {
        width: var(--sidebar-width) !important;
        min-width: var(--sidebar-width) !important;
        max-width: var(--sidebar-width) !important;
        background: linear-gradient(180deg, #020617 0%, #0f172a 55%, #172554 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
        font-size: 15px !important;
        font-weight: 750 !important;
    }

    .ai-header {
        position: fixed;
        top: 0;
        left: var(--sidebar-width);
        right: 0;
        height: var(--header-height);
        z-index: 99999;
        background: linear-gradient(90deg, #050505, #111827);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 30px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.28);
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 14px;
        min-width: 0;
    }

    .brand-icon {
        width: 52px;
        height: 52px;
        border: 4px solid var(--orange);
        color: var(--orange) !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        font-weight: 900;
        flex: 0 0 auto;
    }

    .brand-text {
        font-size: 34px;
        font-weight: 900;
        color: #ffffff !important;
        white-space: nowrap;
    }

    .brand-text span {
        color: var(--orange) !important;
    }

    .nav-items {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: nowrap;
    }

    .nav-items span {
        color: #ffffff !important;
        background: linear-gradient(135deg, #1f2937, #374151);
        padding: 10px 20px;
        border-radius: 999px;
        font-size: 14px;
        font-weight: 800;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.12);
        transition: 0.25s ease;
        white-space: nowrap;
    }

    .nav-items span:hover {
        background: linear-gradient(135deg, var(--orange), var(--orange-2));
        transform: translateY(-2px);
    }

    .page-wrap {
        padding: calc(var(--header-height) + 18px) 24px calc(var(--footer-height) + 28px) 24px !important;
        width: 100%;
        overflow-x: hidden;
    }

    .ai-footer {
        position: fixed !important;
        bottom: 0 !important;
        left: var(--sidebar-width) !important;
        right: 0 !important;
        height: var(--footer-height) !important;
        background: #050505 !important;
        color: #ffffff !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 14px !important;
        font-weight: 800 !important;
        z-index: 99999999 !important;
        border-top: 1px solid rgba(255,255,255,0.12);
    }

    .stButton > button {
        background: linear-gradient(135deg, var(--orange), var(--orange-2)) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 11px 20px !important;
        font-size: 15px !important;
        font-weight: 800 !important;
        box-shadow: 0 10px 25px rgba(249,115,22,0.28);
        transition: all .25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 35px rgba(249,115,22,0.38);
    }

    [data-testid="stMetric"] {
        background: #ffffff !important;
        border-radius: 18px !important;
        padding: 14px !important;
        border: 1px solid var(--border) !important;
        box-shadow: 0 8px 20px rgba(15,23,42,0.08) !important;
        min-height: 98px;
    }

    [data-testid="stMetric"] * {
        color: var(--text) !important;
    }

    .stAlert {
        border-radius: 16px !important;
    }

    /* Home Page */
    .hero-section {
        display: grid;
        grid-template-columns: minmax(0, 1.7fr) minmax(280px, 0.8fr);
        gap: 20px;
        background: linear-gradient(135deg, #ffffff, #f1f5f9);
        border-radius: 26px;
        padding: 22px;
        box-shadow: 0 18px 45px rgba(15,23,42,0.10);
        border: 1px solid var(--border);
        animation: fadeUp .55s ease;
    }

    .eyebrow {
        color: var(--orange) !important;
        font-weight: 900;
        letter-spacing: 1px;
        font-size: 14px;
    }

    .hero-section h1 {
        font-size: clamp(32px, 3vw, 46px);
        font-weight: 900;
        color: var(--text) !important;
        margin: 8px 0;
        line-height: 1.1;
    }

    .hero-section p {
        font-size: 17px;
        color: var(--muted) !important;
        line-height: 1.55;
    }

    .hero-actions {
        display: flex;
        gap: 12px;
        margin-top: 18px;
        flex-wrap: wrap;
    }

    .hero-actions span {
        background: var(--navy);
        color: #ffffff !important;
        padding: 10px 16px;
        border-radius: 999px;
        font-weight: 800;
        font-size: 14px;
    }

    .hero-visual {
        background: linear-gradient(135deg, #111827, #020617);
        border-radius: 22px;
        padding: 24px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .hero-visual, .hero-visual * {
        color: #ffffff !important;
    }

    .circle-score {
        width: 116px;
        height: 116px;
        border-radius: 50%;
        border: 12px solid var(--orange);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 34px;
        font-weight: 900;
    }

    .hero-visual p {
        font-size: 20px !important;
        font-weight: 850 !important;
        margin: 14px 0 4px 0 !important;
        color: #ffffff !important;
    }

    .hero-visual small {
        color: #cbd5e1 !important;
        font-size: 14px !important;
        font-weight: 600 !important;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0,1fr));
        gap: 18px;
        margin-top: 18px;
    }

    .feature-card {
        background: #ffffff;
        border-radius: 22px;
        padding: 22px 18px;
        text-align: center;
        border: 1px solid var(--border);
        box-shadow: 0 10px 28px rgba(15,23,42,.08);
        transition: .25s ease;
        min-height: 160px;
    }

    .feature-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 18px 40px rgba(255,107,0,.16);
        border-color: #fed7aa;
    }

    .feature-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }

    .feature-title {
        font-size: 20px;
        font-weight: 900;
        color: var(--text) !important;
    }

    .feature-desc {
        color: #64748b !important;
        font-size: 14px;
        margin-top: 6px;
        line-height: 1.45;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0,1fr));
        gap: 16px;
        margin: 18px 0;
    }

    .stat-card {
        background: white;
        border-radius: 20px;
        padding: 14px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(15,23,42,0.08);
        border: 1px solid var(--border);
    }

    .stat-card h2 {
        font-size: 28px;
        color: var(--orange) !important;
        margin: 0;
    }

    .stat-card p {
        font-weight: 800;
        color: #334155 !important;
        margin: 4px 0 0;
    }

    /* Upload Page */
    .upload-hero, .profile-hero, .jobs-hero, .optimizer-hero {
        background: linear-gradient(135deg, #ffffff, #fff7ed);
        border-radius: 20px;
        padding: 16px 22px;
        margin-bottom: 16px;
        border: 1px solid #fed7aa;
        box-shadow: 0 8px 22px rgba(15,23,42,0.08);
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
    }

    .profile-hero {
        background: linear-gradient(135deg, #ffffff, #eef2ff);
        border-color: #c7d2fe;
    }

    .jobs-hero {
        background: linear-gradient(135deg, #ffffff, #ecfeff);
        border-color: #a5f3fc;
    }

    .optimizer-hero {
        background: linear-gradient(135deg, #ffffff, #f5f3ff);
        border-color: #ddd6fe;
    }

    .upload-hero h1, .profile-hero h1, .jobs-hero h1, .optimizer-hero h1 {
        color: var(--text) !important;
        font-size: clamp(26px, 2.4vw, 34px) !important;
        margin: 0 !important;
        line-height: 1.15;
    }

    .upload-hero p, .profile-hero p, .jobs-hero p, .optimizer-hero p {
        color: var(--muted) !important;
        font-size: 14px !important;
        margin: 6px 0 0 !important;
    }

    .upload-badge, .profile-domain, .page-badge {
        background: var(--navy);
        color: #ffffff !important;
        padding: 10px 16px;
        border-radius: 999px;
        font-weight: 850;
        font-size: 13px;
        text-align: center;
        white-space: nowrap;
    }

    .upload-badge *, .profile-domain *, .page-badge * {
        color: #ffffff !important;
    }

    .profile-domain {
        border-radius: 18px;
        min-width: 180px;
    }

    .profile-domain span {
        display: block;
        font-weight: 900;
    }

    .profile-domain b {
        color: #fb923c !important;
        font-size: 13px;
    }

    .tips-card {
        background: #ffffff;
        border: 1px solid #fed7aa;
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 8px 24px rgba(15,23,42,0.08);
        min-height: 150px;
    }

    .tips-card b {
        color: var(--orange) !important;
        font-size: 17px;
    }

    .tips-card, .tips-card * {
        color: var(--text) !important;
        line-height: 1.75;
    }

    [data-testid="stFileUploader"] {
        background: #ffffff !important;
        border: 2px dashed #fb923c !important;
        border-radius: 20px !important;
        padding: 16px !important;
        box-shadow: 0 10px 25px rgba(15,23,42,0.08) !important;
        margin-bottom: 14px !important;
    }

    [data-testid="stFileUploader"] section {
        background: var(--navy) !important;
        border-radius: 14px !important;
        padding: 12px !important;
    }

    [data-testid="stFileUploader"] section * {
        color: #ffffff !important;
    }

    [data-testid="stFileUploader"] label {
        color: var(--text) !important;
        font-weight: 800 !important;
    }

    .previous-card {
        background: #ffffff;
        border-left: 5px solid var(--orange);
        border-radius: 16px;
        padding: 16px 18px;
        margin-top: 16px;
        box-shadow: 0 8px 22px rgba(15,23,42,0.08);
    }

    .previous-card h4 {
        color: var(--text) !important;
        margin: 0 0 6px 0 !important;
        font-size: 18px !important;
    }

    .previous-card p {
        color: var(--muted) !important;
        margin: 0 !important;
        font-size: 15px !important;
    }

    .profile-btn-space {
        height: 28px;
    }

    .result-section {
        margin-top: 18px;
        padding-bottom: 20px;
    }

    .empty-upload {
        text-align: center;
        padding: 42px;
        color: #64748b !important;
        background: #ffffff;
        border-radius: 22px;
        border: 1px solid var(--border);
        box-shadow: 0 8px 22px rgba(15,23,42,0.08);
    }

    .empty-upload div {
        font-size: 56px;
    }

    .empty-upload h3 {
        color: var(--text) !important;
        font-size: 22px;
        margin: 8px 0;
    }

    .empty-upload p {
        color: #64748b !important;
    }

    /* Profile Page */
    .profile-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin-top: 16px;
        margin-bottom: 6px;
        border: 1px solid var(--border);
        box-shadow: 0 8px 24px rgba(15,23,42,0.08);
        overflow-wrap: anywhere;
    }

    .profile-card h2 {
        color: var(--text) !important;
        font-size: 22px !important;
        margin: 0 0 12px 0 !important;
    }

    .profile-card p {
        color: var(--muted) !important;
        font-size: 15px !important;
    }

    .domain-circle {
        text-align: center;
        background: #f8fafc;
        border-radius: 18px;
        padding: 20px;
        border: 1px solid var(--border);
    }

    .domain-circle div {
        font-size: 34px;
    }

    .domain-circle h3 {
        font-size: 24px !important;
        margin: 8px 0 2px 0 !important;
        font-weight: 900 !important;
    }

    .domain-circle h2 {
        font-size: 32px !important;
        margin: 10px 0 0 0 !important;
    }

    .domain-circle p, .domain-circle small {
        color: #64748b !important;
    }

    .method-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0,1fr));
        gap: 10px;
        margin-top: 12px;
    }

    .method-grid span {
        background: #fff7ed;
        color: #9a3412 !important;
        padding: 10px 12px;
        border-radius: 14px;
        font-weight: 800;
        text-align: center;
    }

    .skill-badge, .skill-tag, .match-tag, .missing-tag, .keyword-badge {
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 13px;
        margin: 4px;
        display: inline-block;
        font-weight: 750;
    }

    .skill-badge, .match-tag {
        background: #dbeafe;
        color: #1e40af !important;
    }

    .skill-tag {
        background:#f1f5f9;
        color:#475569 !important;
    }

    .missing-tag {
        background:#fee2e2;
        color:#991b1b !important;
    }

    .keyword-badge {
        background:#dcfce7;
        color:#166534 !important;
    }

    .mini-section {
        background: #f8fafc;
        border-left: 4px solid var(--orange);
        border-radius: 14px;
        padding: 12px 14px;
        margin: 10px 0;
        color: #334155 !important;
        font-size: 14px;
        line-height: 1.6;
        overflow-wrap: anywhere;
    }

    .summary-text {
        font-style: italic;
        line-height: 1.7;
        color: #334155 !important;
    }

    .small-card {
        margin-top: 12px;
    }

    /* Jobs Page */
    .job-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 18px;
        margin: 12px 0;
        box-shadow: 0 8px 24px rgba(15,23,42,0.08);
        border-left: 5px solid var(--orange);
        overflow-wrap: anywhere;
    }

    /* Optimizer Page */
    .resume-section {
        background: #ffffff;
        border-radius: 18px;
        padding: 18px;
        margin: 12px 0;
        border: 1px solid var(--border);
        box-shadow: 0 8px 24px rgba(15,23,42,0.08);
        overflow-wrap: anywhere;
    }

    .resume-section h3 {
        color: #1e40af !important;
        border-bottom: 2px solid #bfdbfe;
        padding-bottom: 8px;
        margin-top: 0;
    }

    .resume-section p, .resume-section li {
        color: #374151 !important;
        line-height: 1.65;
    }

    /* Responsive */
    @media (max-width: 1200px) {
        .feature-grid, .stats-grid {
            grid-template-columns: repeat(2, minmax(0,1fr));
        }

        .hero-section {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 900px) {
        .ai-header {
            left: 0;
            padding: 0 16px;
            height: 72px;
        }

        .brand-icon {
            width: 44px;
            height: 44px;
            font-size: 24px;
        }

        .brand-text {
            font-size: 26px;
        }

        .nav-items {
            display: none;
        }

        .ai-footer {
            left: 0 !important;
        }

        .page-wrap {
            padding: 86px 14px 70px 14px !important;
        }

        .upload-hero, .profile-hero, .jobs-hero, .optimizer-hero {
            flex-direction: column;
            align-items: flex-start;
        }

        .profile-domain, .upload-badge, .page-badge {
            width: 100%;
        }

        .method-grid {
            grid-template-columns: 1fr;
        }

        .feature-grid, .stats-grid {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 640px) {
        .page-wrap {
            padding-left: 10px !important;
            padding-right: 10px !important;
        }

        .hero-section, .profile-card, .resume-section, .job-card {
            border-radius: 16px;
            padding: 16px;
        }

        .hero-actions span {
            width: 100%;
            text-align: center;
        }
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    st.markdown("""
    <div class="ai-header">
        <div class="brand">
            <div class="brand-icon">Y</div>
            <div class="brand-text">AI<span>Youth</span></div>
        </div>
        <div class="nav-items">
            <span>Resume</span>
            <span>Jobs</span>
            <span>ATS</span>
            <span>Tracker</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="ai-footer">
        © 2026 AIYouth.ai · aiyouth.ai
    </div>
    """, unsafe_allow_html=True) 

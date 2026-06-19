"""
pages/6_Tracker.py
------------------
Page 6: Application Tracker

Track all job applications with:
- Company, role, status, match score, apply URL, notes
- Status management (Saved → Applied → Interview → Offer/Rejected)
- Summary statistics
- Export as CSV

Uses SQLite via utils/database.py
"""

import streamlit as st
import pandas as pd
import os, sys
from datetime import datetime

# ✅ Must be the first Streamlit call
st.set_page_config(page_title="Application Tracker", page_icon="📊", layout="wide")

# Import custom utils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.ui_theme import apply_theme, render_header, render_footer
from utils.database import get_applications, update_application_status, delete_application, add_application

# Apply theme and header AFTER page config
apply_theme()
render_header()

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stButton > button {
    border-radius: 8px; font-weight: 600;
}
.status-pill {
    padding: 3px 12px; border-radius: 20px; font-size: 12px;
    font-weight: 600; display: inline-block;
}
#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

STATUS_OPTIONS = ["Saved", "Applied", "Interview", "Offer", "Rejected"]

STATUS_COLORS = {
    "Saved":     ("#dbeafe", "#1e40af"),
    "Applied":   ("#fef9c3", "#854d0e"),
    "Interview": ("#dcfce7", "#166534"),
    "Offer":     ("#f0fdf4", "#14532d"),
    "Rejected":  ("#fee2e2", "#991b1b"),
}

# ─── Header ──────────────────────────────────────────────────────────────────
st.markdown("# 📊 Application Tracker")
st.markdown("Track your job applications from saved → offer.")
st.markdown("---")

# ─── Add Manual Application ───────────────────────────────────────────────────
with st.expander("➕ Add Manual Application"):
    col1, col2, col3 = st.columns(3)
    with col1:
        m_company = st.text_input("Company Name")
        m_role = st.text_input("Role Title")
    with col2:
        m_status = st.selectbox("Status", STATUS_OPTIONS)
        m_score = st.number_input("Match Score %", min_value=0, max_value=100, value=0)
    with col3:
        m_url = st.text_input("Apply URL (optional)")
        m_notes = st.text_area("Notes", height=80)

    if st.button("➕ Add Application", use_container_width=True):
        if m_company and m_role:
            add_application({
                "company": m_company,
                "role": m_role,
                "status": m_status,
                "match_score": m_score,
                "apply_url": m_url,
                "notes": m_notes
            })
            st.success(f"✅ Added: {m_role} at {m_company}")
            st.rerun()
        else:
            st.warning("Please fill in at least Company and Role.")

st.markdown("---")

# ─── Load Applications ────────────────────────────────────────────────────────
applications = get_applications()

# ─── Summary Stats ────────────────────────────────────────────────────────────
if applications:
    status_counts = {}
    for app in applications:
        s = app.get("status", "Saved")
        status_counts[s] = status_counts.get(s, 0) + 1

    total = len(applications)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1: st.metric("📋 Total", total)
    with col2: st.metric("💾 Saved", status_counts.get("Saved", 0))
    with col3: st.metric("📤 Applied", status_counts.get("Applied", 0))
    with col4: st.metric("🎙️ Interview", status_counts.get("Interview", 0))
    with col5: st.metric("🎉 Offers", status_counts.get("Offer", 0))
    with col6: st.metric("❌ Rejected", status_counts.get("Rejected", 0))

    # Pipeline visualization
    st.markdown("### 📈 Application Pipeline")
    pipeline_data = {
        "Stage": STATUS_OPTIONS,
        "Count": [status_counts.get(s, 0) for s in STATUS_OPTIONS]
    }
    st.bar_chart(pd.DataFrame(pipeline_data).set_index("Stage"))

    st.markdown("---")

    # ─── Filter Controls ──────────────────────────────────────────────────────
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        filter_status = st.multiselect("Filter by Status:", STATUS_OPTIONS, default=STATUS_OPTIONS)
    with col_f2:
        sort_by = st.selectbox("Sort by:", ["Date (Newest)", "Match Score", "Company"])

    filtered = [a for a in applications if a.get("status") in filter_status]
    if sort_by == "Match Score":
        filtered = sorted(filtered, key=lambda x: x.get("match_score", 0), reverse=True)
    elif sort_by == "Company":
        filtered = sorted(filtered, key=lambda x: x.get("company", "").lower())

    st.markdown(f"### Showing {len(filtered)} of {total} applications")
    st.markdown("---")

    # ─── Application Cards ────────────────────────────────────────────────────
    for app in filtered:
        status = app.get("status", "Saved")
        bg, fg = STATUS_COLORS.get(status, ("#f1f5f9", "#475569"))
        score = app.get("match_score", 0)

        col_a, col_b = st.columns([4, 1])
        with col_a:
            st.markdown(f"""
            <div style="background:white;border-radius:12px;padding:16px;margin:6px 0;
                        box-shadow:0 1px 3px rgba(0,0,0,0.08);border-left:4px solid {fg}">
                <div style="display:flex;justify-content:space-between;align-items:center">
                    <div>
                        <div style="font-size:16px;font-weight:700;color:#0f172a">{app.get('role','')}</div>
                        <div style="font-size:13px;color:#64748b;margin-top:2px">
                            🏢 {app.get('company','')} &nbsp;|&nbsp; 📅 {app.get('applied_date','')}
                        </div>
                    </div>
                    <div style="text-align:right">
                        <span style="background:{bg};color:{fg};padding:4px 14px;border-radius:20px;font-weight:600;font-size:13px">{status}</span>
                        <div style="font-size:12px;color:#94a3b8;margin-top:4px">Match: {score:.0f}%</div>
                    </div>
                </div>
                {f'<div style="font-size:12px;color:#64748b;margin-top:8px">📝 {app.get("notes","")}</div>' if app.get("notes") else ""}
            </div>
            """, unsafe_allow_html=True)

        with col_b:
            new_status = st.selectbox("Update status", STATUS_OPTIONS,
                                      index=STATUS_OPTIONS.index(status),
                                      key=f"status_{app['id']}",
                                      label_visibility="collapsed")
            if new_status != status:
                update_application_status(app["id"], new_status)
                st.rerun()

            if app.get("apply_url"):
                st.link_button("🔗 Apply", app["apply_url"], use_container_width=True)

            if st.button("🗑️ Remove", key=f"del_{app['id']}", use_container_width=True):
                delete_application(app["id"])
                st.toast("Application removed.")
                st.rerun()

    st.markdown("---")

    # ─── CSV Export ───────────────────────────────────────────────────────────
    df = pd.DataFrame(applications)
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Export All as CSV",
        data=csv,
        file_name=f"applications_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

else:
    st.markdown("""
    <div style="text-align:center;padding:80px;color:#94a3b8">
        <div style="font-size:64px">📋</div>
        <div style="font-size:20px;margin-top:16px;font-weight:600">No applications tracked yet</div>
        <div style="font-size:14px;margin-top:8px">
            Save jobs from the <b>Job Matches</b> page
        </div>
    </div>
    """, unsafe_allow_html=True)
render_footer()
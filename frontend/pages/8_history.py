# frontend/pages/8_history.py


import streamlit as st
import requests
import os
from components.sidebar import sidebar
from datetime import datetime

from config import BACKEND_URL

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Prediction History | CanBridge",
    page_icon="📜",
    layout="wide"
)

# ---------------- SESSION GUARD ----------------
if not st.session_state.get("logged_in"):
    st.switch_page("main.py")
 

# -------------------------------
# LOAD EXTERNAL CSS (if exists)
# -------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
css_path = os.path.join(app_dir, "styles", "style.css")

if os.path.exists(css_path):
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# HIDE DEFAULT STREAMLIT SIDEBAR NAV
# -------------------------------
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# SIDEBAR
# -------------------------------
sidebar()

# -------------------------------
# HEADER
# -------------------------------
st.write("")
st.write("")

st.markdown(
    """
    <h1 style='text-align:center; color:white; margin-top: 20px;'>
    📜 Prediction History
    </h1>
    <p style='text-align:center; color:#ffeaea; font-size:18px; margin-top:-10px;'>
    View your past AI-assisted cancer predictions.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# -------------------------------
# FETCH HISTORY FROM BACKEND
# -------------------------------
history_url = f"{BACKEND_URL}/history"

try:
    response = requests.get(history_url, timeout=5)
    response.raise_for_status()
    history_data = response.json()
except Exception as e:
    st.error("⚠️ Unable to fetch history from backend.")
    st.stop()

# -------------------------------
# DISPLAY HISTORY
# -------------------------------
if not history_data:
    st.info("No prediction history available yet.")
    st.stop()

# Sort by most recent first (extra safety)
history_data = sorted(
    history_data,
    key=lambda x: x["created_at"],
    reverse=True
)

for record in history_data:
    created_at = datetime.fromisoformat(record["created_at"])
    formatted_time = created_at.strftime("%d %b %Y, %I:%M %p")

    confidence_pct = round(record["confidence"] * 100, 2)

    st.markdown(
        f"""
            <div style="
            background-color:white;
            border-radius:15px;
            padding:20px;
            margin-bottom:20px;
            box-shadow:0 4px 12px rgba(0,0,0,0.25);">
            <h3 style="color:#9f1f38; margin-bottom:5px;">
                {record["cancer_type"].capitalize()} Cancer
            </h3>

            <p style="font-size:18px; margin:5px 0; color:#333;">
                <b>Prediction:</b> {record["prediction"]}
            </p>

            <p style="font-size:18px; margin:5px 0; color:#333;">
                <b>Confidence:</b> {confidence_pct}%
            </p>

            <p style="font-size:14px; color:#666; margin-top:10px;">
                🕒 {formatted_time}
            </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

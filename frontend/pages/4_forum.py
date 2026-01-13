# frontend/pages/4_forum.py

import streamlit as st
import os
from components.sidebar import sidebar

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Support Communities | CanBridge",
    page_icon="💬",
    layout="wide"
)

# -------------------------------
# SESSION GUARD
# -------------------------------
if not st.session_state.get("logged_in"):
    st.switch_page("main.py")

# -------------------------------
# SIDEBAR
# -------------------------------
sidebar()

# -------------------------------
# LOAD EXTERNAL CSS
# -------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
css_path = os.path.join(app_dir, "styles", "style.css")

if os.path.exists(css_path):
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# GLOBAL RESPONSIVE VIDEO CSS
# -------------------------------
st.markdown(
    """
    <style>
    .video-wrapper {
        position: relative;
        width: 100%;
        padding-top: 56.25%; /* 16:9 */
    }

    .video-wrapper iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# PAGE HEADER
# -------------------------------
st.markdown(
    """
    <div style="text-align:center; margin-top:20px;">
        <h1 style="color:white;">💬 Support & Community Hub</h1>
        <p style="color:#ffeaea; font-size:18px; max-width:900px; margin:auto;">
            Connect with trusted communities and survivor stories across platforms
            where real support and conversations already exist.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ======================================================
# SECTION 1 — COMMUNITY SUPPORT
# ======================================================
st.markdown(
    "<h2 style='color:white; text-align:center; margin-top:40px;'>🤝 Community Support Groups</h2>",
    unsafe_allow_html=True
)

communities = {
    "🩺 Breast Cancer": [
        ("Reddit", "https://www.reddit.com/r/breastcancer/"),
        ("Telegram", "https://t.me/s/breastcancer_support"),
        ("WhatsApp", "https://chat.whatsapp.com/"),
        ("YouTube", "https://www.youtube.com/@breastcancerorg")
    ],
    "🧠 Brain Tumor": [
        ("Reddit", "https://www.reddit.com/r/braintumor/"),
        ("Telegram", "https://t.me/s/braincancer"),
        ("WhatsApp", "https://chat.whatsapp.com/"),
        ("YouTube", "https://www.youtube.com/results?search_query=brain+tumor+survivor")
    ],
    "🖐🏻 Skin Cancer": [
        ("Reddit", "https://www.reddit.com/r/skincancer/"),
        ("Telegram", "https://t.me/s/skincancer"),
        ("WhatsApp", "https://chat.whatsapp.com/"),
        ("YouTube", "https://www.youtube.com/results?search_query=skin+cancer+survivor")
    ]
}

for cancer, links in communities.items():
    st.markdown(
        f"<h3 style='color:white; margin-top:35px; text-align:center;'>{cancer}</h3>",
        unsafe_allow_html=True
    )

    cols = st.columns(4, gap="large")

    for col, (label, link) in zip(cols, links):
        with col:
            st.markdown(
                f"""
                    <div style="
                    background:white;
                    border-radius:16px;
                    padding:22px;
                    text-align:center;
                    box-shadow:0 6px 18px rgba(0,0,0,0.2);
                    ">
                    <h4 style="color:#9f1f38;">{label}</h4>
                    <a href="{link}" target="_blank">
                        <button style="
                            background:#9f1f38;
                            color:white;
                            border:none;
                            padding:10px 16px;
                            border-radius:10px;
                            font-weight:800;
                            margin-top:10px;
                            cursor:pointer;
                        ">
                            🔗 Explore Support
                        </button>
                    </a>
                    </div>
                """,
                unsafe_allow_html=True
            )

# ======================================================
# SECTION 2 — SURVIVOR STORIES (RESPONSIVE)
# ======================================================
st.markdown(
    "<h2 style='color:white; text-align:center; margin-top:60px;'>🎥 Survivor Stories & Experiences</h2>",
    unsafe_allow_html=True
)

st.write("")

yt_cols = st.columns(2, gap="large")

with yt_cols[0]:
    st.markdown(
        """
        <div style="background:white; border-radius:18px; padding:20px; box-shadow:0 6px 18px rgba(0,0,0,0.2);">
            <h4 style="color:#9f1f38;">🎗 Breast Cancer Survivor Story</h4>
            <div class="video-wrapper">
                <iframe src="https://www.youtube.com/embed/q8j_vZRZKx0"
                        allowfullscreen></iframe>
            </div>
            <p style="color:#444; font-size:15px; margin-top:10px;">
                A survivor shares her diagnosis, treatment, and recovery journey.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with yt_cols[1]:
    st.markdown(
        """
        <div style="background:white; border-radius:18px; padding:20px; box-shadow:0 6px 18px rgba(0,0,0,0.2);">
            <h4 style="color:#9f1f38;">💬 Living Through Cancer Treatment</h4>
            <div class="video-wrapper">
                <iframe src="https://www.youtube.com/embed/6NsJZL9CX40"
                        allowfullscreen></iframe>
            </div>
            <p style="color:#444; font-size:15px; margin-top:10px;">
                Honest conversations about treatment side effects and mental resilience.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ======================================================
# DISCLAIMER
# ======================================================
st.markdown(
    """
    <div style="
        margin-top:60px;
        background:white;
        color:#9f1f38;
        padding:22px;
        border-radius:14px;
        text-align:center;
        font-weight:800;
        box-shadow:0 4px 12px rgba(0,0,0,0.25);
        max-width:950px;
        margin-left:auto;
        margin-right:auto;
    ">
        ⚠️ Community discussions and videos are for emotional support and awareness only.  
        Always consult qualified medical professionals for diagnosis and treatment decisions.
    </div>
    """,
    unsafe_allow_html=True
)

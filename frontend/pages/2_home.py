import streamlit as st
import requests
import os
import time
from datetime import date
from components.sidebar import sidebar
from config import BACKEND_URL

st.session_state["page_id"] = "Home"

# ---------------- SESSION GUARD ----------------
if not st.session_state.get("logged_in"):
    st.switch_page("main.py")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Home | CanBridge",
    page_icon="🏥",
    layout="wide"
)

sidebar()

# ---------------- LOAD EXTERNAL CSS ----------------
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
css_path = os.path.join(app_dir, "styles", "style.css")

with open(css_path, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SOFT, FLOWING STYLES ----------------
st.markdown("""
<style>
.main {
    max-width: 900px;
    margin: auto;
}

.main-title {
    color: white;
    font-size: 44px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 6px;
}

.subtitle {
    color: #ffeaea;
    font-size: 20px;
    text-align: center;
    margin-bottom: 45px;
}

.section-title {
    color: white;
    font-size: 28px;
    font-weight: 900;
    text-align: center;
    margin: 45px 0 22px 0;
}

/* FLOWING CARD */
.card {
    background: white;
    border-radius: 22px;
    padding: 32px 36px;
    margin: 0 auto 36px auto;
    box-shadow: 0 6px 24px rgba(0,0,0,0.26);
}

.card p, .card b, .card i {
    color: #333 !important;
    font-size: 19px;
    line-height: 1.7;
    text-align: center;
}

/* QUICK ACTION GRID */
.quick-actions {
    max-width: 720px;
    margin: auto;
}

.quick-actions .stButton > button {
    height: 90px;
    font-size: 18px !important;
    font-weight: 900 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<style>.stApp { background-color: #9f1f38; }</style>", unsafe_allow_html=True)

# ---------------- USER HEADER ----------------
username = st.session_state.get("user", {}).get("username", "User")

st.markdown(f"""
<div class="main">
    <div class="main-title">Welcome back, {username} 👋</div>
    <div class="subtitle">“One step at a time. You are not alone.”</div>
""", unsafe_allow_html=True)

# ==================================================
# 🌟 WARRIOR STORY OF THE DAY
# ==================================================
st.markdown("<div class='section-title'>🌟 Warrior Story of the Day</div>", unsafe_allow_html=True)

stories = []
try:
    s = requests.get(f"{BACKEND_URL}/stories", timeout=5)
    if s.status_code == 200:
        stories = s.json()
except:
    stories = []

if stories:
    index = date.today().toordinal() % len(stories)
    story = stories[index]
    st.markdown(f"""
        <div class='card'>
            <p>{story["content"][:420]}...</p>
            <i>— {story["author"] or "Anonymous"}</i>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class='card'>
            <p>Stories of courage and hope will appear here.</p>
        </div>
    """, unsafe_allow_html=True)

# ==================================================
# 📌 RECENT ACTIVITY
# ==================================================
st.markdown("<div class='section-title'>📌 Your Recent Activity</div>", unsafe_allow_html=True)

history = []
try:
    h = requests.get(f"{BACKEND_URL}/history", timeout=5)
    if h.status_code == 200:
        history = h.json()
except:
    history = []

if not history:
    st.markdown("""
        <div class='card'>
            <p><b>No activity yet.</b></p>
            <p>Run your first prediction to get started.</p>
        </div>
    """, unsafe_allow_html=True)
else:
    latest = sorted(history, key=lambda x: x["created_at"], reverse=True)[0]
    confidence = round(latest["confidence"] * 100, 2)

    st.markdown(f"""
        <div class='card'>
            <p><b>{latest["cancer_type"].capitalize()} Cancer</b></p>
            <p>Result: {latest["prediction"]}</p>
            <p>Confidence: {confidence}%</p>
        </div>
    """, unsafe_allow_html=True)

# ==================================================
# 🚀 QUICK ACTIONS (2 × 2)
# ==================================================
st.markdown("<div class='section-title'>🚀 Quick Actions</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='quick-actions'>", unsafe_allow_html=True)
    r1c1, r1c2 = st.columns(2)
    r2c1, r2c2 = st.columns(2)

    with r1c1:
        if st.button("🧬 Run Prediction", use_container_width=True):
            st.switch_page("pages/3_prediction.py")

    with r1c2:
        if st.button("💬 Join Forums", use_container_width=True):
            st.switch_page("pages/4_forum.py")

    with r2c1:
        if st.button("🌟 Warrior Stories", use_container_width=True):
            st.switch_page("pages/5_warriors.py")

    with r2c2:
        if st.button("💰 Financial Aid", use_container_width=True):
            st.switch_page("pages/6_financialaid.py")

    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# 💡 DID YOU KNOW?
# ==================================================
st.markdown("<div class='section-title'>💡 Did You Know?</div>", unsafe_allow_html=True)

facts = [
    "Early cancer detection significantly improves survival rates.",
    "Many cancers are treatable when detected early.",
    "Emotional and mental support improves recovery outcomes.",
    "AI-assisted tools help doctors make faster, accurate decisions.",
    "Financial aid programs exist for most cancer treatments in India."
]

if "fact_start" not in st.session_state:
    st.session_state.fact_start = time.time()

elapsed = int(time.time() - st.session_state.fact_start)
fact_index = (elapsed // 6) % len(facts)

st.markdown(f"""
    <div class='card'>
        <p>{facts[fact_index]}</p>
    </div>
""", unsafe_allow_html=True)

# ==================================================
# ⚠️ DISCLAIMER
# ==================================================
st.markdown("<div class='section-title'>⚠️ Medical Disclaimer</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='card'>
        <p>
        CanBridge provides AI-assisted insights only and does not replace professional medical advice.
        Always consult a qualified healthcare professional.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

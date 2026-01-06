# pages/7_information.py
import streamlit as st
from components.sidebar import sidebar

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Cancer Information | CanBridge",
    page_icon="📘",
    layout="wide"
)

# ---------------- SESSION GUARD ----------------
if not st.session_state.get("logged_in"):
    st.switch_page("main.py")
 

# Sidebar
try:
    sidebar()
except:
    with st.sidebar:
        st.write("CanBridge")

# -----------------------------
# GLOBAL CSS
# -----------------------------
st.markdown("""
<style>
.stApp { background-color:#9f1f38; }

/* Header */
.info-title {
    text-align:center;
    color:white;
    font-size:40px;
    font-weight:900;
    margin-top:20px;
}
.info-sub {
    text-align:center;
    color:#ffeaea;
    font-size:17px;
    margin-top:-8px;
    margin-bottom:25px;
}

/* Cards */
.info-card {
    background:white;
    border-radius:20px;
    padding:28px;
    box-shadow:0 6px 24px rgba(0,0,0,0.25);
    margin-bottom:25px;
    color:#333;
}
.info-card h2 {
    color:#9f1f38;
    font-size:24px;
    font-weight:900;
    margin-bottom:15px;
}
.info-card p, .info-card li {
    font-size:16px;
    line-height:1.6;
}
.info-card ul { padding-left:18px; }

.section-label {
    margin-top:12px;
    font-weight:900;
    color:#9f1f38;
    font-size:17px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='info-title'>📘 Cancer Information</div>", unsafe_allow_html=True)
st.markdown("<div class='info-sub'>Clear, trustworthy explanations to help you understand cancer and modern care options.</div>", unsafe_allow_html=True)

# -----------------------------
# TABS
# -----------------------------
tabs = st.tabs([
    "📖 About Cancer",
    "🔍 Detection & Diagnosis",
    "💊 Treatment Options",
    "⚙️ Modern Technologies",
    "🛡 Prevention",
    "❤️ Living With Cancer"
])

# -----------------------------
# HELPER: card layout
# -----------------------------
def card(title, body):
    st.markdown(f"""
    <div class='info-card'>
        <h2>{title}</h2>
        {body}
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# TAB 1 — ABOUT CANCER
# ============================================================
with tabs[0]:

    card("What is Cancer?",
    """
    Cancer is a condition where cells grow uncontrollably, ignore the body’s normal signals,
    and begin to invade nearby tissues. These abnormal cells can form tumors and potentially
    spread to other parts of the body (metastasis).

    <div class='section-label'>Why does cancer happen?</div>
    <ul>
        <li>Genetic mutations (inherited or acquired)</li>
        <li>Exposure to carcinogens (tobacco, pollution, radiation)</li>
        <li>Viral infections (HPV, Hepatitis B/C)</li>
        <li>Unhealthy lifestyle factors</li>
        <li>Age-related cell damage</li>
    </ul>

    <div class='section-label'>Major Causes & Risk Factors</div>
    <ul>
        <li>Smoking (responsible for 30% of all cancers)</li>
        <li>Alcohol consumption</li>
        <li>Poor diet & inactivity</li>
        <li>Family history of cancer</li>
        <li>Air pollution & chemical exposure</li>
        <li>Hormonal factors (especially in breast cancer)</li>
    </ul>

    <div class='section-label'>How common is cancer?</div>
    <p>
    According to WHO, **1 in 6 deaths globally** is due to cancer.  
    Early detection and awareness significantly reduce mortality.
    </p>
    """)

# ============================================================
# TAB 2 — DETECTION & DIAGNOSIS
# ============================================================
with tabs[1]:

    card("How Cancer is Detected",
    """
    Doctors use a combination of imaging, laboratory tests, and tissue analysis to confirm cancer.

    <div class='section-label'>Key Detection Methods</div>
    <ul>
        <li><b>MRI Scan</b> — Ideal for brain tumors and soft tissue cancers</li>
        <li><b>CT Scan</b> — Commonly used for lung, abdominal, and pelvic cancers</li>
        <li><b>Mammography</b> — Specialized imaging to detect breast cancer early</li>
        <li><b>Ultrasound</b> — Safe & helpful in spotting lumps or abnormalities</li>
        <li><b>PET Scan</b> — Detects active cancer cells using radioactive tracers</li>
    </ul>

    <div class='section-label'>Histopathology</div>
    <p>
    This is the gold standard for diagnosis. A small tissue sample (biopsy) is examined under a microscope
    to determine whether cells are cancerous and what type they are.
    </p>

    <div class='section-label'>AI-Assisted Detection</div>
    <p>
    Modern AI tools (like those used in CanBridge) help highlight suspicious regions in scans,
    improving early detection.  
    <b>Note:</b> AI cannot replace a clinical diagnosis — it only assists doctors.
    </p>
    """)

# ============================================================
# TAB 3 — TREATMENT OPTIONS
# ============================================================
with tabs[2]:

    card("Medical Treatments",
    """
    Cancer treatment is personalized based on cancer type, stage, and patient health.

    <div class='section-label'>Main Treatment Types</div>
    <ul>
        <li><b>Surgery</b> — Removes tumors when possible</li>
        <li><b>Chemotherapy</b> — Targets rapidly dividing cells</li>
        <li><b>Radiation Therapy</b> — High-energy rays destroy cancer cells</li>
        <li><b>Immunotherapy</b> — Boosts the immune system's response</li>
        <li><b>Targeted Therapy</b> — Attacks specific mutations</li>
        <li><b>Hormone Therapy</b> — For breast/prostate cancers</li>
    </ul>
    """)

    card("Lifestyle & Supportive Measures",
    """
    <ul>
        <li>Balanced diet with protein & antioxidants</li>
        <li>Regular light exercise (walking, yoga)</li>
        <li>Stress reduction (meditation, counseling)</li>
        <li>Proper sleep & hydration</li>
        <li>Avoid smoking & alcohol completely</li>
    </ul>

    <p><b>Support therapies:</b> physiotherapy, speech therapy, pain care, psychological support.</p>
    """)

    st.info("⚠ **Disclaimer:** This page provides general medical information. Always consult a licensed oncologist for treatment decisions.")

# ============================================================
# TAB 4 — MODERN TECHNOLOGIES
# ============================================================
with tabs[3]:

    card("Advanced Cancer Technologies",
    """
    Modern tools have significantly improved accuracy and survival rates.

    <div class='section-label'>Key Technologies</div>
    <ul>
        <li><b>Robotic Surgery (Da Vinci System)</b> — High precision, faster healing</li>
        <li><b>Proton Beam Therapy</b> — Targets tumors with minimal side damage</li>
        <li><b>CyberKnife</b> — Robotic radiation for hard-to-reach tumors</li>
        <li><b>AI-based Radiology</b> — Early detection using pattern recognition</li>
        <li><b>Genomic Sequencing</b> — Personalized medicine based on DNA mutations</li>
        <li><b>Liquid Biopsy</b> — Detects tumor DNA through blood testing</li>
        <li><b>Biomarker-driven Therapy</b> — Extremely precise targeted drugs</li>
    </ul>

    <div class='section-label'>Success Improvements</div>
    <p>
    These technologies have increased early detection and reduced the need for aggressive treatments in many cancers.
    Survival rates have improved significantly for breast, prostate, cervical, and childhood cancers.
    </p>
    """)

# ============================================================
# TAB 5 — PREVENTION
# ============================================================
with tabs[4]:

    card("How to Reduce Cancer Risk",
    """
    <ul>
        <li>Avoid tobacco completely</li>
        <li>Maintain a healthy body weight</li>
        <li>Exercise 30 minutes daily</li>
        <li>Limit processed foods & sugar</li>
        <li>Get vaccinated (HPV, Hepatitis B)</li>
        <li>Reduce alcohol intake</li>
        <li>Protect your skin from UV exposure</li>
    </ul>

    <div class='section-label'>Early Warning Signs</div>
    <ul>
        <li>Unexplained weight loss</li>
        <li>Lumps or swellings</li>
        <li>Persistent cough</li>
        <li>Unusual bleeding</li>
        <li>Non-healing wounds</li>
        <li>Severe fatigue</li>
    </ul>
    """)

# ============================================================
# TAB 6 — LIVING WITH CANCER
# ============================================================
with tabs[5]:

    card("Emotional & Mental Health",
    """
    <p>
    A cancer diagnosis affects mental well-being.  
    Support groups, counseling, meditation, and open communication play an essential role.
    </p>
    <ul>
        <li>Talk therapy & oncology counselors</li>
        <li>Support groups (online & offline)</li>
        <li>Meditation, journaling, guided breathing</li>
        <li>Talking openly with trusted people</li>
    </ul>
    """)

    card("Nutrition During Treatment",
    """
    <ul>
        <li>Small, frequent meals</li>
        <li>High protein foods (eggs, lentils, fish)</li>
        <li>Fruits & vegetables rich in antioxidants</li>
        <li>Hydration: 2–3 liters per day</li>
        <li>Avoid spicy, oily, or very sugary foods</li>
    </ul>
    <p>A registered dietitian can help tailor a personalized nutrition plan.</p>
    """)

# Padding
st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

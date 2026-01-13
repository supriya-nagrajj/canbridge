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

.info-card {
    background:white;
    border-radius:20px;
    padding:30px;
    box-shadow:0 6px 24px rgba(0,0,0,0.25);
    margin-bottom:30px;
    color:#333;
}
.info-card h2 {
    color:#9f1f38;
    font-size:26px;
    font-weight:900;
    margin-bottom:18px;
}
.info-card p, .info-card li {
    font-size:16px;
    line-height:1.75;
}
.info-card ul {
    padding-left:20px;
}

.section-label {
    margin-top:20px;
    font-weight:900;
    color:#9f1f38;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='info-title'>📘 Cancer Information</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='info-sub'>A comprehensive guide to understanding cancer, diagnosis, treatment, and life beyond.</div>",
    unsafe_allow_html=True
)

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
# Helper
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

    card("Understanding Cancer at a Cellular Level",
    """
    <p>
    Cancer is not a single disease, but a broad group of diseases characterized by
    abnormal cell growth. In a healthy body, cells grow, divide, and die in a tightly
    regulated manner. Cancer develops when this regulation breaks down.
    </p>

    <p>
    Cancer cells ignore signals that normally stop cell division, evade programmed cell death,
    and may acquire the ability to invade surrounding tissues. Over time, these abnormal cells
    can form tumors and spread to distant organs through blood or lymphatic systems — a process
    known as metastasis.
    </p>

    <div class='section-label'>How Cancer Begins</div>
    <p>
    Cancer begins due to mutations in DNA. These mutations may be inherited or acquired
    during a person’s lifetime due to environmental exposure or natural aging.
    </p>

    <ul>
        <li>Errors during normal cell division</li>
        <li>Exposure to tobacco smoke, chemicals, or radiation</li>
        <li>Chronic inflammation or infections</li>
        <li>Hormonal imbalances</li>
        <li>Weakened immune surveillance</li>
    </ul>

    <div class='section-label'>Why Early Detection Matters</div>
    <p>
    When cancer is detected early, treatment options are more effective, less aggressive,
    and outcomes are significantly better. Many cancers detected at Stage I or II
    have survival rates exceeding 80–90%.
    </p>
    """)

# ============================================================
# TAB 2 — DETECTION & DIAGNOSIS
# ============================================================
with tabs[1]:

    card("How Doctors Diagnose Cancer",
    """
    <p>
    Cancer diagnosis is a multi-step process. Doctors rarely rely on a single test.
    Instead, they combine clinical evaluation, imaging, laboratory tests, and
    tissue analysis to reach a confirmed diagnosis.
    </p>

    <div class='section-label'>Imaging Techniques</div>
    <p>
    Imaging helps doctors visualize internal organs and identify abnormal structures.
    </p>
    <ul>
        <li><b>MRI:</b> Excellent for brain, spine, and soft tissue evaluation</li>
        <li><b>CT Scan:</b> Cross-sectional imaging for lungs, abdomen, pelvis</li>
        <li><b>Ultrasound:</b> Safe, radiation-free imaging for lumps and masses</li>
        <li><b>Mammography:</b> Specialized breast imaging for early detection</li>
        <li><b>PET Scan:</b> Identifies metabolically active cancer cells</li>
    </ul>

    <div class='section-label'>Biopsy & Histopathology</div>
    <p>
    A biopsy involves removing a small tissue sample from the suspected area.
    This sample is examined under a microscope by a pathologist.
    </p>
    <p>
    Histopathology determines:
    </p>
    <ul>
        <li>Whether cancer is present</li>
        <li>The exact cancer type</li>
        <li>How aggressive the cancer appears</li>
    </ul>

    <div class='section-label'>Role of AI in Detection</div>
    <p>
    Artificial Intelligence assists clinicians by highlighting patterns that may be
    difficult to detect with the human eye. AI tools improve speed and consistency,
    especially in imaging-heavy workflows.
    </p>
    """)

# ============================================================
# TAB 3 — TREATMENT OPTIONS
# ============================================================
with tabs[2]:

    card("Clinical Treatment Approaches",
    """
    <p>
    Cancer treatment is individualized. Factors such as cancer type, stage,
    molecular profile, age, and overall health influence treatment decisions.
    </p>

    <div class='section-label'>Primary Treatment Modalities</div>
    <ul>
        <li><b>Surgery:</b> Removes localized tumors when feasible</li>
        <li><b>Chemotherapy:</b> Systemic drugs targeting rapidly dividing cells</li>
        <li><b>Radiation Therapy:</b> Localized destruction using high-energy beams</li>
        <li><b>Immunotherapy:</b> Activates the immune system to fight cancer</li>
        <li><b>Targeted Therapy:</b> Attacks specific genetic mutations</li>
        <li><b>Hormone Therapy:</b> Used in hormone-sensitive cancers</li>
    </ul>

    <div class='section-label'>Side Effects & Management</div>
    <p>
    Treatments may cause fatigue, nausea, hair loss, or immune suppression.
    Supportive care helps manage these effects and improve quality of life.
    </p>
    """)

# ============================================================
# TAB 4 — MODERN TECHNOLOGIES
# ============================================================
with tabs[3]:

    card("Technological Advances in Cancer Care",
    """
    <p>
    Advances in technology have transformed cancer care from generalized treatment
    to highly personalized medicine.
    </p>

    <ul>
        <li><b>Robotic Surgery:</b> Precision with minimal invasion</li>
        <li><b>Proton Therapy:</b> Reduced radiation damage to healthy tissue</li>
        <li><b>AI Radiology:</b> Faster scan interpretation</li>
        <li><b>Genomic Profiling:</b> DNA-based treatment decisions</li>
        <li><b>Liquid Biopsy:</b> Cancer detection through blood samples</li>
    </ul>

    <p>
    These innovations reduce treatment toxicity, shorten recovery time,
    and improve long-term outcomes.
    </p>
    """)

# ============================================================
# TAB 5 — PREVENTION
# ============================================================
with tabs[4]:

    card("Reducing Cancer Risk",
    """
    <p>
    While not all cancers are preventable, many can be reduced through lifestyle changes
    and preventive care.
    </p>

    <ul>
        <li>Eliminate tobacco exposure</li>
        <li>Maintain a healthy body weight</li>
        <li>Stay physically active</li>
        <li>Eat a balanced, plant-rich diet</li>
        <li>Protect skin from UV radiation</li>
        <li>Participate in screening programs</li>
    </ul>

    <div class='section-label'>Early Warning Signs</div>
    <p>
    Persistent symptoms should never be ignored. Early medical attention saves lives.
    </p>
    """)

# ============================================================
# TAB 6 — LIVING WITH CANCER
# ============================================================
with tabs[5]:

    card("Life Beyond Diagnosis",
    """
    <p>
    A cancer diagnosis affects emotional, social, and psychological well-being.
    Managing mental health is just as important as treating the disease itself.
    </p>

    <div class='section-label'>Emotional Support</div>
    <ul>
        <li>Counseling and psycho-oncology care</li>
        <li>Peer and survivor support groups</li>
        <li>Mindfulness and stress management</li>
    </ul>
    """)

    card("Nutrition & Daily Living",
    """
    <p>
    Nutrition supports recovery, immunity, and energy levels during treatment.
    </p>

    <ul>
        <li>Small, frequent meals</li>
        <li>Adequate protein intake</li>
        <li>Hydration and electrolyte balance</li>
        <li>Limiting processed foods</li>
    </ul>

    <p>
    Always consult a qualified nutritionist for personalized advice.
    </p>
    """)

st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

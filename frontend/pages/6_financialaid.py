# frontend/pages/6_financialaid.py

import streamlit as st
import os
from components.sidebar import sidebar

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Financial Support | CanBridge",
    page_icon="💰",
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
# FORCE RED BACKGROUND (SAFE)
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #9f1f38 !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD GLOBAL CSS (IF EXISTS)
# -------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
css_path = os.path.join(app_dir, "styles", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# LOCAL CARD STYLES
# -------------------------------
st.markdown("""
<style>
.fin-card {
    background: white;
    color: #333;
    border-radius: 18px;
    padding: 26px;
    margin-bottom: 28px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.22);
}
.fin-card h3 {
    color: #9f1f38;
    margin-bottom: 12px;
}
.fin-label {
    font-weight: 900;
    color: #9f1f38;
}
.fin-card p {
    font-size: 15.5px;
    line-height: 1.6;
}
.fin-link a {
    color: #9f1f38;
    font-weight: 900;
    text-decoration: none;
}
.fin-link a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# HEADER
# ===============================
st.markdown("""
<div style="text-align:center; margin-top:25px;">
    <h1 style="color:white; font-size:44px;">💰 Financial Support for Cancer Treatment (India)</h1>
    <p style="color:#ffeaea; font-size:18px; max-width:900px; margin:auto;">
        This section is designed to guide cancer patients and caregivers through
        real financial support options available in India — including government
        schemes, trusted NGOs, and hospital-based assistance.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ===============================
# TABS
# ===============================
gov_tab, ngo_tab, guide_tab, hospital_tab = st.tabs([
    "🏛 Government Schemes",
    "🤝 NGOs & Trusts",
    "🧠 How Financial Help Works",
    "🏥 Hospital Financial Help Desks"
])

# ======================================================
# GOVERNMENT SCHEMES
# ======================================================
with gov_tab:

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="fin-card">
            <h3>Rashtriya Arogya Nidhi (RAN)</h3>
            <p><span class="fin-label">Who it is for:</span> Indian citizens from economically weaker sections undergoing treatment in government hospitals.</p>
            <p><span class="fin-label">Cancer types:</span> All cancers (priority to life-threatening and advanced cases).</p>
            <p><span class="fin-label">Geographic coverage:</span> Pan-India (through Regional Cancer Centres & major government hospitals).</p>
            <p><span class="fin-label">Financial support:</span> Case-dependent grants; often substantial for surgery, chemotherapy, or radiation.</p>
            <p><span class="fin-label">How patients access it:</span> Applications are routed through the treating government hospital’s medical superintendent or social work department.</p>
            <p class="fin-link">Visit : <a href="https://www.mohfw.gov.in" target="_blank">Ministry of Health & Family Welfare</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="fin-card">
            <h3>Ayushman Bharat – PM-JAY</h3>
            <p><span class="fin-label">Who it is for:</span> Families listed under SECC or meeting income-based eligibility criteria.</p>
            <p><span class="fin-label">Cancer types:</span> Breast, cervical, oral, lung, gastrointestinal, and several others.</p>
            <p><span class="fin-label">Geographic coverage:</span> Pan-India (only at empanelled hospitals).</p>
            <p><span class="fin-label">Financial support:</span> Coverage up to ₹5 lakh per family per year.</p>
            <p><span class="fin-label">How patients access it:</span> Enrollment and treatment occur directly at Ayushman-empanelled hospitals.</p>
            <p class="fin-link">Visit : <a href="https://pmjay.gov.in" target="_blank">Official PM-JAY Portal</a></p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown("""
        <div class="fin-card">
            <h3>Prime Minister’s National Relief Fund (PMNRF)</h3>
            <p><span class="fin-label">Focus:</span> Financial relief for patients suffering from serious and life-threatening illnesses.</p>
            <p><span class="fin-label">Cancer types:</span> All cancers.</p>
            <p><span class="fin-label">Primary locations:</span> Pan-India.</p>
            <p><span class="fin-label">Type of support:</span> Direct financial grants (amount decided case-wise).</p>
            <p><span class="fin-label">How to approach:</span> Online application with medical and income documentation.</p>
            <p class="fin-link">Visit : <a href="https://www.pmindia.gov.in/en/pms-funds/" target="_blank">PMNRF Official Portal</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="fin-card">
            <h3>State Illness Assistance Funds (SIAF)</h3>
            <p><span class="fin-label">Focus:</span> State-level financial assistance for residents undergoing major medical treatment.</p>
            <p><span class="fin-label">Cancer types:</span> Most cancer types (state-specific policies).</p>
            <p><span class="fin-label">Primary locations:</span> Respective Indian states.</p>
            <p><span class="fin-label">Type of support:</span> Partial or full treatment cost reimbursement (case-dependent).</p>
            <p><span class="fin-label">How to approach:</span> Application through state health departments or government hospitals.</p>
            <p class="fin-link">Visit : <a href="https://www.nhp.gov.in" target="_blank">National Health Portal (India)</a></p>
        </div>
        """, unsafe_allow_html=True)


# ======================================================
# NGOs & TRUSTS (STRICTLY FINANCIAL)
# ======================================================
with ngo_tab:

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="fin-card">
            <h3>Cancer Patients Aid Association (CPAA)</h3>
            <p><span class="fin-label">Focus:</span> Financial aid for underprivileged cancer patients.</p>
            <p><span class="fin-label">Cancer types:</span> All.</p>
            <p><span class="fin-label">Primary locations:</span> Mumbai and nearby regions.</p>
            <p><span class="fin-label">Type of support:</span> Assistance for treatment costs, diagnostics, and medicines (case-based).</p>
            <p><span class="fin-label">How to approach:</span> Referral via hospital social worker or direct application.</p>
            <p class="fin-link">Visit : <a href="https://cancer.org.in" target="_blank">cancer.org.in</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="fin-card">
            <h3>Indian Cancer Society – Cancer Cure Fund</h3>
            <p><span class="fin-label">Focus:</span> Financial assistance for economically disadvantaged cancer patients.</p>
            <p><span class="fin-label">Cancer types:</span> All.</p>
            <p><span class="fin-label">Coverage:</span> Multiple states across India.</p>
            <p><span class="fin-label">Type of support:</span> Treatment and diagnostic cost assistance.</p>
            <p><span class="fin-label">How to approach:</span> Application with income proof and medical documents.</p>
            <p class="fin-link">Visit : <a href="https://www.indiancancersociety.org" target="_blank">indiancancersociety.org</a></p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown("""
        <div class="fin-card">
            <h3>Tata Trusts – Medical Grants Programme</h3>
            <p><span class="fin-label">Focus:</span> Financial grants for treatment of serious illnesses including cancer.</p>
            <p><span class="fin-label">Cancer types:</span> All cancers.</p>
            <p><span class="fin-label">Primary locations:</span> Pan-India (through partner hospitals).</p>
            <p><span class="fin-label">Type of support:</span> Case-based financial grants toward treatment costs.</p>
            <p><span class="fin-label">How to approach:</span> Referral via hospital or partnered NGOs.</p>
            <p class="fin-link">Visit : <a href="https://www.tatatrusts.org" target="_blank">tatatrusts.org</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="fin-card">
            <h3>CanKids… KidsCan</h3>
            <p><span class="fin-label">Focus:</span> Financial and treatment support for children with cancer.</p>
            <p><span class="fin-label">Cancer types:</span> Pediatric cancers (leukemia, brain tumors, solid tumors).</p>
            <p><span class="fin-label">Primary locations:</span> Multiple cities across India.</p>
            <p><span class="fin-label">Type of support:</span> Treatment funding, diagnostics, and supportive care.</p>
            <p><span class="fin-label">How to approach:</span> Referral through partner hospitals or direct NGO contact.</p>
            <p class="fin-link">Visit : <a href="https://cankidsindia.org" target="_blank">cankidsindia.org</a></p>
        </div>
        """, unsafe_allow_html=True)

# ======================================================
# HOW FINANCIAL HELP ACTUALLY WORKS (GUIDED, NOT STEPS)
# ======================================================
with guide_tab:
    st.markdown("""
        <div class="fin-card">
        <h3 style="font-size:26px;">Understanding Financial Support in Cancer Care</h3>

        <p style="font-size:17px; line-height:1.8;">
        For many patients and caregivers, the financial side of cancer treatment can feel
        overwhelming — not because support doesn’t exist, but because the system is fragmented.
        In India, financial assistance is rarely accessed through a single form or portal.
        Instead, it works as a coordinated effort between hospitals, government schemes,
        and trusted non-profit organizations.
        </p>

        <h4 style="color:#9f1f38; font-size:20px; margin-top:22px;">
        Where Financial Support Usually Begins
        </h4>
        <p style="font-size:17px; line-height:1.8;">
        The starting point is almost always the treating hospital.
        Once a diagnosis is confirmed, the hospital generates an estimated treatment cost.
        This estimate becomes the foundation for all financial assistance applications.
        Hospital social work departments use this information to determine which government
        schemes or NGOs are suitable for the patient’s medical and financial situation.
        </p>

        <h4 style="color:#9f1f38; font-size:20px; margin-top:22px;">
        Role of Government Schemes and NGOs
        </h4>
        <p style="font-size:17px; line-height:1.8;">
        Government schemes are generally explored first, as they tend to offer the largest
        coverage for treatment expenses such as surgery, chemotherapy, and radiation.
        However, these schemes may not cover every cost.
        NGOs play a critical role by bridging gaps — helping with medicines, diagnostics,
        travel expenses, or partial treatment funding where government aid falls short.
        </p>

        <h4 style="color:#9f1f38; font-size:20px; margin-top:22px;">
        Importance of Documentation
        </h4>
        <p style="font-size:17px; line-height:1.8;">
        Documentation is a key deciding factor in financial assistance.
        Most schemes and NGOs require a combination of medical reports,
        hospital cost estimates, income certificates, and identity proof.
        Keeping organized copies of these documents significantly improves
        approval chances and reduces delays.
        </p>

        <h4 style="color:#9f1f38; font-size:20px; margin-top:22px;">
        Why Hospital Social Work Departments Matter
        </h4>
        <p style="font-size:17px; line-height:1.8;">
        Hospital social workers act as navigators through the financial support system.
        They are familiar with current schemes, application procedures,
        and trusted charitable funds.
        Engaging with them early allows patients to access support in parallel
        with treatment planning, instead of reacting after costs become unmanageable.
        </p>
        </div>
    """, unsafe_allow_html=True)


# ======================================================
# HOSPITAL FINANCIAL HELP DESKS
# ======================================================
with hospital_tab:
    st.markdown("""
    <div class="fin-card">
        <h3>Tata Memorial Hospital (Mumbai)</h3>
        <p>
        Tata Memorial Hospital has a dedicated Medical Social Work Department that assists
        patients in accessing government schemes, charitable funds, and NGO support.
        </p>
        <p>
        The team evaluates financial need, helps prepare applications, and coordinates
        with trusts and relief funds for eligible patients.
        </p>
        <p><span class="fin-label">Who should approach:</span> Patients seeking subsidized or free treatment.</p>
        <p><span class="fin-label">Official site:</span> <a href="https://tmc.gov.in" target="_blank">tmc.gov.in</a></p>
    </div>

    <div class="fin-card">
        <h3>AIIMS & Regional Cancer Centres</h3>
        <p>
        AIIMS and government Regional Cancer Centres across India actively facilitate
        financial assistance through central and state schemes.
        </p>
        <p>
        Social work units guide patients through Rashtriya Arogya Nidhi,
        state illness assistance funds, and hospital-linked charitable trusts.
        </p>
        <p><span class="fin-label">Who should approach:</span> Patients receiving treatment in government hospitals.</p>
        <p><span class="fin-label">Official portal:</span> <a href="https://www.aiims.edu" target="_blank">aiims.edu</a></p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# DISCLAIMER
# ======================================================
st.markdown("""
<div style="
    background:white;
    color:#9f1f38;
    padding:20px;
    border-radius:14px;
    font-weight:900;
    text-align:center;
    max-width:900px;
    margin:50px auto 30px auto;
    box-shadow:0 4px 14px rgba(0,0,0,0.25);
">
⚠️ Financial assistance availability varies by case, documentation, hospital, and policy updates.
Always verify details through official portals or hospital social work departments.
</div>
""", unsafe_allow_html=True)

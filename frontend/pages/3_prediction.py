import streamlit as st
import requests
import os
from components.sidebar import sidebar
from config import BACKEND_URL

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Cancer Prediction | CanBridge",
    page_icon="🧬",
    layout="wide"
)

# ---------------- SESSION GUARD ----------------
if not st.session_state.get("logged_in"):
    st.switch_page("main.py")

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
# HIDE DEFAULT STREAMLIT NAV
# -------------------------------
st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR
# -------------------------------
sidebar()

# -------------------------------
# HEADER
# -------------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:white;'>
        🧬 Cancer Prediction
    </h1>
    <p style='text-align:center; color:#ffeaea; font-size:18px;'>
        Upload a medical image and receive an AI-assisted observation.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# -------------------------------
# SESSION STATE
# -------------------------------
if "selected_cancer" not in st.session_state:
    st.session_state.selected_cancer = None

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

if "confirm_input" not in st.session_state:
    st.session_state.confirm_input = False

# -------------------------------
# CANCER TYPE SELECTION
# -------------------------------
st.markdown(
    "<h3 style='color:white;'>Select Cancer Type</h3>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("🩺 Breast Cancer", use_container_width=True):
        st.session_state.selected_cancer = "breast"
        st.session_state.confirm_input = False

with col2:
    if st.button("🧠 Brain Tumor", use_container_width=True):
        st.session_state.selected_cancer = "brain"
        st.session_state.confirm_input = False

with col3:
    if st.button("🖐🏻 Skin Cancer", use_container_width=True):
        st.session_state.selected_cancer = "skin"
        st.session_state.confirm_input = False

# -------------------------------
# SHOW SELECTED CANCER TYPE
# -------------------------------
if st.session_state.selected_cancer:
    st.markdown(
        f"""
        <p style="color:white; font-size:18px; font-weight:700; margin-top:10px;">
            Selected: {st.session_state.selected_cancer.capitalize()} Cancer
        </p>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ==================================================
# 📋 INPUT INSTRUCTIONS (NEW — SAFE ADDITION)
# ==================================================
if st.session_state.selected_cancer:

    if st.session_state.selected_cancer == "breast":
        instructions = """
        ✔ Upload a **breast ultrasound image**  
        ✔ Lesion should be clearly visible  
        ✖ Do NOT upload MRI, CT, X-ray, reports, or phone photos  
        """

    elif st.session_state.selected_cancer == "brain":
        instructions = """
        ✔ Upload a **brain MRI scan**  
        ✔ Axial / sagittal / coronal views are acceptable  
        ✖ Do NOT upload CT scans, X-rays, or reports  
        """

    else:  # skin
        instructions = """
        ✔ Upload a **dermatoscopic image** of a skin lesion  
        ✔ Close-up, well-lit lesion preferred  
        ✖ Do NOT upload selfies or normal skin photos  
        """

    st.markdown(
        f"""
            <div style="
            background-color:white;
            border-radius:14px;
            padding:20px;
            margin-bottom:15px;
            box-shadow:0 4px 12px rgba(0,0,0,0.3);
            color:#9f1f38;
            font-size:15px;
            ">
                <b>📋 Image Upload Guidelines</b><br><br>
                {instructions}  <br>
                <i style="font-size:13px;">
                Predictions assume the uploaded image matches the expected medical imaging type.
                </i>
            </div>
        """,
        unsafe_allow_html=True
    )

    st.session_state.confirm_input = st.checkbox(
        "I confirm that the uploaded image matches the required medical imaging type."
    )

# -------------------------------
# IMAGE UPLOAD
# -------------------------------
uploaded_image = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"],
    disabled=(st.session_state.selected_cancer is None)
)

if uploaded_image:
    st.image(uploaded_image, width=350)

st.write("")

# -------------------------------
# RUN PREDICTION
# -------------------------------
if st.button(
    "🔍 Run Prediction",
    disabled=(uploaded_image is None or not st.session_state.confirm_input)
):

    with st.spinner("Running prediction..."):
        files = {"file": uploaded_image}
        url = f"{BACKEND_URL}/predict/{st.session_state.selected_cancer}"
        response = requests.post(url, files=files)

    if response.status_code == 200:
        st.session_state.prediction_result = response.json()
    else:
        st.error("Prediction failed. Please try again.")

# -------------------------------
# DISPLAY RESULT
# -------------------------------
if st.session_state.prediction_result:

    result = st.session_state.prediction_result
    confidence_pct = round(result["confidence"] * 100, 2)

    st.markdown(
        f"""
            <div style="
            background-color:white;
            border-radius:15px;
            padding:30px;
            box-shadow:0 4px 14px rgba(0,0,0,0.35);
            margin-top:30px;
            text-align:center;
            ">
            <h2 style="color:#9f1f38; font-size:32px;">
                {result['prediction']}
            </h2>
            <h3 style="color:#9f1f38;">
                Confidence: {confidence_pct}%
            </h3>
            <p style="font-size:14px; color:#444;">
                This result assumes a valid medical image was provided.
            </p>
            </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    colA, colB = st.columns(2, gap="large")

    # -------------------------------
    # GENERATE CARE PLAN (PDF)
    # -------------------------------
    with colA:
        if st.button("📄 Generate Care Plan", use_container_width=True):
            report_url = f"{BACKEND_URL}/report/{result['prediction_id']}"
            st.markdown(
                f"[Click here to download your care plan]({report_url})",
                unsafe_allow_html=True
            )

    # -------------------------------
    # SAVED INDICATOR
    # -------------------------------
    with colB:
        st.button("💾 Saved to History", use_container_width=True, disabled=True)

    # -------------------------------
    # DISCLAIMER
    # -------------------------------
    st.markdown(
        """
        <div style="
            margin-top: 25px;
            padding: 18px;
            border-radius: 10px;
            background-color: #ffffff;
            color: #9f1f38;
            font-weight: 900;
            text-align: center;
            font-size: 16px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.3);
        ">
            ⚠️ <b>Important Reminder:</b><br>
            AI-assisted results are supportive insights only.<br>
            Always consult a qualified medical professional.
        </div>
        """,
        unsafe_allow_html=True,
    )

# pages/3_prediction.py
import streamlit as st
import os
from components.sidebar import sidebar

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Cancer Prediction | CanBridge",
    page_icon="🧬",
    layout="wide"
)

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
# HIDE DEFAULT STREAMLIT SIDEBAR PAGE NAV
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
# SIDEBAR NAVIGATION
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
    🧬 Cancer Prediction
    </h1>
    <p style='text-align:center; color:#ffeaea; font-size:18px; margin-top:-10px;'>
    Upload a medical image and receive an AI-assisted observation.
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# -------------------------------
# CANCER TYPE CARD SELECTION
# -------------------------------
st.markdown("<h3 style='color:white; margin-bottom:10px;'>Select Cancer Type</h3>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .select-card {
        background-color: #ffffff;
        color: #9f1f38;
        font-weight: 900;
        border-radius: 15px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        cursor: pointer;
        transition: 0.2s ease;
    }
    .select-card:hover {
        background-color: #ffe6ea;
        transform: translateY(-3px);
    }
    .selected-card {
        border: 4px solid #ffd353;
        background-color: #fff6d6 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# state for selected cancer
if "selected_cancer" not in st.session_state:
    st.session_state["selected_cancer"] = None

def select(label):
    st.session_state["selected_cancer"] = label

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("🩺 Breast Cancer\n(Histopathology)", use_container_width=True):
        select("breast")

with col2:
    if st.button("🧠 Brain Tumor\n(MRI)", use_container_width=True):
        select("brain")

with col3:
    if st.button("🫁 Lung Cancer\n(Image)", use_container_width=True):
        select("lung")

st.write("")

if st.session_state["selected_cancer"]:
    st.markdown(
        "<p style='color:white; font-size:18px; font-weight:700;'>Selected: "
        + st.session_state["selected_cancer"].capitalize()
        + "</p>",
        unsafe_allow_html=True,
    )

# -------------------------------
# IMAGE UPLOAD
# -------------------------------
uploaded_image = st.file_uploader(
    "Upload Image", type=["jpg", "jpeg", "png"], disabled=(st.session_state["selected_cancer"] is None)
)

if uploaded_image:
    # show a smaller preview to avoid huge images
    st.image(uploaded_image, caption="Uploaded Image Preview", width=350)

st.write("")

# -------------------------------
# PREDICT BUTTON
# -------------------------------
predict_btn = st.button("🔍 Run Prediction", use_container_width=True, disabled=(uploaded_image is None))

# -------------------------------
# RESULT DISPLAY
# -------------------------------
if predict_btn:

    # TEMP VALUES
    result = "Cancer Detected"      # later replaced by model
    confidence = "89%"              # later replaced by model

    conf_val = int(confidence.replace("%", ""))
    confidence_color = "#28a745" if conf_val >= 85 else "#f0ad4e" if conf_val >= 60 else "#d9534f"

    # ——— CLEAN RESULT HTML ———
    result_html = """
    <div style="
        background-color:white;
        border-radius:15px;
        padding:30px;
        box-shadow:0 4px 14px rgba(0,0,0,0.35);
        margin-top:30px;
        text-align:center;
    ">
        <h2 style="color:#9f1f38; font-size:32px; margin-bottom:20px;">
            {result_text}
        </h2>
        <h2 style="color:#9f1f38; font-size:32px; margin-bottom:20px;">
            {conf_value} Confidence
        </h2>

        
    </div>
    """.format(
        result_text=result,
        conf_color=confidence_color,
        conf_value=confidence
    )

    # ——— DISPLAY RESULT ———
    st.markdown(result_html, unsafe_allow_html=True)

    # ACTION BUTTONS
    # ---------------------------
    st.write("")  # spacing
    colA, colB = st.columns(2, gap="large")
    colC, colD = st.columns(2, gap="large")

    with colA:
        st.button("📄 Download Care Roadmap (PDF)", use_container_width=True)

    with colB:
        st.button("💬 Talk to the Community", use_container_width=True)

    with colC:
        st.button("🌐 Explore Support Resources", use_container_width=True)

    with colD:
        st.button("💾 Save to History", use_container_width=True)

    # ---------------------------
    # DISCLAIMER
    # ---------------------------
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
            AI results are only supportive insights.<br>
            Always consult a qualified medical professional.
        </div>
        """,
        unsafe_allow_html=True,
    )

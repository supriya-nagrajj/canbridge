import streamlit as st
from components.sidebar import sidebar

st.set_page_config(page_title="Financial Aid | CanBridge", page_icon="💰", layout="wide")

# Sidebar
try:
    sidebar()
except:
    with st.sidebar:
        st.write("CanBridge")

# --------------------------
# CSS  (NO indentation!)
# --------------------------
st.markdown("""
<style>
.stApp {
    background-color: #9f1f38;
}
.fa-title {
    text-align:center;
    color:white;
    font-size:40px;
    font-weight:900;
    margin-top:25px;
}
.fa-sub {
    text-align:center;
    color:#ffeaea;
    font-size:18px;
    margin-top:-10px;
    margin-bottom:25px;
}

/* Card */
.aid-card {
    background:white;
    border-radius:20px;
    padding:25px;
    box-shadow:0 6px 22px rgba(0,0,0,0.22);
    margin-bottom:28px;
    color:#9f1f38;
}
.aid-title {
    font-size:26px;
    font-weight:900;
    margin-bottom:6px;
}
.tag {
    display:inline-block;
    background:#ffd353;
    padding:6px 14px;
    border-radius:999px;
    font-weight:900;
    font-size:13px;
    margin-bottom:10px;
}
.label {
    margin-top:12px;
    font-size:15px;
    font-weight:900;
    color:#555;
}
.apply-btn {
    background:#ffd353;
    padding:10px 20px;
    border-radius:10px;
    color:#9f1f38;
    font-weight:900;
    border:none;
    cursor:pointer;
    margin-top:18px;
}
.apply-btn:hover {
    background:#ffcc33;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# HEADER
# ---------------------------------------
st.markdown("<h1 class='fa-title'>💰 Financial Aid Support</h1>", unsafe_allow_html=True)
st.markdown("<p class='fa-sub'>NGOs and Government programs that help cancer patients.</p>", unsafe_allow_html=True)

# ---------------------------------------
# Tabs
# ---------------------------------------
ngo_tab, gov_tab = st.tabs(["🏥 NGO Support", "🏛 Government Schemes"])


# ------------------------------------------------------
# DATA LISTS (no HTML in data, only plain values)
# ------------------------------------------------------
ngo_data = [
    {
        "name": "Cancer Care Foundation",
        "location": "Mumbai, Pune, Chennai",
        "cancers": "Breast, Lung, Brain",
        "eligibility": "Low-income families with medical certificate",
        "description": "Provides financial support for treatment and diagnostics.",
        "link": "https://example-ngo.org"
    },
    {
        "name": "Hope Warriors Trust",
        "location": "Bangalore, Delhi",
        "cancers": "All cancer types",
        "eligibility": "BPL families",
        "description": "Support for chemotherapy, medicine, and hospital care.",
        "link": "https://hopewarriors.org"
    }
]

gov_data = [
    {
        "name": "Ayushman Bharat Yojana",
        "location": "Pan India",
        "cancers": "All types",
        "eligibility": "Economically weaker families",
        "description": "Covers up to ₹5 lakh annually for treatment.",
        "link": "https://pmjay.gov.in"
    },
    {
        "name": "State Cancer Relief Fund",
        "location": "State-specific",
        "cancers": "Breast, Lung, Brain",
        "eligibility": "Residents meeting income limits",
        "description": "Reimburses treatment and hospitalization costs.",
        "link": "https://statehealth.gov.in"
    }
]


# ------------------------------------------------------
# FUNCTION TO RENDER A CARD  (NO F-STRING, NO FORMAT)
# ------------------------------------------------------
def render_card(d, tag_text):

    html = """
    <div class='aid-card'>
    <div class='aid-title'>""" + d["name"] + """</div>
    <div class='tag'>""" + tag_text + """</div>

    <div class='label'>📍 Location</div>
    <div>""" + d["location"] + """</div>

    <div class='label'>🎗 Supported Cancer Types</div>
    <div>""" + d["cancers"] + """</div>

    <div class='label'>📝 Eligibility</div>
    <div>""" + d["eligibility"] + """</div>

    <div class='label'>ℹ Description</div>
    <div>""" + d["description"] + """</div>

    <a href='""" + d["link"] + """' target='_blank'>
        <button class='apply-btn'>Visit Official Page ↗</button>
    </a>
    </div>
"""
    st.markdown(html, unsafe_allow_html=True)


# ------------------------------------------------------
# NGO TAB
# ------------------------------------------------------
with ngo_tab:
    for entry in ngo_data:
        render_card(entry, "NGO")


# ------------------------------------------------------
# GOVT TAB
# ------------------------------------------------------
with gov_tab:
    for entry in gov_data:
        render_card(entry, "Government")

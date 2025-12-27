import streamlit as st
from components.sidebar import sidebar
st.session_state["page_id"] = "Home"
import os
# from components.navbar import navbar

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Home | CanBridge"   ,
    page_icon="🏥",
    layout="wide"
)


sidebar()

# -------------------------------
# LOAD EXTERNAL CSS
# -------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__)) 
app_dir = os.path.dirname(current_dir)
css_path = os.path.join(app_dir, "styles", "style.css")

with open(css_path, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Background color
st.markdown("<style>.stApp { background-color: #9f1f38; }</style>", unsafe_allow_html=True)


# -------------------------------
# WELCOME + QUOTE
# -------------------------------
st.markdown("<div class='welcome'>Welcome back, <b>User</b> 👋</div>", unsafe_allow_html=True)
st.markdown("<div class='quote'>“Keep going. One day at a time, one step at a time.”</div>", unsafe_allow_html=True)

# -------------------------------
# DASHBOARD
# -------------------------------
col1, col2 = st.columns([1, 1])

# Warrior Story
with col1:
    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>🌟 Warrior Story of the Day</div>
            <div class='card-text'>
                Mira, a 42-year-old breast cancer survivor, began her journey frightened but full of hope.
                With early screening and support, she found strength again.
                <br><br>
                <i>“You are stronger than the storm you are facing.”</i>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Forum Updates
with col2:
    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>💬 Forum Updates</div>
            <div class='card-text'>
                • <b>2 new messages</b> in <b>Breast Cancer Forum</b><br>
                • Community activity rising — check latest posts
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Treatment Card
st.markdown(
    """
    <div class='card'>
        <div class='card-title'>🩺 Care Roadmap</div>
        <div class='card-text'>
            Your personalized care roadmap has been generated.<br><br>
    """,
    unsafe_allow_html=True
)

# Streamlit-safe navigation button
if st.button("➡ View your care roadmap"):
    st.switch_page("pages/5_resources.py")

st.markdown("</div></div>", unsafe_allow_html=True)

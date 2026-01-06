import streamlit as st
import requests
from config import BACKEND_URL

# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Login | CanBridge",
    page_icon="🩺",
    layout="centered"
)

# ---------------- BACKGROUND IMAGE ----------------
bg_url = "https://images.pexels.com/photos/9486838/pexels-photo-9486838.jpeg?_gl=1*1blifdf*_ga*MTgyNDA1NzE2NS4xNzYzMjc4NzA2*_ga_8JE65Q40S6*czE3NjMyNzg3MDYkbzEkZzEkdDE3NjMyODA0MDQkajQ1JGwwJGgw"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{bg_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .logo {{
        text-align: center;
        font-size: 80px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 3px 3px 0px #1A1A1A;
    }}
    .login-head {{
        color: #ffffff;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
    }}
    .stTextInput label {{
        color: #ffffff !important;
        font-weight: 900 !important;
        font-size: 20px !important;
    }}
    .stButton button {{
        background-color: #F7F7F7;
        color: #2B2B2B;
        font-size: 20px;
        font-weight: 900;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOGO ----------------
st.markdown("<div class='logo'>CanBridge</div>", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
st.markdown("<div class='login-head'>Log IN</div>", unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your Username")
password = st.text_input("Password", type="password", placeholder="Enter password")

if st.button("Login", use_container_width=True):
    if not username or not password:
        st.error("Please enter username and password")
    else:
        try:
            response = requests.post(
                f"{BACKEND_URL}/auth/login",
                json={
                    "username": username,
                    "password": password
                },
                timeout=5
            )

            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.user = response.json()
                st.switch_page("pages/2_home.py")
            else:
                st.error("Invalid username or password")

        except Exception as e:
            st.error(f"Backend not reachable: {e}")

# ---------------- LINKS ----------------
st.page_link("pages/1_register.py", label="New user? Register here")

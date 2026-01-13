import streamlit as st
import requests
from config import BACKEND_URL

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Register | CanBridge",
    page_icon="🩺",
    layout="centered"
)

# ---------------- BACKGROUND CSS ----------------
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
        color: white;
    }}
    .register-head {{
        color: white;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown("<div class='logo'>CanBridge</div>", unsafe_allow_html=True)
st.markdown("<div class='register-head'>Create Your Account</div>", unsafe_allow_html=True)

# ---------------- FORM ----------------
full_name = st.text_input("Full Name", )
email = st.text_input("Email")
phone = st.text_input("Phone Number")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Register", use_container_width=True):

    if not username or not email or not password or not full_name or not phone:
        st.error("All fields are required.")
    elif password != confirm:
        st.error("Passwords do not match.")
    else:
        try:
            response = requests.post(
                f"{BACKEND_URL}/auth/register",
                json={
                    "username": username,
                    "email": email,
                    "password": password
                },
                timeout=5
            )

            if response.status_code == 200:
                st.success("Account created successfully. Please login.")
                st.switch_page("main.py")
            else:
                st.error(response.json().get("detail", "Registration failed."))

        except Exception as e:
            st.error(f"Backend not reachable: {e}")

# ---------------- BACK TO LOGIN ----------------
st.page_link("main.py", label="Already have an account? Login here")

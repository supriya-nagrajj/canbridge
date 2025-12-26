import streamlit as st
import requests

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Login | CanBridge",
    page_icon="🩺",
    layout="centered"
)

# ---- BACKGROUND IMAGE ----
bg_url = "https://images.pexels.com/photos/9486838/pexels-photo-9486838.jpeg?_gl=1*1blifdf*_ga*MTgyNDA1NzE2NS4xNzYzMjc4NzA2*_ga_8JE65Q40S6*czE3NjMyNzg3MDYkbzEkZzEkdDE3NjMyODA0MDQkajQ1JGwwJGgw"  # replace this with your image

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
        margin-bottom: 10px;
        font-size: 80px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 3px 3px 0px #1A1A1A;
    }}

    .register-link {{
        color: #ffffff;
        text-align: center;
        margin-top: 10px;
    }}

    .register_btn button {{
    background-color: #ffffff !important;
    color: #ffd353 !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    border-radius: 10px !important;
    width: 100% !important;
    margin-top: 15px !important;
}}
 
    .login-head{{
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
        on-mouse-hover: background-color: #fff2cc;
    }}
    </style>
    """,    
    unsafe_allow_html=True
)

# ---- LOGO (TOP) ----
st.markdown("<div class='logo'>CanBridge</div>", unsafe_allow_html=True)

# ---- LOGIN CARD ----
with st.container():
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)

    st.markdown("<div class='login-head'>Log IN</div>", unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Enter your Username")
    password = st.text_input("Password", type="password", placeholder="Enter password")

    if st.button("Login", use_container_width=True):
        # TODO: Call your FastAPI auth
        st.success("Login clicked!")

    st.markdown("</div>", unsafe_allow_html=True)

# ---- REGISTER LINK ----



st.page_link("pages/1_register.py", label="New user? Register here")
st.page_link("pages/2_home.py", label="Home")
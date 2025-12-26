import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Register | CanBridge",
    page_icon="🩺",
    layout="centered"
)

# ---- BACKGROUND & THEME CSS (exact same as login) ----
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
        margin-bottom: 10px;
        font-size: 80px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 3px 3px 0px #1A1A1A;
    }}

    .register-head {{
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
        background-color: #ffffff !important;
        color: #2B2B2B !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        border-radius: 10px !important;
        width: 100% !important;
        margin-top: 20px !important;
    }}

    .login-link {{
        text-align: center;
        margin-top: 15px;
        color: #ffffff;
        font-weight: 600;
    }}

    .login-link a {{
        color: #ffd353;
        text-decoration: none;
        font-weight: 800;
        font-size: 18px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HEADER LOGO ----
st.markdown("<div class='logo'>CanBridge</div>", unsafe_allow_html=True)

# ---- REGISTRATION CARD ----
with st.container():
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)

    st.markdown("<div class='register-head'>Create Your Account</div>", unsafe_allow_html=True)

    full_name = st.text_input("Full Name", placeholder="Enter your full name")
    email = st.text_input("Email", placeholder="Enter email address")
    phone = st.text_input("Phone Number", placeholder="Enter phone number")
    username = st.text_input("Username", placeholder="Choose a username")
    password = st.text_input("Password", type="password", placeholder="Create password")
    confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")

    if st.button("Register", use_container_width=True):
        if password != confirm:
            st.error("Passwords do not match!")
        else:
            # TODO: Send data to FastAPI
            st.success("Account created successfully!")

    st.markdown("</div>", unsafe_allow_html=True)

# ---- BACK TO LOGIN ----
st.page_link("main.py", label="Already have an account? Login here")

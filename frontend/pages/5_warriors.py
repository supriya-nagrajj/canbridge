import streamlit as st
import requests
from components.sidebar import sidebar
from config import BACKEND_URL
import time
import random

st.set_page_config(page_title="Warrior Stories", page_icon="🌟", layout="wide")

if not st.session_state.get("logged_in"):
    st.switch_page("main.py")

sidebar()

user = st.session_state["user"]
username = user["username"]

# ---------------- CSS + HEART ANIMATION ----------------
st.markdown("""
<style>
.stApp { background-color:#9f1f38; }

.card {
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow:0 6px 18px rgba(0,0,0,0.18);
    color:#222;
}

.title { font-size:20px; font-weight:900; color:#9f1f38; }
.author { font-size:13px; color:#666; margin-bottom:10px; }

.heart {
    position: fixed;
    bottom: 40px;
    font-size: 26px;
    animation: floatUp 2.8s ease-out forwards;
    opacity: 0.9;
    z-index: 9999;
    pointer-events: none;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) scale(1);
        opacity: 1;
    }
    100% {
        transform: translateY(-220px) scale(1.8);
        opacity: 0;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:white;'>🌟 Warrior Stories</h1>", unsafe_allow_html=True)

# ---------------- ADD STORY ----------------
with st.expander("➕ Add Your Story"):
    with st.form("story_form"):
        title = st.text_input("Title")
        content = st.text_area("Your story", height=200)
        anon = st.checkbox("Post anonymously", value=True)
        submit = st.form_submit_button("Share")

    if submit:
        requests.post(
            f"{BACKEND_URL}/stories",
            params={
                "title": title or "Untitled",
                "content": content,
                "author": "Anonymous" if anon else username
            }
        )
        st.success("Story shared 💖")
        st.rerun()

# ---------------- FETCH STORIES ----------------
stories = []
try:
    resp = requests.get(f"{BACKEND_URL}/stories", params={"username": username})
    if resp.status_code == 200:
        stories = resp.json()
except:
    stories = []

cols = st.columns(3, gap="large")

# ---------------- INIT HEART STATE ----------------
if "show_hearts" not in st.session_state:
    st.session_state.show_hearts = False

if "heart_start" not in st.session_state:
    st.session_state.heart_start = 0

# ---------------- DISPLAY STORIES ----------------
for i, s in enumerate(stories):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <div class="title">{s['title']}</div>
            <div class="author">By {s['author']}</div>
            <p>{s['content']}</p>
        """, unsafe_allow_html=True)

        # -------- SEND LOVE --------
        if s["author"] != username:
            if st.button("💖 Send Love", key=f"love_{s['id']}"):
                res = requests.post(
                    f"{BACKEND_URL}/stories/{s['id']}/love",
                    params={"username": username}
                )

                if res.status_code == 200:
                    data = res.json()

                    if data.get("status") == "sent":
                        st.success("💖 Love sent")
                        st.session_state.show_hearts = True
                        st.session_state.heart_start = time.time()

                    elif data.get("status") == "exists":
                        st.info("💕 You’ve already sent love to this story")

                else:
                    st.error("Unable to send love right now.")

        # -------- LOVE RECEIVED (OWNER) --------
        if s["author"] == username and s.get("love_received", 0) > 0:
            st.markdown(
                f"<b>💖 You received love from {s['love_received']} warrior(s)</b>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HEART ANIMATION ----------------
if st.session_state.show_hearts:
    hearts_html = ""

    for _ in range(14):
        left = random.randint(30, 70)
        delay = random.uniform(0, 0.6)
        size = random.randint(22, 32)

        hearts_html += f"""
        <div class="heart" style="
            left:{left}%;
            font-size:{size}px;
            animation-delay:{delay}s;
        ">
            ❤️
        </div>
        """

    st.markdown(hearts_html, unsafe_allow_html=True)

    if time.time() - st.session_state.heart_start > 3:
        st.session_state.show_hearts = False

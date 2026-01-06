import os
import streamlit as st
import requests
from components.sidebar import sidebar
from config import BACKEND_URL

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="Warrior Stories | CanBridge",
    page_icon="🌟",
    layout="wide"
)

# ---------------- SESSION GUARD ----------------
if not st.session_state.get("logged_in"):
    st.switch_page("main.py")

sidebar()

# ---------------- ADMIN CHECK ----------------
IS_ADMIN = (
    st.session_state.get("user") is not None
    and st.session_state["user"].get("role") == "admin"
)

# -----------------------
# Minimal CSS (UNCHANGED)
# -----------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #9f1f38; }
    body { color: #fff; }

    .ws-header { text-align:center; color:white; margin-top:20px; }
    .ws-sub { text-align:center; color:#ffeaea; font-size:15px; margin-top:-6px; margin-bottom:18px; }

    .card {
        background:white;
        color:#9f1f38;
        border-radius:12px;
        padding:18px;
        box-shadow:0 6px 20px rgba(0,0,0,0.12);
        min-height:260px;
        display:flex;
        flex-direction:column;
        justify-content:space-between;
    }

    .tag {
        display:inline-block;
        background:#ffd353;
        color:#9f1f38;
        padding:6px 12px;
        border-radius:999px;
        font-weight:800;
        font-size:12px;
    }

    .title { font-size:18px; font-weight:900; margin-top:10px; }
    .meta { font-size:13px; color:#6b6b6b; margin-top:6px; }
    .excerpt { margin-top:12px; color:#444444; font-size:14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------
# Header
# -----------------------
st.markdown("<div class='ws-header'><h1>🌟 Warrior Stories</h1></div>", unsafe_allow_html=True)
st.markdown(
    "<div class='ws-sub'>Real journeys. Real courage. Share your story — anonymously if you prefer.</div>",
    unsafe_allow_html=True
)

# -----------------------
# Add Story Button (UNCHANGED)
# -----------------------
if "show_composer" not in st.session_state:
    st.session_state.show_composer = False

col_left, col_right = st.columns([8, 1])
with col_right:
    if st.button("Add Story"):
        st.session_state.show_composer = True

# -----------------------
# Composer (UNCHANGED)
# -----------------------
if st.session_state.show_composer:
    with st.form("composer"):
        title = st.text_input("Title")
        content = st.text_area("Your Story", height=220)
        anonymous = st.checkbox("Post anonymously", value=True)
        submitted = st.form_submit_button("✨ Share Story")

    if submitted:
        if not content.strip():
            st.error("Story cannot be empty.")
        else:
            requests.post(
                f"{BACKEND_URL}/stories",
                params={
                    "title": title or "Untitled Story",
                    "content": content,
                    "author": "Anonymous" if anonymous else st.session_state["user"]["username"]
                }
            )
            st.session_state.show_composer = False
            st.rerun()

# -----------------------
# Fetch stories
# -----------------------
stories = requests.get(f"{BACKEND_URL}/stories").json()

# -----------------------
# Display stories (3 CARDS PER ROW — RESTORED)
# -----------------------
cols_per_row = 3
for i in range(0, len(stories), cols_per_row):
    row = stories[i:i + cols_per_row]
    cols = st.columns(cols_per_row, gap="large")

    for col, story in zip(cols, row):
        with col:
            st.markdown(
                f"""
                <div class='card'>
                    <div>
                        <span class='tag'>Story</span>
                        <div class='title'>{story['title']}</div>
                        <div class='meta'>By <b>{story['author'] or "Anonymous"}</b></div>
                        <div class='excerpt'>{story['content'][:160]}...</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            c1, c2, c3 = st.columns([2, 1, 1])

            # LIKE (UNCHANGED)
            with c2:
                if st.button(f"❤️ {story['likes']}", key=f"like_{story['id']}"):
                    requests.post(f"{BACKEND_URL}/stories/{story['id']}/like")
                    st.rerun()

            # DELETE — ADMIN ONLY (THE ONLY NEW LOGIC)
            if IS_ADMIN:
                with c3:
                    if st.button("🗑", key=f"delete_{story['id']}"):
                        res = requests.delete(
                            f"{BACKEND_URL}/stories/{story['id']}",
                            headers={
                                "x-user-role": st.session_state["user"]["role"]
                            }
                        )
                        if res.status_code == 200:
                            st.rerun()
                        else:
                            st.error("Admin authorization failed")

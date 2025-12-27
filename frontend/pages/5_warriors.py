# app/pages/5_warriors.py
import streamlit as st
from datetime import datetime
from components.sidebar import sidebar

# -----------------------
# Page config
# -----------------------
st.set_page_config(page_title="Warrior Stories | CanBridge", page_icon="🌟", layout="wide")

# Render shared sidebar (safe)
try:
    sidebar()
except Exception:
    # fallback: simple sidebar if component missing
    with st.sidebar:
        st.markdown("<h3 style='color:white;'>CanBridge</h3>", unsafe_allow_html=True)

# -----------------------
# Minimal CSS for styling
# -----------------------
st.markdown(
    """
    <style>
    /* background & typography */
    .stApp { background-color: #9f1f38; }
    body { color: #fff; }

    /* header */
    .ws-header { text-align:center; color:white; margin-top:20px; }
    .ws-sub { text-align:center; color:#ffeaea; font-size:15px; margin-top:-6px; margin-bottom:18px; }

    /* top row layout */
    .top-controls { display:flex; justify-content:space-between; align-items:center; gap:12px; margin-bottom:18px; }

    /* add button (styled regular Streamlit button replacement area) */
    .add-btn {
        background:#ffd353;
        color:#9f1f38;
        padding:10px 18px;
        border-radius:12px;
        font-weight:900;
        border: none;
        box-shadow: 0 6px 18px rgba(0,0,0,0.18);
        cursor:pointer;
    }

    /* card */
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

    .title {
        font-size:18px;
        font-weight:900;
        margin-top:10px;
    }

    .meta { font-size:13px; color:#6b6b6b; margin-top:6px; }

    .excerpt { margin-top:12px; color:#444444; font-size:14px; }

    /* heart button area (small rounded square) */
    .heart-area {
        display:flex;
        justify-content:flex-end;
        align-items:center;
        gap:8px;
    }
    .heart-btn {
        background:#111827;
        color:white;
        padding:8px 10px;
        border-radius:8px;
        border:none;
        font-size:18px;
        cursor:pointer;
    }

    /* composer (centered narrow card) */
    .composer {
        max-width:860px;
        margin: 12px auto 22px auto;
        background: white;
        color: #111;
        padding:14px;
        border-radius:10px;
        box-shadow:0 6px 18px rgba(0,0,0,0.12);
    }

    /* responsive spacing */
    @media (max-width: 900px) {
        .card { min-height: 240px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------
# Header + top controls
# -----------------------
st.markdown("<div class='ws-header'><h1>🌟 Warrior Stories</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='ws-sub'>Real journeys. Real courage. Share your story — anonymously if you prefer.</div>", unsafe_allow_html=True)

# row with title left and add button right
col_left, col_right = st.columns([8, 1])
with col_left:
    st.write("")  # keeps left aligned header area intact
with col_right:
    if st.button("Add Story", key="open_composer"):
        st.session_state.show_composer = True

# -----------------------
# Session-state stories
# -----------------------
if "ws_stories" not in st.session_state:
    st.session_state.ws_stories = [
        {
            "id": 1,
            "title": "Finding Light in the Darkest Days",
            "cancer_type": "Breast Cancer",
            "author": "Anonymous",
            "date": "2025-01-14",
            "excerpt": "There was a morning I woke up and felt hope for the first time in months...",
            "text": "There was a morning I woke up and felt hope for the first time in months. It started small, but it grew…",
            "liked": False
        },
        {
            "id": 2,
            "title": "Small Steps, Big Victories",
            "cancer_type": "Brain Tumor",
            "author": "Mira S.",
            "date": "2025-01-10",
            "excerpt": "Healing didn’t happen overnight, but every small win mattered...",
            "text": "Healing didn’t happen overnight, but every small win mattered. I celebrated the tiny things because they added up.",
            "liked": False
        },
        {
            "id": 3,
            "title": "The Day I Chose Hope Again",
            "cancer_type": "Lung Cancer",
            "author": "James R.",
            "date": "2024-12-19",
            "excerpt": "At first I didn’t believe I could keep going. But then something changed...",
            "text": "At first I didn’t believe I could keep going. But then something changed and I chose hope day by day.",
            "liked": True
        }
    ]
    st.session_state._next_ws_id = 4

# ensure flag exists
if "show_composer" not in st.session_state:
    st.session_state.show_composer = False

# -----------------------
# Composer (compact, centered) - shows when show_composer True
# -----------------------
if st.session_state.show_composer:
    st.markdown("<div class='composer'>", unsafe_allow_html=True)
    with st.form("composer_form"):
        title = st.text_input("Title (optional)", placeholder="A short, hopeful title")
        cancer_type = st.selectbox("Cancer Type", ["Breast Cancer", "Brain Tumor", "Lung Cancer", "Liver Cancer", "Other"])
        text = st.text_area("Your Story (required)", height=220, placeholder="Share what happened, how you felt, and what helped.")
        anonymous = st.checkbox("Post anonymously", value=True)
        submitted = st.form_submit_button("✨ Share Story")

    if submitted:
        if not text.strip():
            st.error("Please write something before posting.")
        else:
            new = {
                "id": st.session_state._next_ws_id,
                "title": title.strip() if title.strip() else "Untitled Story",
                "cancer_type": cancer_type,
                "author": "Anonymous" if anonymous else "You",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "excerpt": (text.strip()[:150] + "...") if len(text.strip()) > 150 else text.strip(),
                "text": text.strip(),
                "liked": False
            }
            st.session_state.ws_stories.insert(0, new)
            st.session_state._next_ws_id += 1
            st.session_state.show_composer = False
            st.success("Your story was shared — thank you 🌟")
            # st.experimental_user()
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------
# Stories grid (3 columns)
# -----------------------
stories = st.session_state.ws_stories
cols_per_row = 3
for start in range(0, len(stories), cols_per_row):
    row = stories[start:start + cols_per_row]
    cols = st.columns(cols_per_row, gap="large")
    for col, story in zip(cols, row):
        with col:
            # Card
            st.markdown(
                f"""
                <div class='card'>
                    <div>
                        <span class='tag'>{story['cancer_type']}</span>
                        <div class='title'>{story['title']}</div>
                        <div class='meta'>By <b>{story['author']}</b> • {story['date']}</div>
                        <div class='excerpt'>{story['excerpt']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Place heart button under the card but aligned to the right visually
            heart_col1, heart_col2 = st.columns([3, 1])
            with heart_col1:
                st.write("")  # spacer
            with heart_col2:
                # Make heart label show filled or outline
                label = "❤️" if story.get("liked") else "🤍"
                if st.button(label, key=f"like_{story['id']}", use_container_width=False):
                    story["liked"] = not story.get("liked", False)
                    st.experimental_rerun()

# -----------------------
# Footer spacing
# -----------------------
st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)

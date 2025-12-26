# pages/4_forum.py
import streamlit as st
import os
import streamlit.components.v1 as components
from components.sidebar import sidebar
# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Support Forums | CanBridge",
    page_icon="💬",
    layout="wide"
)

# -------------------------------
# LOAD EXTERNAL CSS (optional)
# -------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
css_path = os.path.join(app_dir, "styles", "style.css")

if os.path.exists(css_path):
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR NAV
# -------------------------------
sidebar()

# -------------------------------
# PAGE HEADER
# -------------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:white; margin-top:40px;'>
        💬 Support Communities
    </h1>
    <p style='text-align:center; color:#ffeaea; font-size:18px; margin-top:-10px;'>
        Chat with others who understand your journey
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# -------------------------------
# CATEGORY BUTTONS
# -------------------------------
st.markdown("<h3 style='color:white;'>Choose a Community</h3>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4, gap="large")

breast = c1.button("🩺 Breast Cancer", use_container_width=True)
brain  = c2.button("🧠 Brain Tumor", use_container_width=True)
lung   = c3.button("🫁 Lung Cancer", use_container_width=True)
liver  = c4.button("🩸 Liver Cancer", use_container_width=True)

st.write("")

# -------------------------------
# DUMMY CHAT DATA
# -------------------------------
breast_msgs = [
    {"user": "other", "text": "Welcome everyone, feel free to share your experiences."},
    {"user": "you",   "text": "I’m new here, thank you for welcoming me."},
    {"user": "other", "text": "We’re here for you ❤️"},
]

brain_msgs = [
    {"user": "other", "text": "MRI weeks are always stressful."},
    {"user": "you",   "text": "I agree… but this group helps me feel less alone."},
]

lung_msgs = [
    {"user": "other", "text": "Breathing exercises helped me after treatment."},
    {"user": "you",   "text": "Could you share which routine you follow?"},
]

liver_msgs = [
    {"user": "other", "text": "Staying hydrated made a big difference for me."},
    {"user": "you",   "text": "Thanks, I’ll try increasing my water intake."},
]

# -------------------------------
# CHAT WINDOW RENDERER
# -------------------------------
def render_chat_window(title, messages):

    st.markdown(
        f"<h3 style='color:white; margin-bottom:10px;'>{title} Community Chat</h3>",
        unsafe_allow_html=True
    )

    # Build HTML for chat window (inside ONE HTML component)
    chat_html = """
    <div class='chat-window'>
    """

    for m in messages:
        bubble_class = "right-msg" if m["user"] == "you" else "left-msg"
        chat_html += f"""
        <div class="chat-msg {bubble_class}">
            {m['text']}
        </div>
        """

    chat_html += "</div>"

    # Render as a component so HTML does NOT break
    components.html(
        f"""
        <style>
        .chat-window {{
            background: white;
            height: 500px;
            border-radius: 14px;
            padding: 18px;
            overflow-y: auto;
            box-shadow: 0 4px 14px rgba(0,0,0,0.18);
        }}
        .chat-msg {{
            padding: 12px 18px;
            border-radius: 16px;
            max-width: 20%;
            font-size: 15px;
            line-height: 1.4;
            margin-bottom: 14px;
        }}
        .left-msg {{
            background: #f7f7f7;
            color: #333;
            border-bottom-left-radius: 4px;
            text-align: left;
        }}
        .right-msg {{
            background: #9f1f38;
            color: white;
            border-bottom-right-radius: 4px;
            margin-left: auto;
            text-align: left;
        }}
        .msg-composer {{
            background: white;
            border-radius: 12px;
            padding: 14px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.18);
        }}
        </style>
        {chat_html}
        """,
        height=550,
        scrolling=True
    )

    # Message composer below chat window
    st.write("")
    st.markdown("<div class='msg-composer'>", unsafe_allow_html=True)
    st.text_area("Type your message…", height=90)
    st.button("Send", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# SHOW THE SELECTED CHAT
# -------------------------------
if breast:
    render_chat_window("Breast Cancer", breast_msgs)

elif brain:
    render_chat_window("Brain Tumor", brain_msgs)

elif lung:
    render_chat_window("Lung Cancer", lung_msgs)

elif liver:
    render_chat_window("Liver Cancer", liver_msgs)

else:
    st.info("Select a community above to open the chat.", icon="💬")
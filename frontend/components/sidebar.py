# components/sidebar.py
import streamlit as st

def sidebar():
    """Reusable sidebar component for CanBridge."""
    
    # ---- HIDE STREAMLIT DEFAULT NAVIGATION COMPLETELY ----
    st.markdown("""
        <style>
            /* Hide Streamlit’s default sidebar page list */
            [data-testid="stSidebarNav"] {
                display: none !important;
            }

            /* Hide fallback sidebar menu containers (Streamlit internal) */
            section[data-testid="stSidebar"] .css-1d391kg,
            section[data-testid="stSidebar"] .css-1v0mbdj,
            section[data-testid="stSidebar"] ul {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # ----------- YOUR CUSTOM SIDEBAR -----------
    with st.sidebar:
        st.markdown("<h2 style='color:#9F1F38;'>CanBridge</h2>", unsafe_allow_html=True)

        # ---- MAIN NAV ----
        st.page_link("pages/2_home.py", label="🏠 Home")
        st.page_link("pages/3_prediction.py", label="🧬 Predict")
        st.page_link("pages/4_forum.py", label="💬 Forums")
        st.page_link("pages/5_warriors.py", label="🌟 Warrior Stories")
        st.page_link("pages/6_financialaid.py", label="💰 Financial Aid")
        st.page_link("pages/7_information.py", label="ℹ️ Information")
        st.page_link("pages/8_history.py", label="📜 History")
        st.markdown(
            "<hr style='border: 1px solid #ccc; margin-top:10px; margin-bottom:10px;'>",
            unsafe_allow_html=True
        )

        # Optional extra pages (disabled for now)
        # st.page_link("pages/7_faq.py", label="❓ FAQ")
        # st.page_link("pages/8_about.py", label="ℹ️ About CanBridge")

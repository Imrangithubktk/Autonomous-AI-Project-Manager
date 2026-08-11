import streamlit as st

from pages.dashboard import show_dashboard
from pages.analytics import show_analytics
from pages.recommendations import show_recommendations
from pages.chat import show_chat


st.set_page_config(
    page_title="Autonomous AI Project Manager",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🤖 AI Project Manager")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Recommendations",
        "AI Chat"
    ]
)

st.title("🤖 Autonomous AI Project Manager")

st.caption(
    "FastAPI • PostgreSQL • LangGraph • Streamlit"
)

st.markdown("---")

if page == "Dashboard":

    show_dashboard()

elif page == "Analytics":

    show_analytics()

elif page == "Recommendations":

    show_recommendations()

elif page == "AI Chat":

    show_chat()
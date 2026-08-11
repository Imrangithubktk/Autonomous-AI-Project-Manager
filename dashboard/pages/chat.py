import streamlit as st

from api_client import chat_with_ai


def show_chat():

    st.header("💬 AI Project Manager Chat")

    if "session_id" not in st.session_state:

        st.session_state.session_id = "streamlit_user"

    message = st.text_input(
        "Ask your AI Assistant"
    )

    if st.button("Send"):

        if message:

            response = chat_with_ai(
                st.session_state.session_id,
                message
            )

            st.success(
                response.get(
                    "final_response",
                    response
                )
            )
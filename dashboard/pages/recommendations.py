import streamlit as st

from api_client import get_recommendations


def show_recommendations():

    st.header("🧠 AI Recommendations")

    st.markdown(
        "AI-generated recommendations based on your current project data."
    )

    st.markdown("---")

    try:

        response = get_recommendations()

        recommendations = response.get(
            "recommendations",
            ""
        )

        if recommendations:

            lines = recommendations.split("\n")

            for line in lines:

                line = line.strip()

                if line:

                    st.success(line)

        else:

            st.info("No recommendations available.")

    except Exception as e:

        st.error(e)
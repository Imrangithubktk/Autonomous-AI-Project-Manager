import streamlit as st

from api_client import (
    get_dashboard
)


def show_dashboard():

    st.header("📊 Dashboard")

    st.markdown(
        "Real-time overview of your projects and tasks."
    )

    st.markdown("---")

    try:

        dashboard = get_dashboard()

        # -----------------------------
        # Projects
        # -----------------------------

        st.subheader("📁 Projects")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Projects",
            dashboard.get("total_projects", 0)
        )

        col2.metric(
            "Active Projects",
            dashboard.get("active_projects", 0)
        )

        col3.metric(
            "Completed Projects",
            dashboard.get("completed_projects", 0)
        )

        st.markdown("")

        # -----------------------------
        # Tasks
        # -----------------------------

        st.subheader("✅ Tasks")

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "Total Tasks",
            dashboard.get("total_tasks", 0)
        )

        col5.metric(
            "Pending Tasks",
            dashboard.get("pending_tasks", 0)
        )

        col6.metric(
            "Completed Tasks",
            dashboard.get("completed_tasks", 0)
        )

        st.markdown("---")

        st.info(
            "💡 Use the Analytics page for charts and visual reports."
        )

    except Exception as e:

        st.error(f"Dashboard Error: {e}")
import streamlit as st
import pandas as pd
import plotly.express as px

from api_client import (
    get_project_status,
    get_task_status,
    get_task_priority,
    get_deadlines
)


def show_analytics():

    st.header("📈 Project Analytics")

    st.markdown("---")

    # =====================================================
    # Project Status
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 Project Status")

        try:

            project_status = get_project_status()

            df = pd.DataFrame(
                list(project_status.items()),
                columns=["Status", "Projects"]
            )

            fig = px.bar(
                df,
                x="Status",
                y="Projects",
                text="Projects",
                title="Projects by Status"
            )

            fig.update_traces(textposition="outside")

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        except Exception as e:

            st.error(e)

    # =====================================================
    # Task Status
    # =====================================================

    with col2:

        st.subheader("📋 Task Status")

        try:

            task_status = get_task_status()

            df = pd.DataFrame(
                list(task_status.items()),
                columns=["Status", "Tasks"]
            )

            fig = px.pie(
                df,
                names="Status",
                values="Tasks",
                title="Task Status Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        except Exception as e:

            st.error(e)

    st.markdown("---")

    # =====================================================
    # Task Priority
    # =====================================================

    st.subheader("🔥 Task Priority")

    try:

        priority = get_task_priority()

        df = pd.DataFrame(
            list(priority.items()),
            columns=["Priority", "Tasks"]
        )

        fig = px.bar(
            df,
            x="Priority",
            y="Tasks",
            text="Tasks",
            title="Task Priority"
        )

        fig.update_traces(textposition="outside")

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.error(e)

    st.markdown("---")

    # =====================================================
    # Deadlines
    # =====================================================

    st.subheader("⏰ Upcoming Deadlines")

    try:

        deadlines = get_deadlines()

        if len(deadlines) == 0:

            st.success("No upcoming deadlines.")

        else:

            df = pd.DataFrame(deadlines)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

    except Exception as e:

        st.error(e)
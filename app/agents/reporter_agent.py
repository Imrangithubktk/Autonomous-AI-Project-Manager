from app.monitoring.logger import logger
from app.graph.state import ProjectState


def reporter_agent(state: ProjectState):

    logger.info("Reporter Agent Started")

    print("Reporter Agent Running...")

    try:

        analytics = state.get("analytics", {})
        recommendations = state.get("recommendations", "")

        if not analytics:

            logger.warning("Analytics data not available for report generation.")

            state["final_response"] = (
                "Unable to generate report because analytics data is missing."
            )

            logger.info("Reporter Agent Completed")

            return state


        dashboard = analytics.get("dashboard", {})


        logger.info("Generating AI Project Status Report")


        report = f"""
==============================
 AI PROJECT STATUS REPORT
==============================

Project Overview
----------------
Total Projects      : {dashboard.get('total_projects', 0)}
Active Projects     : {dashboard.get('active_projects', 0)}
Completed Projects  : {dashboard.get('completed_projects', 0)}

Task Overview
-------------
Total Tasks         : {dashboard.get('total_tasks', 0)}
Pending Tasks       : {dashboard.get('pending_tasks', 0)}
Completed Tasks     : {dashboard.get('completed_tasks', 0)}

AI Recommendations
------------------
{recommendations}

==============================
Report Generated Successfully
==============================
"""


        state["final_response"] = report


        logger.info("Report Generated Successfully")


    except Exception as e:

        logger.error(f"Reporter Agent Error: {str(e)}")
        raise


    logger.info("Reporter Agent Completed")

    return state
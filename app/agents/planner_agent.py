from app.graph.state import ProjectState


def planner_agent(state: ProjectState):

    print("Planner Agent Running...")

    user_input = state["user_input"].lower()

    if "status" in user_input:
        state["intent"] = "project_status"

    elif "pending" in user_input:
        state["intent"] = "pending_tasks"

    elif "recommend" in user_input:
        state["intent"] = "recommendations"

    else:
        state["intent"] = "general"

    print("Detected Intent:", state["intent"])

    return state
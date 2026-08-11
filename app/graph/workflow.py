from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from app.graph.state import ProjectState

from app.agents.supervisor_agent import supervisor_agent
from app.agents.analytics_agent import analytics_agent
from app.agents.recommendation_agent import recommendation_agent
from app.agents.reporter_agent import reporter_agent
from app.agents.rag_agent import rag_agent
from app.agents.general_agent import general_agent


workflow = StateGraph(ProjectState)

memory = MemorySaver()


# -----------------------
# Nodes
# -----------------------

workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("analytics", analytics_agent)
workflow.add_node("recommendation", recommendation_agent)
workflow.add_node("reporter", reporter_agent)
workflow.add_node("rag", rag_agent)
workflow.add_node("general", general_agent)


# -----------------------
# Entry Point
# -----------------------

workflow.set_entry_point("supervisor")


# -----------------------
# Routing
# -----------------------

def route_after_supervisor(state: ProjectState):

    intent = state["intent"]

    if intent == "dashboard":
        return "analytics"

    elif intent == "project_status":
        return "analytics"

    elif intent == "analytics":
        return "analytics"

    elif intent == "recommendation":
        return "analytics"

    elif intent == "rag":
        return "rag"

    elif intent == "general":
        return "general"

    else:
        return "general"


# -----------------------
# Conditional Routing
# -----------------------

workflow.add_conditional_edges(
    "supervisor",
    route_after_supervisor,
    {
        "analytics": "analytics",
        "rag": "rag",
        "general": "general",
    }
)


# -----------------------
# Analytics Flow
# -----------------------

workflow.add_edge("analytics", "recommendation")
workflow.add_edge("recommendation", "reporter")
workflow.add_edge("reporter", END)


# -----------------------
# RAG Flow
# -----------------------

workflow.add_edge("rag", END)


# -----------------------
# General Chat Flow
# -----------------------

workflow.add_edge("general", END)


# -----------------------
# Compile
# -----------------------

graph = workflow.compile(
    checkpointer=memory
)
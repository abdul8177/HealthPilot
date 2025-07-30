# app/agents/agent_graph.py

from app.agents.state import NodeState
from app.agents.medical_agent import medical_agent
from app.agents.planner_agent import planner_agent
from app.agents.nutrition_agent import nutrition_agent
from app.agents.feedback_agent import feedback_agent

from langgraph.graph import StateGraph, END
from typing import Optional

# --- Routing Function ---
def router(state: NodeState) -> str:
    user_input = state.user_input.lower()

    if any(kw in user_input for kw in ["sugar", "bp", "report", "glucose"]):
        return "medical"
    elif any(kw in user_input for kw in ["diet", "food", "meal"]):
        return "nutrition"
    elif "schedule" in user_input:
        return "planner"
    elif "feedback" in user_input:
        return "feedback"
    else:
        return "planner"  # Default fallback

# --- Graph Execution Function ---
async def run_agent_graph(user_input: str, user_id: str = "default") -> str:
    # Initialize input state
    state = NodeState(
        user_input=user_input,
        user_id=user_id,
        history=[]
    )

    # Build the graph
    workflow = StateGraph(state_schema=NodeState)

    # Add agent nodes
    workflow.add_node("medical", medical_agent)
    workflow.add_node("router", lambda state: state)
    workflow.add_node("planner", planner_agent)
    workflow.add_node("nutrition", nutrition_agent)
    workflow.add_node("feedback", feedback_agent)
    # Set entry and end
    workflow.set_entry_point("router")
    # Add router node (must also be added explicitly)

    workflow.add_conditional_edges("router", router, {
        "medical": "medical",
        "planner": "planner",
        "nutrition": "nutrition",
        "feedback": "feedback"
    })
    workflow.add_edge("medical", END)
    workflow.add_edge("planner", END)
    workflow.add_edge("nutrition", END)
    workflow.add_edge("feedback", END)
    # Compile and run
    graph = workflow.compile()
    final_state = await graph.ainvoke(state)

    return final_state.get("agent_response", "I'm not sure how to respond.")


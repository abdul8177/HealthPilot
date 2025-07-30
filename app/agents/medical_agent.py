from app.agents.state import NodeState
async def medical_agent(state: NodeState) -> NodeState:
    history = state.history or []
    user_input = state.user_input.lower()

    if "sugar" in user_input:
        response = "Your latest glucose reading is within normal range."
    else:
        response = "No medical condition detected."

    history.append({"agent": "medical", "response": response})

    return NodeState(
        user_input=state.user_input,
        user_id=state.user_id,
        history=history,
        agent_response=response
    )

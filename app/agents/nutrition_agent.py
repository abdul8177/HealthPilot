# app/agents/nutrition_agent.py

from app.agents import state
from app.agents.state import NodeState
async def nutrition_agent(state: NodeState) -> NodeState:
    user_input = state.user_input
    history = state.history or []

    # Mock nutrition logic
    if "diet" in user_input.lower() or "meal" in user_input.lower():
        suggestion = "Based on your profile, try a low-carb lunch with grilled tofu and steamed vegetables. 🥦"
    else:
        suggestion = "No dietary preferences detected in your input."

    history.append({"agent": "nutrition", "response": suggestion})

    
    return NodeState(
        user_input=state.user_input,
        user_id=state.user_id,
        history=history,
        agent_response=suggestion
    )

# app/agents/feedback_agent.py
from app.agents.state import NodeState
async def feedback_agent(state: NodeState) -> NodeState:
    user_input = state.user_input
    history = state.history or []

    if "feedback" in user_input.lower():
        processed = "Thanks for your feedback! We'll personalize your next plan accordingly."
    else:
        processed = "No feedback intent detected."

    history.append({"agent": "feedback", "response": processed})
    return NodeState(
        user_input=state.user_input,
        user_id=state.user_id,
        history=history,
        agent_response=processed
    )

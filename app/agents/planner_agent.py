# app/agents/planner_agent.py
from app.agents.state import NodeState
async def planner_agent(state: NodeState) -> NodeState:

    user_input = state.user_input.lower()
    history = state.history or []
    # Mock planner logic
    if "schedule" in user_input:
        plan = "Here is your personalized schedule for today: 🥗 Breakfast at 8am, 🏃‍♂️ Walk at 7pm."
    else:
        plan = "Planner didn’t detect a scheduling need."

    history.append({"agent": "planner", "response": plan})

    return NodeState(
        user_input=state.user_input,
        user_id=state.user_id,
        history=history,
        agent_response=plan
    )

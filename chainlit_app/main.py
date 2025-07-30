# chainlit_app/main.py

import chainlit as cl
from app.agents.agent_graph import run_agent_graph  

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content

    # You can add session-level memory or user data here
    user_id = cl.user_session.get("id", "default_user")
    if user_id is None:
        user_id = "default_user"

    # Call your LangGraph agent orchestration logic
    response = await run_agent_graph(user_input, user_id=user_id)

    # Send the agent's response to the user
    await cl.Message(content=response).send()

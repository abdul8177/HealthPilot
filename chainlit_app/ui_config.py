# chainlit_app/ui_config.py

import chainlit as cl

# Optional: Customize Chainlit UI
cl.configure(
    app_name="HealthPilot",
    app_description="Your Personalized AI Health Assistant",
    theme=cl.Theme(
        name="HealthPilot Light",
        primary_color="#6E9BD0",
        background_color="#FFFFFF",
        text_color="#333333",
    ),
    disable_default_css=False
)

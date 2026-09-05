from google.adk.agents import Agent

root_agent = Agent(
    name="my_first_agent",
    model="gemini-2.5-flash",
    description="A simple AI assistant",
    instruction="""
    You are a helpful AI assistant.
    Answer the user's questions clearly and concisely.
    """
)
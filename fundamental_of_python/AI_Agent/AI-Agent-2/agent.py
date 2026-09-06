"""
Free Online AI Chatbot Agent (Google Gemini API)
--------------------------------------------------
Uses Google's Gemini API, which has a genuinely FREE tier
(no payment info required - just a free Google account).

SETUP (one-time):
    1. Get a free API key: https://aistudio.google.com/apikey
       (Sign in with any Google account, click "Create API Key")
    2. Install the package (make sure it's up to date):
         pip install -q -U google-genai
    3. Set your API key as an environment variable.
       IMPORTANT: the variable must be named exactly GEMINI_API_KEY
       (the SDK looks for this name automatically).
         Windows (PowerShell):  $env:GEMINI_API_KEY="your-key-here"
         Mac/Linux:              export GEMINI_API_KEY="your-key-here"

       OR set it permanently (Windows):
         Win + S -> search "Environment Variables" ->
         "Edit environment variables for your account" -> New ->
         Name: GEMINI_API_KEY, Value: your-key
         (then fully restart VS Code)

To run:
    python simple_gemini_agent.py
"""

from google import genai
from google.genai import types

# ---- 1. Set up the client ----
# With no arguments, this automatically reads the GEMINI_API_KEY
# environment variable.
# We add an explicit timeout so the program fails with an error
# instead of hanging forever if the network/API doesn't respond.
client = genai.Client(
    http_options=types.HttpOptions(timeout=30000)  # 30 seconds, in milliseconds
)

MODEL_NAME = "gemini-3.6-flash"  # current fast, free-tier friendly model


def chat_with_agent(user_input, previous_interaction_id=None):
    """Send one message to Gemini, continuing the prior turn if there is one."""
    print("[debug] Sending request to Gemini...")
    interaction = client.interactions.create(
        model=MODEL_NAME,
        input=user_input,
        previous_interaction_id=previous_interaction_id
    )
    print("[debug] Response received.")
    return interaction.output_text, interaction.id


def main():
    print("=" * 60)
    print(" Free Online AI Agent (powered by Google Gemini)")
    print("=" * 60)
    print(f"Model: {MODEL_NAME}")
    print("Type 'quit' to exit.\n")

    last_interaction_id = None

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("quit", "exit"):
            print("Agent: Goodbye!")
            break

        try:
            reply, last_interaction_id = chat_with_agent(user_input, last_interaction_id)
        except Exception as e:
            print(f"\n[Error] {e}")
            print("Check that your GEMINI_API_KEY environment variable is set correctly.\n")
            continue

        print(f"Agent: {reply}\n")


if __name__ == "__main__":
    main()


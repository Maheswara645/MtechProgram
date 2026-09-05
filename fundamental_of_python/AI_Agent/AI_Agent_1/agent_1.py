def ai_agent():
    print("🤖 Simple AI Agent")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Agent: Goodbye!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Agent: Hello! How can I help you today?")

        elif "your name" in user_input:
            print("Agent: I'm a simple Python AI agent.")

        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Agent: The current time is {current_time}.")

        elif "date" in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Agent: Today's date is {current_date}.")

        else:
            print("Agent: Sorry, I don't understand that yet.")

# Run the agent
if __name__ == "__main__":
    ai_agent()
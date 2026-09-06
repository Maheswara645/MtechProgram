"""A simple local Python learning agent that needs no API key."""

import re


KNOWLEDGE_BASE = [
    (
        {"python", "learn"},
        "Start with variables, strings, numbers, conditions, loops, functions, and lists.",
    ),
    (
        {"variable"},
        "A variable stores a value. Example: name = 'Alex' and age = 20.",
    ),
    (
        {"list"},
        "A list stores multiple values in order. Example: numbers = [1, 2, 3].",
    ),
    (
        {"function"},
        "A function is reusable code. Example: def add(first, second): return first + second.",
    ),
    (
        {"loop"},
        "Use a for loop to repeat over values: for item in items: print(item).",
    ),
    (
        {"if", "condition"},
        "Use if to make a decision: if score >= 50: print('Pass').",
    ),
]


def get_response(user_input):
    """Return the best response using keyword overlap."""
    words = set(re.findall(r"[a-z]+", user_input.lower()))
    best_response = None
    best_score = 0

    for keywords, response in KNOWLEDGE_BASE:
        score = len(words & keywords)
        if score > best_score:
            best_score = score
            best_response = response

    if best_response:
        return best_response
    return (
        "I am a small local Python assistant. Ask me about variables, lists, "
        "functions, loops, conditions, or how to learn Python."
    )


def ai_agent():
    """Run the local agent until the user exits."""
    print("Local Python Learning Agent")
    print("Type 'exit' or 'quit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAgent: Goodbye!")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("Agent: Goodbye!")
            break
        if user_input:
            print(f"Agent: {get_response(user_input)}\n")


if __name__ == "__main__":
    ai_agent()

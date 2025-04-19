# main.py
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.gemini_client import configure_gemini
from src.config import AGENT_CONFIG, MAX_TURNS, MODEL_NAME, COLOR_RESET
from src.agent import AIAgent
from src.conversation import Conversation

def run_conversation():
    """Sets up and runs the multi-agent conversation."""
    try:
        configure_gemini()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred during setup: {e}")
        return

    # --- Agent Initialization ---
    agents = [AIAgent(**cfg) for cfg in AGENT_CONFIG]
    if not agents:
        print("Error: No agents defined in config.")
        return
    num_agents = len(agents)
    print(f"Initialized {num_agents} agents:")
    for agent in agents:
        print(f"- {agent.name}")

    # --- Get Topic ---
    topic = input("Please enter the topic for discussion: ")
    print(f"\n--- Starting discussion on: {topic} ---")

    # --- Initialize Shared Conversation ---
    # We can provide a general system instruction or leave it None
    initial_system_prompt = f"You are part of a multi-agent discussion group exploring the topic: {topic}. Please provide thoughtful contributions based on your designated personality when prompted."
    # Or maybe just pass the first user message as the topic:
    shared_conversation = Conversation(model_name=MODEL_NAME) # system_instruction=initial_system_prompt < Gemini might not use this well in start_chat

    # --- Conversation Loop ---
    last_message = f"The topic is: {topic}. Let's begin the discussion."
    print(f"\n{COLOR_RESET}SYSTEM: {last_message}") # Use reset for system messages

    current_turn = 0
    agent_index = 0

    try:
        while current_turn < MAX_TURNS:
            current_agent = agents[agent_index]
            print(f"\n{current_agent.color_code}--- {current_agent.name}'s turn ---")

            # Agent generates response based on its personality and the last message
            response = current_agent.generate_response(shared_conversation, last_message)

            print(f"{current_agent.name}: {response}{COLOR_RESET}") # Apply color, then reset

            last_message = response # Update last message for the next agent
            current_turn += 1
            agent_index = (agent_index + 1) % num_agents # Cycle through agents

            # Optional: Add a small delay? time.sleep(1)

    except KeyboardInterrupt:
        print("\nConversation interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred during the conversation: {e}")
    finally:
        print("\n--- End of Discussion ---")
        # Optional: Print full history
        # print("\nFull Conversation History:")
        # for entry in shared_conversation.get_gemini_history(): # Use Gemini's history
        #    role = entry.role
        #    text = "".join(part.text for part in entry.parts if hasattr(part, 'text'))
        #    print(f"[{role}]: {text}")


if __name__ == "__main__":
    run_conversation()
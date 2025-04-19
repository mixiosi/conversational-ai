# src/agent.py

# Make sure this import is present at the top
from src.conversation import Conversation

# --- Add the AIAgent class definition below ---

class AIAgent:
    """Represents an AI agent with a specific personality."""

    def __init__(self, name: str, personality: str, color_code: str = ""):
        """
        Initializes the agent.

        Args:
            name: The name of the agent (e.g., "Philosopher Bot").
            personality: A string describing the agent's behavior/persona.
            color_code: ANSI escape code for terminal color output (optional).
        """
        self.name = name
        self.personality = personality
        self.color_code = color_code # For printing

    # src/agent.py -> AIAgent.generate_response

    def generate_response(self, conversation: Conversation, current_dialogue: str) -> str:
        """
        Generates a response based on the conversation history and personality,
        using the shared conversation object. Now emphasizing direct response.
        """
        self.name = name
        self.personality = personality
        self.color_code = color_code

    def generate_response(self, conversation: Conversation, current_dialogue: str) -> str:

        # --- MODIFIED PROMPT ---
        prompt = f"""You are {self.name}, participating in a discussion. Your persona: '{self.personality}'.
The previous participant just said:
---
{current_dialogue}
---
Your task is to **directly respond to the points made in the statement above**. Acknowledge their view, critique it, or build upon it, according to your persona. Ensure your response clearly connects to what was just said before adding your own thoughts."""

        # Use the *shared* conversation object to send the message.
        response_text = conversation.send_message(prompt)

        return response_text
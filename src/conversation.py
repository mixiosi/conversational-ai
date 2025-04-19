# src/conversation.py
import google.generativeai as genai
from typing import List, Dict

class Conversation:
    """Manages the conversation history for a single Gemini chat session."""

    def __init__(self, model_name: str = "gemini-pro", system_instruction: str = None):
        """
        Initializes the conversation.

        Args:
            model_name: The name of the Gemini model to use.
            system_instruction: An optional instruction for the model's behavior (Gemini specific).
        """
        try:
            # System instruction might be supported differently; check Gemini docs
            # For basic chat, we might prepend it to the first user message or use specific API params if available
            model_args = {}
            # As of early 2024, direct system_instruction was less prominent in basic chat API
            # than in some other models/APIs. We prepend it manually if needed.
            self._system_instruction = system_instruction
            model = genai.GenerativeModel(model_name, **model_args)

            # Start chat without initial history, we'll add system prompt manually if needed
            self._chat = model.start_chat(history=[])
            self._history = [] # Keep our own parallel history for reference if needed
            print(f"Chat session started with {model_name}.")

        except Exception as e:
            print(f"Error initializing conversation: {e}")
            raise

    def add_message(self, role: str, text: str):
        """Adds a message to our internal history (optional)."""
        self._history.append({"role": role, "text": text})

    def send_message(self, message: str) -> str:
        """Sends a message to the Gemini chat session and returns the response."""
        try:
            # Prepend system instruction if it exists and this is the first "user" message conceptually
            # Note: Gemini's chat handles history roles automatically ('user', 'model')
            # If we need a strong *persistent* system prompt, API capabilities might differ.
            # For now, assume personality is injected per-turn via the prompt construction.

            response = self._chat.send_message(message)

            # Simple check for safety flags or blocks
            if not response.candidates:
                return "Error: No content generated (potentially blocked)."
            
            # Safely extract text
            full_response_text = ""
            if hasattr(response, 'parts') and response.parts:
                full_response_text = "".join(part.text for part in response.parts if hasattr(part, 'text'))
            elif response.candidates and hasattr(response.candidates[0].content, 'parts') and response.candidates[0].content.parts:
                 full_response_text = "".join(part.text for part in response.candidates[0].content.parts if hasattr(part, 'text'))
            else:
                 print(f"Warning: Could not extract text reliably from response structure: {response}")
                 # Attempt fallback if text attribute exists directly (less common for newer APIs)
                 if hasattr(response, 'text'):
                     full_response_text = response.text
                 else:
                    return "Error: Could not extract text from response."
            
            # Add user message and model response to internal history
            self.add_message("user", message) # The message sent *to* the model
            self.add_message("model", full_response_text) # The message received *from* the model

            return full_response_text

        except Exception as e:
            print(f"Error sending message: {e}")
            # Handle specific API errors if needed (e.g., rate limits, content filtering)
            return f"Error: {e}"

    def get_history(self) -> List[Dict[str, str]]:
        """Returns the internal conversation history."""
        # Gemini's chat object also has a history attribute: self._chat.history
        # Returning our own parallel history for now.
        return self._history

    def get_gemini_history(self):
        """Returns the history directly from the Gemini chat object."""
        return self._chat.history
# src/gemini_client.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

def configure_gemini():
    """Configures the Gemini API with the API key."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file.")
    genai.configure(api_key=api_key)
    print("Gemini API configured.") # Optional: for confirmation

def generate_text(prompt: str, model_name: str = "gemini-pro") -> str:
    """Generates text using the specified Gemini model."""
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        # Basic error check for safety features, etc.
        if not response.candidates:
             return "Error: No content generated. The prompt might have been blocked."
        # Handle cases where the response might not have 'text' directly
        # Accessing parts safely
        if response.parts:
             return "".join(part.text for part in response.parts if hasattr(part, 'text'))
        elif hasattr(response.candidates[0].content, 'parts') and response.candidates[0].content.parts:
             return "".join(part.text for part in response.candidates[0].content.parts if hasattr(part, 'text'))
        else:
             # Fallback or further investigation needed depending on API response structure
             print(f"Unexpected response structure: {response}")
             return "Error: Could not extract text from response."

    except Exception as e:
        print(f"An error occurred during text generation: {e}")
        # Consider more specific error handling based on potential Gemini API errors
        return f"Error: {e}"

# Example usage (optional, for testing this file directly)
if __name__ == '__main__':
    configure_gemini()
    test_prompt = "Explain the concept of emergence in complex systems in one sentence."
    result = generate_text(test_prompt)
    print("\nTest Prompt:", test_prompt)
    print("Gemini Response:", result)

*   **`main.py`**:
    *   The main entry point for the application.
    *   Handles initialization (API, agents).
    *   Prompts the user for the discussion topic.
    *   Manages the main conversation loop, orchestrating agent turns.
    *   Prints the conversation to the console.
*   **`src/config.py`**:
    *   Contains the configuration list for the AI agents (name, personality prompt, display color).
    *   Defines global settings like the maximum number of turns (`MAX_TURNS`) and the Gemini model name (`MODEL_NAME`).
*   **`src/gemini_client.py`**:
    *   Contains the `configure_gemini` function which reads the `GOOGLE_API_KEY` from the `.env` file and configures the `google.generativeai` library.
*   **`src/conversation.py`**:
    *   Defines the `Conversation` class.
    *   Initializes and holds the `ChatSession` object from the `google.generativeai` library.
    *   Provides the `send_message` method which interacts with the Gemini API, sends the user/agent prompt, and returns the model's response. Implicitly manages chat history within the `ChatSession`.
*   **`src/agent.py`**:
    *   Defines the `AIAgent` class.
    *   Each instance represents one agent with its specific name and personality.
    *   The `generate_response` method is responsible for constructing the turn-specific prompt (combining personality instructions and the previous message) before calling the shared `Conversation` object's `send_message` method.
*   **`.env`** (Manual Creation Required):
    *   Stores the `GOOGLE_API_KEY` securely. This file is ignored by Git via `.gitignore`.
*   **`requirements.txt`**:
    *   Lists the necessary Python packages (`google-generativeai`, `python-dotenv`).
*   **`.gitignore`**:
    *   Tells Git which files/directories to ignore (e.g., `.venv`, `.env`, `__pycache__`).

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mixiosi/conversational-ai.git
    cd conversational-ai
    ```
2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv .venv
    # Windows
    # .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create `.env` file:**
    *   In the project's root directory (`conversational-ai/`), create a file named `.env`.
    *   Add your Google Gemini API key to it:
        ```
        GOOGLE_API_KEY=YOUR_API_KEY_HERE
        ```

## How to Run

1.  Ensure your virtual environment is activated.
2.  Run the main script from the project's root directory:
    ```bash
    python main.py
    ```
3.  Enter a topic when prompted.

## Configuration

*   Agent personalities, the number of agents, maximum discussion turns, and the specific Gemini model used can be adjusted in `src/config.py`.

## Current Status

The basic framework for multi-agent conversation is functional. Ongoing efforts are focused on refining the prompts within `src/agent.py` to improve the agents' ability to directly respond to each other and maintain a more coherent and engaging discussion.

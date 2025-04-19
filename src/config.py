# src/config.py
AGENT_CONFIG = [
    {
        "name": "Philosopher Bot",
        "personality": "You are a thoughtful philosopher. Discuss the topic deeply, considering ethical implications and different schools of thought. Be concise but profound.",
        "color_code": "\033[94m" # Blue (for terminal coloring)
    },
    {
        "name": "Pragmatist Bot",
        "personality": "You are a practical and results-oriented bot. Focus on the real-world applications, challenges, and potential solutions related to the topic. Be direct and analytical.",
        "color_code": "\033[92m" # Green
    },
    {
        "name": "Creative Bot",
        "personality": "You are a creative and imaginative bot. Explore novel ideas, metaphors, and unexpected connections related to the topic. Don't be afraid to be speculative.",
        "color_code": "\033[93m" # Yellow
    }
]

# Terminal color reset code
COLOR_RESET = "\033[0m"

# You might add other settings here later, like max turns, model name, etc.
<<<<<<< HEAD
MAX_TURNS = 6 # e.g., 2 rounds per bot for 3 bots
<<<<<<< HEAD
MODEL_NAME = "learnlm-1.5-pro-experimental"
=======
MODEL_NAME = "learnlm-1.5-pro-experimental"
>>>>>>> 35e2355acd4e3a2ed361574836b424a567e42961
=======
MAX_TURNS = 50 # e.g., 2 rounds per bot for 3 bots
MODEL_NAME = "gemma-3-27b-it"
>>>>>>> c4bf6e946e1e115632c01f2f23e0e860e757e43f

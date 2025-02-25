from dotenv import load_dotenv, dotenv_values
import os

# Load dotenv
success = load_dotenv()
print(f"Load dotenv success: {success}")

# Print loaded values
print(dotenv_values())  # Should display variables from .env

# Try accessing a specific variable
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")
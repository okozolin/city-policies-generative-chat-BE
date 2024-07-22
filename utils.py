import os
from openai import OpenAI
from dotenv import load_dotenv  # Import python-dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client
api_key = os.getenv("GROQ_API_KEY")

if not api_key or api_key == "your_groq_api_key_here":
    print("Error: GROQ_API_KEY is not set or is still the default value.")
    print("Please get an API key from https://console.groq.com and put it in the .env file.")
    exit(1)

client = Groq(api_key=api_key)

def test_api_call():
    try:
        print("Testing Groq API call...")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Explain the importance of fast language models in one sentence.",
                }
            ],
            model="llama-3.1-8b-instant",
        )
        print("\nSuccess! Received response from Groq API:")
        print("-" * 50)
        print(chat_completion.choices[0].message.content)
        print("-" * 50)
    except Exception as e:
        print(f"\nAPI Call Failed: {e}")

if __name__ == "__main__":
    test_api_call()

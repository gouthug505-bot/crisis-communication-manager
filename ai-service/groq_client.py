import os
import time
import json
import logging
from dotenv import load_dotenv
from groq import Groq

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class GroqClient:
    def __init__(self, model="llama-3.1-8b-instant", max_retries=3):
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key or api_key == "your_groq_api_key_here":
            logger.error("GROQ_API_KEY is missing or invalid.")
            raise ValueError("Invalid GROQ_API_KEY")
        
        self.client = Groq(api_key=api_key)
        self.model = model
        self.max_retries = max_retries

    def generate_json(self, prompt, system_prompt="You are a helpful assistant. Please output in valid JSON format."):
        """
        Calls the Groq API and expects a JSON response.
        Implements 3-retry with exponential backoff and error logging.
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        retries = 0
        backoff_time = 1

        while retries <= self.max_retries:
            try:
                logger.info(f"Attempting API call (Attempt {retries + 1}/{self.max_retries + 1})")
                chat_completion = self.client.chat.completions.create(
                    messages=messages,
                    model=self.model,
                    response_format={"type": "json_object"}
                )
                
                content = chat_completion.choices[0].message.content
                logger.info("API call successful. Parsing JSON.")
                
                # Try to parse the JSON response
                parsed_json = json.loads(content)
                return parsed_json
                
            except Exception as e:
                logger.error(f"API call or JSON parsing failed: {e}")
                retries += 1
                
                if retries <= self.max_retries:
                    logger.info(f"Retrying in {backoff_time} seconds...")
                    time.sleep(backoff_time)
                    backoff_time *= 2  # Exponential backoff
                else:
                    logger.error("Max retries reached. Failing operation.")
                    return None

    def generate_recommendation(self, user_profile, context):
        """
        Generates a personalized AI recommendation based on user profile and context.
        """
        system_prompt = (
            "You are an expert AI recommendation engine. Based on the user profile and context provided, "
            "generate 3 highly personalized, actionable recommendations. "
            "Your output must be strictly in JSON format with a 'recommendations' array containing objects "
            "with 'title', 'description', and 'confidence_score' keys."
        )
        prompt = f"User Profile: {user_profile}\nContext: {context}"
        return self.generate_json(prompt, system_prompt)

    def generate_report(self, data_summary, topic):
        """
        Generates a structured report based on a data summary.
        """
        system_prompt = (
            "You are a professional business analyst. Given the data summary and topic, "
            "generate a concise, structured report. Your output must be strictly in JSON format "
            "with 'title', 'executive_summary', 'key_findings' (array of strings), and 'conclusion' keys."
        )
        prompt = f"Topic: {topic}\nData Summary: {data_summary}"
        return self.generate_json(prompt, system_prompt)

if __name__ == "__main__":
    # Test the GroqClient
    client = GroqClient()
    prompt = "Give me 2 examples of fast animals in JSON format with keys 'animal1' and 'animal2'."
    result = client.generate_json(prompt)
    
    if result:
        print("\nFinal Result:")
        print(json.dumps(result, indent=2))
    else:
        print("\nFailed to get a valid response.")

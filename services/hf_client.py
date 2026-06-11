import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL") or "https://router.huggingface.co/v1"

MODEL_NAME = os.getenv("MODEL_NAME") or "Qwen/Qwen2.5-72B-Instruct"

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError(
        "HF_TOKEN not found in .env file"
    )

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def ask_llm(system_prompt, user_prompt):

    try:

        print("\nSending request to HF...")

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.7,
            max_tokens=3000
        )

        print("HF Response Received!")

        return response.choices[0].message.content

    except Exception as e:

        print(f"\nHF ERROR: {e}")

        return None
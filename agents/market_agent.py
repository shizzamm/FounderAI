import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are a senior market research analyst.
"""


def run(idea_data):

    prompt = f"""
Return ONLY valid JSON.

Idea:

{json.dumps(idea_data, indent=2)}

Schema:

{{
    "competitors": [],
    "market_gap": "",
    "opportunities": [],
    "risks": []
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nMARKET RESPONSE:")
    print(response)

    result = clean_json_response(response)

    update_memory(
        "market",
        result
    )

    return result
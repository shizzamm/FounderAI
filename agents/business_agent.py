import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are a McKinsey business consultant.
"""


def run(idea_data, market_data):

    prompt = f"""
Return ONLY valid JSON.

Idea:

{json.dumps(idea_data, indent=2)}

Market:

{json.dumps(market_data, indent=2)}

Schema:

{{
    "revenue_model":"",
    "pricing_strategy":"",
    "customer_acquisition":"",
    "growth_strategy":""
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nBUSINESS RESPONSE:")
    print(response)

    result = clean_json_response(response)

    update_memory(
        "business",
        result
    )

    return result
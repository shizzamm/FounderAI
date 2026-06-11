import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are a Senior Product Manager at Google.
"""


def run(
    idea_data,
    market_data,
    business_data
):

    prompt = f"""
Return ONLY valid JSON.

Idea:

{json.dumps(idea_data, indent=2)}

Market:

{json.dumps(market_data, indent=2)}

Business:

{json.dumps(business_data, indent=2)}

Schema:

{{
    "mvp_features": [],
    "future_features": [],
    "pages": [],
    "tech_stack": {{
        "frontend":"",
        "backend":"",
        "database":""
    }}
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nPM RESPONSE:")
    print(response)

    result = clean_json_response(response)

    update_memory(
        "product",
        result
    )

    return result
import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are an elite startup critic.

Your job is to evaluate startup ideas brutally honestly.

Score the startup from 1-10.

Identify strengths, weaknesses and improvements.

Return ONLY valid JSON.
"""


def run(
    idea_data,
    market_data,
    business_data,
    product_data,
    cto_data,
    investor_data
):

    prompt = f"""
Analyze this startup.

Idea:

{json.dumps(idea_data, indent=2)}

Market:

{json.dumps(market_data, indent=2)}

Business:

{json.dumps(business_data, indent=2)}

Product:

{json.dumps(product_data, indent=2)}

Technical:

{json.dumps(cto_data, indent=2)}

Investor:

{json.dumps(investor_data, indent=2)}

Schema:

{{
    "overall_score": 0,
    "strengths": [],
    "weaknesses": [],
    "improvements": [],
    "final_verdict": ""
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nCRITIC RESPONSE:")
    print(response)

    result = clean_json_response(
        response
    )

    update_memory(
        "critic",
        result
    )

    return result
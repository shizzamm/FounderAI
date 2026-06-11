import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are a venture capitalist and startup investor.

Analyze startups from an investor perspective.
"""


def run(
    idea_data,
    market_data,
    business_data,
    product_data,
    cto_data
):

    prompt = f"""
Return ONLY valid JSON.

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

Schema:

{{
    "investment_score":"",
    "funding_required":"",
    "revenue_projection":"",
    "investor_risks":[],
    "pitch_summary":""
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nINVESTOR RESPONSE:")
    print(response)

    result = clean_json_response(
        response
    )

    update_memory(
        "investor",
        result
    )

    return result
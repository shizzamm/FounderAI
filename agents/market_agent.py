import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from services.search_service import search_competitors

from memory.memory_manager import update_memory


SYSTEM_PROMPT = """
You are a senior market research analyst.

Return ONLY valid JSON.

Do NOT return markdown.

Do NOT return explanations.
"""


def run(idea_data):

    competitors = search_competitors(
        idea_data["startup_name"]
    )

    prompt = f"""
Return ONLY valid JSON.

Idea:

{json.dumps(idea_data, indent=2)}

Competitors Found:

{json.dumps(competitors, indent=2)}

Analyze the market.

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

    result = clean_json_response(
        response
    )

    update_memory(
        "market",
        result
    )

    return result
import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory


SYSTEM_PROMPT = """
You are a McKinsey business consultant.

Always return exactly ONE valid JSON object.

Never return markdown.

Never explain.

Never repeat the input.

Never output multiple JSON objects.
"""


def run(idea_data, market_data):

    prompt = f"""
Use the following data ONLY as context.

DO NOT repeat it.

Return ONLY ONE valid JSON object matching the schema.

Idea:

{json.dumps(idea_data, indent=2)}

Market:

{json.dumps(market_data, indent=2)}

Schema:

{{
    \"revenue_model\":\"\",
    \"pricing_strategy\":\"\",
    \"customer_acquisition\":\"\",
    \"growth_strategy\":\"\"
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
import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are a Staff Software Engineer and CTO.
Design scalable software systems.
"""


def run(product_data):

    prompt = f"""
Return ONLY valid JSON.

Keep responses concise.

Product Data:

{json.dumps(product_data, indent=2)}

Schema:

{{
    "architecture":"",
    "main_services":[],
    "database_tables":[],
    "deployment_plan":""
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nCTO RESPONSE:")
    print(response)

    result = clean_json_response(
        response
    )

    update_memory(
        "cto",
        result
    )

    return result
import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are a Staff Software Engineer and CTO.

Design scalable software systems.

IMPORTANT:
Return ONLY valid JSON.
Do NOT return markdown.
Do NOT add explanations.
Do NOT create dictionaries inside arrays.
"""


def run(product_data):

    prompt = f"""
Return ONLY valid JSON.

Keep responses concise.

Product Data:

{json.dumps(product_data, indent=2)}

Schema:

{{
    \"architecture\":\"\",
    \"main_services\":[
        \"service1\",
        \"service2\"
    ],
    \"database_tables\":[
        \"table1\",
        \"table2\"
    ],
    \"deployment_plan\":\"\"
}}

Example:

{{
    \"architecture\":\"Microservices\",
    \"main_services\":[
        \"User Service\",
        \"Payment Service\",
        \"Notification Service\"
    ],
    \"database_tables\":[
        \"users\",
        \"payments\",
        \"notifications\"
    ],
    \"deployment_plan\":\"Deploy using Docker on AWS\"
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nCTO RESPONSE:")
    print(response)

    result = clean_json_response(response)

    update_memory(
        "cto",
        result
    )

    return result
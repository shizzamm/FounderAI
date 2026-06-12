import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory


SYSTEM_PROMPT = """
You are a startup evaluator.

Compare two startup versions.

Return ONLY valid JSON.
"""


def run(
    original_idea,
    improved_idea,
    critic_data
):

    prompt = f"""
Original Startup:

{json.dumps(original_idea, indent=2)}

Improved Startup:

{json.dumps(improved_idea, indent=2)}

Original Critic Feedback:

{json.dumps(critic_data, indent=2)}

Return ONLY JSON.

Schema:

{{
    "original_score": 0,
    "improved_score": 0,
    "improvement": 0,
    "summary": ""
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nCOMPARISON RESPONSE:")
    print(response)

    result = clean_json_response(
        response
    )

    update_memory(
        "comparison",
        result
    )

    return result
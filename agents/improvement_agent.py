import json

from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory


SYSTEM_PROMPT = """
You are a world-class startup strategist.

Your job is to improve startup ideas based on critic feedback.

Return ONLY valid JSON.
"""


def run(
    idea_data,
    critic_data
):

    prompt = f"""
Startup:

{json.dumps(idea_data, indent=2)}

Critic Feedback:

{json.dumps(critic_data, indent=2)}

Improve the startup.

Return ONLY valid JSON.

Schema:

{{
    "startup_name":"",
    "problem":"",
    "solution":"",
    "target_audience":"",
    "unique_value_proposition":"",
    "improvements_applied":[]
}}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nIMPROVEMENT RESPONSE:")
    print(response)

    result = clean_json_response(
        response
    )

    update_memory(
        "improved_idea",
        result
    )

    return result
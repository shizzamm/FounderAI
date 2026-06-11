from services.hf_client import ask_llm
from services.json_utils import clean_json_response
from memory.memory_manager import update_memory

SYSTEM_PROMPT = """
You are a Silicon Valley startup strategist.
"""


def run(startup_idea):

    prompt = f"""
Return ONLY valid JSON.

{{
    "startup_name":"",
    "problem":"",
    "solution":"",
    "target_audience":"",
    "unique_value_proposition":""
}}

Startup Idea:

{startup_idea}
"""

    response = ask_llm(
        SYSTEM_PROMPT,
        prompt
    )

    print("\nIDEA RESPONSE:")
    print(response)

    result = clean_json_response(response)

    update_memory(
        "idea",
        result
    )

    return result
import json
import re


def clean_json_response(response):

    if response is None:
        raise ValueError(
            "Model returned None"
        )

    response = response.strip()

    response = re.sub(
        r"^```json",
        "",
        response,
        flags=re.IGNORECASE
    )

    response = re.sub(
        r"^```",
        "",
        response
    )

    response = re.sub(
        r"```$",
        "",
        response
    )

    response = response.strip()

    try:
        return json.loads(response)

    except Exception:

        match = re.search(
            r"\{.*\}",
            response,
            re.DOTALL
        )

        if match:

            json_text = match.group()

            return json.loads(
                json_text
            )

        raise
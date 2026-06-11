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

        start = response.find("{")
        end = response.rfind("}")

        if start != -1 and end != -1:

            json_text = response[start:end + 1]

            return json.loads(json_text)

        raise ValueError(
            "Could not extract valid JSON"
        )
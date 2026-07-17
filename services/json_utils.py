import json
import re


def clean_json_response(response):

    if response is None:
        raise ValueError(
            "Model returned None"
        )

    response = response.strip()

    # Remove markdown code blocks
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

    # Detect multiple JSON objects
    if "}\n{" in response or "}\r\n{" in response:

        objects = re.findall(
            r"\{.*?\}(?=\s*\{|$)",
            response,
            re.DOTALL
        )

        if objects:
            response = objects[-1]

    try:
        return json.loads(response)

    except Exception:

        # Extract largest JSON object
        matches = re.findall(
            r"\{.*\}",
            response,
            re.DOTALL
        )

        if matches:

            largest = max(matches, key=len)

            return json.loads(largest)

        raise
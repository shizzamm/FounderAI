import json
import os

MEMORY_FILE = "memory/context.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read().strip()

            if not content:
                return {}

            return json.loads(content)

    except Exception:

        return {}


def save_memory(data):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def update_memory(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)
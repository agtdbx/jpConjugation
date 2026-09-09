import time
import requests


def _get_jisho_parts_of_speech(keyword: str) -> list[str]:
    time.sleep(0.5)
    try:
        response = requests.get(f"https://jisho.org/api/v1/search/words?keyword={keyword}", timeout=5)
        response.raise_for_status()

        data = response.json().get("data", [])

        if not data or not data[0].get("senses"):
            return []

        return data[0]["senses"][0].get("parts_of_speech", [])

    except requests.RequestException:
        return []


def get_verb_type_from_jisho(verb: str) -> str:
    types = _get_jisho_parts_of_speech(verb)
    if len(types) == 0:
        return "ERROR"

    for type in types:
        if "ichidan" in type.lower():
            return "ichidan"
        if "godan" in type.lower():
            return "godan"

    return "exception"


def get_adjective_type_from_jisho(adjective: str) -> str:
    types = _get_jisho_parts_of_speech(adjective)
    if len(types) == 0:
        return "ERROR"

    for type in types:
        if "i-adjective" in type.lower():
            return "i"
        if "na-adjective" in type.lower():
            return "na"

    return "nope"

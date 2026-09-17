from jpconjugation.models import Adjective
from jpconjugation.conjugation.adjectives.rules import build_rules


def get_past_rules(adjective: Adjective) -> dict:
    return build_rules(
        adjective=adjective,
        i_rules={
            "ip": "enlève 'i' au radical et ajoute 'katta'",
            "fp": "enlève 'i' au radical et ajoute 'katta desu'",
            "in": "enlève 'i' au radical et ajoute 'kunakatta'",
            "fn": "enlève 'i' au radical et ajoute 'kunakatta desu'",
        },
        na_rules={
            "ip": "ajoute ' datta'",
            "fp": "ajoute ' deshita'",
            "in": "ajoute ' janakatta'",
            "fn": "ajoute ' ja arimasen deshita'",
        }
    )


def get_past_forms(adjective: Adjective) -> dict:
    if adjective.type == "i":
        return _get_past_i_forms(adjective)
    elif adjective.type == "na":
        return _get_past_na_forms(adjective)
    else:
        return {}


def _get_past_i_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.stem + "katta",
        "fp" : f"{adjective.stem}katta desu",
        "in" : adjective.stem + "kunakatta",
        "fn" : f"{adjective.stem}kunakatta desu",
    }


def _get_past_na_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji + " datta",
        "fp" : adjective.romaji + " deshita",
        "in" : adjective.romaji + " janakatta",
        "fn" : adjective.romaji + " ja arimasen deshita",
    }

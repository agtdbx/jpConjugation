from jpconjugation.models import Adjective
from jpconjugation.conjugation.adjectives.rules import build_core_rules


def get_present_rules(adjective: Adjective) -> dict:
    return build_core_rules(
        adjective=adjective,
        i_rules={
            "ip": "prend la forme du dictionnaire",
            "fp": "ajoute ' desu'",
            "in": "enlève 'i' au radical et ajoute 'kunai'",
            "fn": "enlève 'i' au radical et ajoute 'kunai desu'",
        },
        na_rules={
            "ip": "ajoute ' da'",
            "fp": "ajoute ' desu'",
            "in": "ajoute ' janai'",
            "fn": "ajoute ' ja arimasen'",
        }
    )


def get_present_forms(adjective: Adjective) -> dict:
    if adjective.type == "i":
        return _get_present_i_forms(adjective)
    elif adjective.type == "na":
        return _get_present_na_forms(adjective)
    else:
        return {}


def _get_present_i_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji,
        "fp" : f"{adjective.romaji} desu",
        "in" : adjective.stem + "kunai",
        "fn" : adjective.stem + "kunai desu",
    }


def _get_present_na_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji + " da",
        "fp" : adjective.romaji + " desu",
        "in" : adjective.romaji + " janai",
        "fn" : adjective.romaji + " ja arimasen",
    }

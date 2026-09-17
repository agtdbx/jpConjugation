from jpconjugation.models import Adjective
from jpconjugation.conjugation.adjectives.rules import build_core_rules


def get_adverbial_rules(adjective: Adjective) -> dict:
    return build_core_rules(
        adjective=adjective,
        i_rules={
            "ip": "enlève 'i' au radical et ajoute 'ku'",
        },
        na_rules={
            "ip": "ajoute ' ni'",
        }
    )


def get_adverbial_forms(adjective: Adjective) -> dict:
    if adjective.type == "i":
        return _get_adverbial_i_forms(adjective)
    elif adjective.type == "na":
        return _get_adverbial_na_forms(adjective)
    else:
        return {}


def _get_adverbial_i_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.stem + "ku"
    }


def _get_adverbial_na_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji + " ni"
    }

from jpconjugation.models import Adjective
from jpconjugation.conjugation.adjectives.rules import build_rules


def get_connective_rules(adjective: Adjective) -> dict:
    return build_rules(
        adjective=adjective,
        i_rules={
            "ip": "enlève 'i' au radical et ajoute 'kute'",
            "in": "enlève 'i' au radical et ajoute 'kunakute'",
        },
        na_rules={
            "ip": "ajoute ' de'",
            "in": "ajoute ' janakute'",
        }
    )


def get_connective_forms(adjective: Adjective) -> dict:
    if adjective.type == "i":
        return _get_connective_i_forms(adjective)
    elif adjective.type == "na":
        return _get_connective_na_forms(adjective)
    else:
        return {}


def _get_connective_i_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.stem + "kute",
        "in" : adjective.stem + "kunakute",
    }


def _get_connective_na_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji + " de",
        "in" : adjective.romaji + " janakute",
    }

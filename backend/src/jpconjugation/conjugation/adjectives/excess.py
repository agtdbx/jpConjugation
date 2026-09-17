from jpconjugation.models import Adjective
from jpconjugation.define import ADJECTIVES_EXCEPTIONS
from jpconjugation.conjugation.adjectives.rules import build_rules


def get_excess_rules(adjective: Adjective) -> dict:
    if adjective.romaji in ADJECTIVES_EXCEPTIONS.keys():
        ending = "sasugiru"
    else:
        ending = "sugiru"

    return build_rules(
        adjective=adjective,
        i_rules={
            "ip": f"enlève 'i' au radical et ajoute '{ending}'",
        },
        na_rules={
            "ip": f"ajoute '{ending}'",
        }
    )


def get_excess_forms(adjective: Adjective) -> dict:
    if adjective.type == "i":
        return _get_excess_i_forms(adjective)
    elif adjective.type == "na":
        return _get_excess_na_forms(adjective)
    else:
        return {}


def _get_excess_i_forms(adjective: Adjective) -> dict:
    if adjective.romaji in ADJECTIVES_EXCEPTIONS.keys():
        return {
            "ip" : adjective.stem + "sasugiru"
        }
    return {
        "ip" : adjective.stem + "sugiru"
    }


def _get_excess_na_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji + "sugiru"
    }

from jpconjugation.models import Adjective
from jpconjugation.conjugation.adjectives.rules import build_rules

###########################################################################################
# BA
###########################################################################################

def get_conditional_ba_rules(adjective: Adjective) -> dict:
    return build_rules(
        adjective=adjective,
        i_rules={
            "ip": "enlève 'i' au radical et ajoute 'kereba'",
            "in": "enlève 'i' au radical et ajoute 'kunakereba'",
        },
        na_rules={
            "ip": "ajoute ' nara'",
            "in": "ajoute ' janai nara'",
        }
    )


def get_conditional_ba_forms(adjective: Adjective) -> dict:
    if adjective.type == "i":
        return _get_conditional_ba_i_forms(adjective)
    elif adjective.type == "na":
        return _get_conditional_ba_na_forms(adjective)
    else:
        return {}


def _get_conditional_ba_i_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.stem + "kereba",
        "in" : adjective.stem + "kunakereba",
    }


def _get_conditional_ba_na_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji + " nara",
        "in" : adjective.romaji + " janai nara",
    }


###########################################################################################
# TARA
###########################################################################################

def get_conditional_tara_rules(adjective: Adjective) -> dict:
    return build_rules(
        adjective=adjective,
        i_rules={
            "ip": "enlève 'i' au radical et ajoute 'kattara'",
            "in": "enlève 'i' au radical et ajoute 'kunakattara'",
        },
        na_rules={
            "ip": "ajoute ' dattara'",
            "in": "ajoute ' ja nakattara'",
        }
    )


def get_conditional_tara_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "i":
        return _get_conditional_tara_i_forms(adjective)
    elif type == "na":
        return _get_conditional_tara_na_forms(adjective)
    else:
        return {}


def _get_conditional_tara_i_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.stem + "kattara",
        "in" : adjective.stem + "kunakattara",
    }


def _get_conditional_tara_na_forms(adjective: Adjective) -> dict:
    return {
        "ip" : adjective.romaji + " dattara",
        "in" : adjective.romaji + " ja nakattara",
    }

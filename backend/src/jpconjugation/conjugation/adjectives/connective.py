from jpconjugation.models import Adjective
from jpconjugation.define import ADJECTIVES_EXCEPTIONS

def get_connective_rules(adjective: Adjective) -> dict:
    if adjective.type == "i":
        exception = ""
        if adjective.romaji in ADJECTIVES_EXCEPTIONS:
            exception = f" /!\\Radical '{adjective.stem}'/!\\"
        return {
            "ip": f"Pour un i adjectif,enlève 'i' au radical et ajoute 'kute'.{exception}",
            "in": f"Pour un i adjectif,enlève 'i' au radical et ajoute 'kunakute'.{exception}",
        }
    elif adjective.type == "na":
        return {
            "ip": "Pour un na adjectif,ajoute ' de'",
            "in": "Pour un na adjectif,ajoute ' janakute'",
        }
    return {}


def get_connective_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "i":
        return _get_connective_i_forms(adjective)
    elif type == "na":
        return _get_connective_na_forms(adjective)
    else:
        return {}


def _get_connective_i_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.stem + "kute"
    # Informel Négatif
    form_in = adjective.stem + "kunakute"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_connective_na_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.romaji + " de"
    # Informel Négatif
    form_in = adjective.romaji + " janakute"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }

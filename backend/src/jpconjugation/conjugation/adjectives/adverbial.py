from jpconjugation.models import Adjective
from jpconjugation.define import ADJECTIVES_EXCEPTIONS

def get_adverbial_rules(adjective: Adjective) -> dict:
    if adjective.type == "i":
        exception = ""
        if adjective.romaji in ADJECTIVES_EXCEPTIONS:
            exception = f" /!\\Radical '{adjective.stem}'/!\\"
        return {
            "ip": f"Pour un i adjectif, on enlève 'i' au radical et on ajoute 'ku'.{exception}",
        }
    elif adjective.type == "na":
        return {
            "ip": "Pour un na adjectif, on ajoute ' ni'",
        }
    return {}

def get_adverbial_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "i":
        return _get_adverbial_i_forms(adjective)
    elif type == "na":
        return _get_adverbial_na_forms(adjective)
    else:
        return {}


def _get_adverbial_i_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.stem + "ku"

    return {
        "ip" : form_ip
    }


def _get_adverbial_na_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.romaji + " ni"

    return {
        "ip" : form_ip
    }
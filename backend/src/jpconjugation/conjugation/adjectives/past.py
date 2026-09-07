from jpconjugation.models import Adjective
from jpconjugation.define import ADJECTIVES_EXCEPTIONS

def get_past_rules(adjective: Adjective) -> dict:
    if adjective.type == "i":
        exception = ""
        if adjective.romaji in ADJECTIVES_EXCEPTIONS:
            exception = f" /!\\Radical '{adjective.stem}'/!\\"
        return {
            "ip": f"Pour un i adjectif, on enlève 'i' au radical et on ajoute 'katta'.{exception}",
            "fp": f"Pour un i adjectif, on enlève 'i' au radical et on ajoute 'katta desu'.{exception}",
            "in": f"Pour un i adjectif, on enlève 'i' au radical et on ajoute 'kunakatta'.{exception}",
            "fn": f"Pour un i adjectif, on enlève 'i' au radical et on ajoute 'kunakatta desu'.{exception}",
        }
    elif adjective.type == "na":
        return {
            "ip": "Pour un na adjectif, on ajoute ' datta'",
            "fp": "Pour un na adjectif, on ajoute ' deshita'",
            "in": "Pour un na adjectif, on ajoute ' janakatta'",
            "fn": "Pour un na adjectif, on ajoute ' ja arimasen deshita'",
        }
    return {}


def get_past_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "i":
        return _get_past_i_forms(adjective)
    elif type == "na":
        return _get_past_na_forms(adjective)
    else:
        return {}


def _get_past_i_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.stem + "katta"
    # Informel Négatif
    form_in = adjective.stem + "kunakatta"

    return {
        "ip" : form_ip,
        "fp" : f"{form_ip} desu",
        "in" : form_in,
        "fn" : f"{form_in} desu",
    }


def _get_past_na_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.romaji + " datta"
    # Formel Positif
    form_fp = adjective.romaji + " deshita"
    # Informel Négatif
    form_in = adjective.romaji + " janakatta"
    # Formel Négatif
    form_fn = adjective.romaji + " ja arimasen deshita"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }
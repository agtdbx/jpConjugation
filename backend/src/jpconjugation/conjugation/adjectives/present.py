from jpconjugation.models import Adjective
from jpconjugation.define import ADJECTIVES_EXCEPTIONS

def get_present_rules(adjective: Adjective) -> dict:
    if adjective.type == "i":
        exception = ""
        if adjective.romaji in ADJECTIVES_EXCEPTIONS:
            exception = f" /!\\Radical '{adjective.stem}'/!\\"
        return {
            "ip": f"Forme du dictionnaire.{exception}",
            "fp": f"Pour un i adjectif, ajoute ' desu'.{exception}",
            "in": f"Pour un i adjectif, enlève 'i' au radical et ajoute 'kunai'.{exception}",
            "fn": f"Pour un i adjectif, enlève 'i' au radical et ajoute 'kunai desu'.{exception}",
        }
    elif adjective.type == "na":
        return {
            "ip": "Pour un na adjectif, ajoute ' da'",
            "fp": "Pour un na adjectif, ajoute ' desu'",
            "in": "Pour un na adjectif, ajoute ' janai'",
            "fn": "Pour un na adjectif, ajoute ' ja arimasen'",
        }
    return {}


def get_present_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "i":
        return _get_present_i_forms(adjective)
    elif type == "na":
        return _get_present_na_forms(adjective)
    else:
        return {}


def _get_present_i_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.romaji
    # Informel Négatif
    form_in = adjective.stem + "kunai"

    return {
        "ip" : form_ip,
        "fp" : f"{form_ip} desu",
        "in" : form_in,
        "fn" : f"{form_in} desu",
    }


def _get_present_na_forms(adjective: Adjective) -> dict:
    # Informel Positif
    form_ip = adjective.romaji + " da"
    # Formel Positif
    form_fp = adjective.romaji + " desu"
    # Informel Négatif
    form_in = adjective.romaji + " janai"
    # Formel Négatif
    form_fn = adjective.romaji + " ja arimasen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }

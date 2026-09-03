from jpconjugation.models import Adjective

def get_connective_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "ii":
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
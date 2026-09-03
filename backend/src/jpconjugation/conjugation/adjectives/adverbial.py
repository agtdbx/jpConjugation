from jpconjugation.models import Adjective

def get_adverbial_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "ii":
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
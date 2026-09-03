from jpconjugation.models import Adjective

def get_present_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "ii":
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
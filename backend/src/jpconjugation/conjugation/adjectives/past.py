from jpconjugation.models import Adjective

def get_past_forms(adjective: Adjective) -> dict:
    type = adjective.type

    if type == "ii":
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
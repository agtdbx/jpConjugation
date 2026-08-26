def get_connective_forms(adjectif_parse: dict) -> dict:
    type = adjectif_parse.get("type")

    if type == "i":
        return _get_connective_i_forms(adjectif_parse)
    elif type == "na":
        return _get_connective_na_forms(adjectif_parse)
    else:
        return {}


def _get_connective_i_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["stem"] + "kute"
    # Informel Négatif
    form_in = adjectif_parse["stem"] + "kunakute"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_connective_na_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["adjectif"] + " de"
    # Informel Négatif
    form_in = adjectif_parse["adjectif"] + " janakute"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }
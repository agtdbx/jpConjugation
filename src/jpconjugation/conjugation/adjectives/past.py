def get_past_forms(adjectif_parse: dict) -> dict:
    type = adjectif_parse.get("type")

    if type == "i":
        return _get_past_i_forms(adjectif_parse)
    elif type == "na":
        return _get_past_na_forms(adjectif_parse)
    else:
        return {}


def _get_past_i_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["stem"] + "katta"
    # Informel Négatif
    form_in = adjectif_parse["stem"] + "kunakatta"

    return {
        "ip" : form_ip,
        "fp" : f"{form_ip} desu",
        "in" : form_in,
        "fn" : f"{form_in} desu",
    }


def _get_past_na_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["adjectif"] + " datta"
    # Formel Positif
    form_fp = adjectif_parse["adjectif"] + " deshita"
    # Informel Négatif
    form_in = adjectif_parse["adjectif"] + " janakatta"
    # Formel Négatif
    form_fn = adjectif_parse["adjectif"] + " ja arimasen deshita"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }
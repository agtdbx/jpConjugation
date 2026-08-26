def get_present_forms(adjectif_parse: dict) -> dict:
    type = adjectif_parse.get("type")

    if type == "i":
        return _get_present_i_forms(adjectif_parse)
    elif type == "na":
        return _get_present_na_forms(adjectif_parse)
    else:
        return {}


def _get_present_i_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["adjectif"]
    # Informel Négatif
    form_in = adjectif_parse["stem"] + "kunai"

    return {
        "ip" : form_ip,
        "fp" : f"{form_ip} desu",
        "in" : form_in,
        "fn" : f"{form_in} desu",
    }


def _get_present_na_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["adjectif"] + " da"
    # Formel Positif
    form_fp = adjectif_parse["adjectif"] + " desu"
    # Informel Négatif
    form_in = adjectif_parse["adjectif"] + " janai"
    # Formel Négatif
    form_fn = adjectif_parse["adjectif"] + " ja arimasen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }
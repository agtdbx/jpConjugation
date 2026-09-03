def get_adverbial_forms(adjectif_parse: dict) -> dict:
    type = adjectif_parse.get("type")

    if type == "i":
        return _get_adverbial_i_forms(adjectif_parse)
    elif type == "na":
        return _get_adverbial_na_forms(adjectif_parse)
    else:
        return {}


def _get_adverbial_i_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["stem"] + "ku"

    return {
        "ip" : form_ip
    }


def _get_adverbial_na_forms(adjectif_parse: dict) -> dict:
    # Informel Positif
    form_ip = adjectif_parse["adjectif"] + " ni"

    return {
        "ip" : form_ip
    }
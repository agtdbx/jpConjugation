from verbs.bases import get_base_i, get_base_o

def get_volitional_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_volitional_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_volitional_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_volitional_exception_forms(verbe_parse)
    else:
        return {}


def _get_volitional_godan_forms(verbe_parse: dict) -> dict:
    base_i = get_base_i(verbe_parse)
    base_o = get_base_o(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["stem"] + base_o + "u"
    # Formel Positif
    form_fp = verbe_parse["stem"] + base_i + "mashou"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_volitional_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["stem"] + "you"
    # Formel Positif
    form_fp = verbe_parse["stem"] + "mashou"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_volitional_exception_forms(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return _get_volitional_godan_forms(verbe_parse)
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "shiyou",
            "fp" : "shimashou",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "koyou",
            "fp" : "kimashou",
        }
    elif verbe_parse["verbe"] == "aru":
        return {
            "ip" : "arou",
            "fp" : "arimashou",
        }

    return {}
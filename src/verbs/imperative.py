from verbs.bases import get_base_te

def get_imperative_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_imperative_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_imperative_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_imperative_exception_forms(verbe_parse)
    else:
        return {}


def _get_imperative_godan_forms(verbe_parse: dict) -> dict:
    base_te = get_base_te(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["stem"] + base_te
    # Formel Positif
    form_fp = verbe_parse["stem"] + base_te + " kudasai"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_imperative_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["stem"] + "te"
    # Formel Positif
    form_fp = verbe_parse["stem"] + "te kudasai"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_imperative_exception_forms(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return {
            "ip" : "itte",
            "fp" : "itte kudasai",
        }
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "shite",
            "fp" : "shite kudasai",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "kite",
            "fp" : "kite kudasai",
        }
    elif verbe_parse["verbe"] == "aru":
        return {
            "ip" : "atte",
            "fp" : "atte kudasai",
        }

    return {}
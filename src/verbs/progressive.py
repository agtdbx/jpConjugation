from verbs.bases import get_base_te

def get_progressive_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_progressive_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_progressive_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_progressive_exception_forms(verbe_parse)
    else:
        return {}


def _get_progressive_godan_forms(verbe_parse: dict) -> dict:
    base_te = get_base_te(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["stem"] + base_te + "iru"
    # Formel Positif
    form_fp = verbe_parse["stem"] + base_te + "imasu"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_progressive_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["stem"] + "teiru"
    # Formel Positif
    form_fp = verbe_parse["stem"] + "teimasu"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_progressive_exception_forms(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return {
            "ip" : "itteiru",
            "fp" : "itteimasu",
        }
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "shiteiru",
            "fp" : "shiteimasu",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "kiteiru",
            "fp" : "kiteimasu",
        }
    elif verbe_parse["verbe"] == "aru":
        return {
            "ip" : "atteiru",
            "fp" : "atteimasu",
        }

    return {}
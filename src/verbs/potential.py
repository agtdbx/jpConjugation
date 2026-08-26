from verbs.bases import get_base_e

def get_potential_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_potential_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_potential_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_potential_exception_forms(verbe_parse)
    else:
        return {}


def _get_potential_godan_forms(verbe_parse: dict) -> dict:
    base_e = get_base_e(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["stem"] + base_e + "ru"
    # Formel Positif
    form_fp = verbe_parse["stem"] + base_e + "masu"
    # Informel Négatif
    form_in = verbe_parse["stem"] + base_e + "nai"
    # Formel Négatif
    form_fn = verbe_parse["stem"] + base_e + "masen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_potential_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["stem"] + "rareru"
    # Formel Positif
    form_fp = verbe_parse["stem"] + "raremasu"
    # Informel Négatif
    form_in = verbe_parse["stem"] + "rarenai"
    # Formel Négatif
    form_fn = verbe_parse["stem"] + "raremasen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_potential_exception_forms(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return _get_potential_godan_forms(verbe_parse)
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "dekiru",
            "fp" : "dekimasu",
            "in" : "dekinai",
            "fn" : "dekimasen",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "korareru",
            "fp" : "koraremasu",
            "in" : "korarenai",
            "fn" : "koraremasen",
        }

    return {}
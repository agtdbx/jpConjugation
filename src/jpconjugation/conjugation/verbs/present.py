from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_i

def get_present_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_present_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_present_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_present_exception_forms(verbe_parse)
    else:
        return {}


def _get_present_godan_forms(verbe_parse: dict) -> dict:
    base_a = get_base_a(verbe_parse)
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["verbe"]
    # Formel Positif
    form_fp = verbe_parse["stem"] + base_i + "masu"
    # Informel Négatif
    form_in = verbe_parse["stem"] + base_a + "nai"
    # Formel Négatif
    form_fn = verbe_parse["stem"] + base_i + "masen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_present_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["verbe"]
    # Formel Positif
    form_fp = verbe_parse["stem"] + "masu"
    # Informel Négatif
    form_in = verbe_parse["stem"] + "nai"
    # Formel Négatif
    form_fn = verbe_parse["stem"] + "masen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_present_exception_forms(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return {
            "ip" : "iku",
            "fp" : "ikimasu",
            "in" : "ikanai",
            "fn" : "ikimasen",
        }
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "suru",
            "fp" : "shimasu",
            "in" : "shinai",
            "fn" : "shimasen",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "kuru",
            "fp" : "kimasu",
            "in" : "konai",
            "fn" : "kimasen",
        }
    elif verbe_parse["verbe"] == "aru":
        return {
            "ip" : "aru",
            "fp" : "arimasu",
            "in" : "nai",
            "fn" : "arimasen",
        }

    return {}
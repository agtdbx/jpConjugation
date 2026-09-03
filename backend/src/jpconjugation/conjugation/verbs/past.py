from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_i, get_base_ta

def get_past_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_past_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_past_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_past_exception_forms(verbe_parse)
    else:
        return {}


def _get_past_godan_forms(verbe_parse: dict) -> dict:
    base_a = get_base_a(verbe_parse)
    base_ta = get_base_ta(verbe_parse)
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["stem"] + base_ta
    # Formel Positif
    form_fp = verbe_parse["stem"] + base_i + "mashita"
    # Informel Négatif
    form_in = verbe_parse["stem"] + base_a + "nakatta"
    # Formel Négatif
    form_fn = verbe_parse["stem"] + base_i + "masen deshita"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_past_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["stem"] + "ta"
    # Formel Positif
    form_fp = verbe_parse["stem"] + "mashita"
    # Informel Négatif
    form_in = verbe_parse["stem"] + "nakatta"
    # Formel Négatif
    form_fn = verbe_parse["stem"] + "masen deshita"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_past_exception_forms(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return {
            "ip" : "itta",
            "fp" : "ikimashita",
            "in" : "ikanakatta",
            "fn" : "ikimasen deshita",
        }
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "shita",
            "fp" : "shimashita",
            "in" : "shinakatta",
            "fn" : "shimasen deshita",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "kita",
            "fp" : "kimashita",
            "in" : "konakatta",
            "fn" : "kimasen deshita",
        }
    elif verbe_parse["verbe"] == "aru":
        return {
            "ip" : "atta",
            "fp" : "arimashita",
            "in" : "nakatta",
            "fn" : "arimasen deshita",
        }

    return {}
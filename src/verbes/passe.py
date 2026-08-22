from src.verbes.bases import get_base_a, get_base_i, get_base_ta

def get_godan_passe_formes(verbe_parse: dict) -> dict:
    base_a = get_base_a(verbe_parse)
    base_ta = get_base_ta(verbe_parse)
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["radical"] + base_ta
    # Formel Positif
    forme_fp = verbe_parse["radical"] + base_i + "mashita"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + base_a + "nakatta"
    # Formel Négatif
    forme_fn = verbe_parse["radical"] + base_i + "masen deshita"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }


def get_ichidan_passe_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["radical"] + "ta"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + "mashita"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + "nakatta"
    # Formel Négatif
    forme_fn = verbe_parse["radical"] + "masen deshita"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }


def get_exception_passe_formes(verbe_parse: dict) -> dict:
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
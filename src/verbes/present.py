from verbes.bases import get_base_a, get_base_i

def get_present_godan_formes(verbe_parse: dict) -> dict:
    base_a = get_base_a(verbe_parse)
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["verbe"]
    # Formel Positif
    forme_fp = verbe_parse["radical"] + base_i + "masu"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + base_a + "nai"
    # Formel Négatif
    forme_fn = verbe_parse["radical"] + base_i + "masen"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }


def get_present_ichidan_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["verbe"]
    # Formel Positif
    forme_fp = verbe_parse["radical"] + "masu"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + "nai"
    # Formel Négatif
    forme_fn = verbe_parse["radical"] + "masen"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }


def get_present_exception_formes(verbe_parse: dict) -> dict:
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
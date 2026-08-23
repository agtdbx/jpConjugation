from verbes.bases import get_base_te

def get_progressif_godan_formes(verbe_parse: dict) -> dict:
    base_te = get_base_te(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["radical"] + base_te + "iru"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + base_te + "imasu"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
    }


def get_progressif_ichidan_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["radical"] + "teiru"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + "teimasu"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
    }


def get_progressif_exception_formes(verbe_parse: dict) -> dict:
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
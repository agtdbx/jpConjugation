from verbes.bases import get_base_te

def get_imperatif_godan_formes(verbe_parse: dict) -> dict:
    base_te = get_base_te(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["radical"] + base_te
    # Formel Positif
    forme_fp = verbe_parse["radical"] + base_te + " kudasai"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
    }


def get_imperatif_ichidan_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["radical"] + "te"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + "te kudasai"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
    }


def get_imperatif_exception_formes(verbe_parse: dict) -> dict:
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
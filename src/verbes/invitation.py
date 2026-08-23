from verbes.bases import get_base_i, get_base_o

def get_invitation_godan_formes(verbe_parse: dict) -> dict:
    base_i = get_base_i(verbe_parse)
    base_o = get_base_o(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["radical"] + base_o + "u"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + base_i + "mashou"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
    }


def get_invitation_ichidan_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["radical"] + "you"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + "mashou"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
    }


def get_invitation_exception_formes(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return get_invitation_godan_formes(verbe_parse)
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
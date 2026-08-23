from verbes.bases import get_base_i

###########################################################################################
# Présent
###########################################################################################

def get_volonte_present_godan_formes(verbe_parse: dict) -> dict:
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["radical"] + base_i + "tai"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + base_i + "takunai"

    return {
        "ip" : forme_ip,
        "in" : forme_in,
    }


def get_volonte_present_ichidan_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["radical"] + "tai"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + "takunai"

    return {
        "ip" : forme_ip,
        "in" : forme_in,
    }


def get_volonte_present_exception_formes(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return {
            "ip" : "ikitai",
            "in" : "ikitakunai",
        }
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "shitai",
            "in" : "shitakunai",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "kitai",
            "in" : "kitakunai",
        }

    return {}

###########################################################################################
# Passé
###########################################################################################

def get_volonte_passe_godan_formes(verbe_parse: dict) -> dict:
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["radical"] + base_i + "takatta"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + base_i + "takunakatta"

    return {
        "ip" : forme_ip,
        "in" : forme_in,
    }


def get_volonte_passe_ichidan_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["radical"] + "takatta"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + "takunakatta"

    return {
        "ip" : forme_ip,
        "in" : forme_in,
    }


def get_volonte_passe_exception_formes(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return {
            "ip" : "ikitakatta",
            "in" : "ikitakunakatta",
        }
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "shitakatta",
            "in" : "shitakunakatta",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "kitakatta",
            "in" : "kitakunakatta",
        }

    return {}
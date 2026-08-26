from verbs.bases import get_base_i

###########################################################################################
# Présent
###########################################################################################

def get_desirative_present_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_desirative_present_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_desirative_present_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_desirative_present_exception_forms(verbe_parse)
    else:
        return {}


def _get_desirative_present_godan_forms(verbe_parse: dict) -> dict:
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["stem"] + base_i + "tai"
    # Informel Négatif
    form_in = verbe_parse["stem"] + base_i + "takunai"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_desirative_present_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["stem"] + "tai"
    # Informel Négatif
    form_in = verbe_parse["stem"] + "takunai"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_desirative_present_exception_forms(verbe_parse: dict) -> dict:
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

def get_desirative_past_forms(verbe_parse: dict) -> dict:
    type = verbe_parse.get("type")

    if type == "godan":
        return _get_desirative_past_godan_forms(verbe_parse)
    elif type == "ichidan":
        return _get_desirative_past_ichidan_forms(verbe_parse)
    elif type == "exception":
        return _get_desirative_past_exception_forms(verbe_parse)
    else:
        return {}


def _get_desirative_past_godan_forms(verbe_parse: dict) -> dict:
    base_i = get_base_i(verbe_parse)

    # Informel Positif
    form_ip = verbe_parse["stem"] + base_i + "takatta"
    # Informel Négatif
    form_in = verbe_parse["stem"] + base_i + "takunakatta"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_desirative_past_ichidan_forms(verbe_parse: dict) -> dict:
    # Informel Positif
    form_ip = verbe_parse["stem"] + "takatta"
    # Informel Négatif
    form_in = verbe_parse["stem"] + "takunakatta"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_desirative_past_exception_forms(verbe_parse: dict) -> dict:
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
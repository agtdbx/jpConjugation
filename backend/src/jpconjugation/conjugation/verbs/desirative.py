from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_i

###########################################################################################
# Present
###########################################################################################

def get_desirative_present_rules(verb: Verb) -> dict:
    if verb.type == "godan":
        return {
            "ip": "Pour un verbe Godan, on prend la forme en I et on ajoute 'tai'.",
            "fp": "Pour un verbe Godan, on prend la forme en I et on ajoute 'tai desu'.",
            "in": "Pour un verbe Godan, on prend la forme en I et on ajoute 'takunai'.",
            "fn": "Pour un verbe Godan, on prend la forme en I et on ajoute 'takunai desu'."
        }
    elif verb.type == "ichidan":
        return {
            "ip": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'tai'.",
            "fp": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'tai desu'.",
            "in": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'takunai'.",
            "fn": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'takunai desu'."
        }
    elif verb.type == "exception":
        return {
            "ip": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'tai'.",
            "fp": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'tai desu'.",
            "in": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'takunai'.",
            "fn": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'takunai desu'."
        }
    return {}


def get_desirative_present_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_desirative_present_godan_forms(verb)
    elif type == "ichidan":
        return _get_desirative_present_ichidan_forms(verb)
    elif type == "exception":
        return _get_desirative_present_exception_forms(verb)
    else:
        return {}


def _get_desirative_present_godan_forms(verb: Verb) -> dict:
    base_i = get_base_i(verb)

    # Informel Positif
    form_ip = verb.stem + base_i + "tai"
    # Informel Négatif
    form_in = verb.stem + base_i + "takunai"

    return {
        "ip" : form_ip,
        "fp" : form_ip + " desu",
        "in" : form_in,
        "fn" : form_in + " desu",
    }


def _get_desirative_present_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "tai"
    # Informel Négatif
    form_in = verb.stem + "takunai"

    return {
        "ip" : form_ip,
        "fp" : form_ip + " desu",
        "in" : form_in,
        "fn" : form_in + " desu",

    }


def _get_desirative_present_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "ikitai",
            "fp" : "ikitai desu",
            "in" : "ikitakunai",
            "fn" : "ikitakunai desu",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shitai",
            "fp" : "shitai desu",
            "in" : "shitakunai",
            "fn" : "shitakunai desu",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kitai",
            "fp" : "kitai desu",
            "in" : "kitakunai",
            "fn" : "kitakunai desu",
        }

    return {}

###########################################################################################
# Past
###########################################################################################

def get_desirative_past_rules(verb: Verb) -> dict:
    if verb.type == "godan":
        return {
            "ip": "Pour un verbe Godan, on prend la forme en I et on ajoute 'takatta'.",
            "fp": "Pour un verbe Godan, on prend la forme en I et on ajoute 'takatta desu'.",
            "in": "Pour un verbe Godan, on prend la forme en I et on ajoute 'takunakatta'.",
            "fn": "Pour un verbe Godan, on prend la forme en I et on ajoute 'takunakatta desu'."
        }
    elif verb.type == "ichidan":
        return {
            "ip": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'takatta'.",
            "fp": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'takatta desu'.",
            "in": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'takunakatta'.",
            "fn": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'takunakatta desu'."
        }
    elif verb.type == "exception":
        return {
            "ip": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'takatta'.",
            "fp": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'takatta desu'.",
            "in": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'takunakatta'.",
            "fn": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'takunakatta desu'."
        }
    return {}


def get_desirative_past_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_desirative_past_godan_forms(verb)
    elif type == "ichidan":
        return _get_desirative_past_ichidan_forms(verb)
    elif type == "exception":
        return _get_desirative_past_exception_forms(verb)
    else:
        return {}


def _get_desirative_past_godan_forms(verb: Verb) -> dict:
    base_i = get_base_i(verb)

    # Informel Positif
    form_ip = verb.stem + base_i + "takatta"
    # Informel Négatif
    form_in = verb.stem + base_i + "takunakatta"

    return {
        "ip" : form_ip,
        "fp" : form_ip + " desu",
        "in" : form_in,
        "fn" : form_in + " desu",
    }


def _get_desirative_past_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "takatta"
    # Informel Négatif
    form_in = verb.stem + "takunakatta"

    return {
        "ip" : form_ip,
        "fp" : form_ip + " desu",
        "in" : form_in,
        "fn" : form_in + " desu",
    }


def _get_desirative_past_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "ikitakatta",
            "fp" : "ikitakatta desu",
            "in" : "ikitakunakatta",
            "fn" : "ikitakunakatta desu",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shitakatta",
            "fp" : "shitakatta desu",
            "in" : "shitakunakatta",
            "fn" : "shitakunakatta desu",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kitakatta",
            "fp" : "kitakatta desu",
            "in" : "kitakunakatta",
            "fn" : "kitakunakatta desu",
        }

    return {}

from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_e, get_base_te

###########################################################################################
# Soft
###########################################################################################

def get_imperative_soft_rules(verb: Verb) -> dict:
    if verb.type == "godan":
        return {
            "ip": "Pour un verbe Godan, on prend la forme en TE.",
            "fp": "Pour un verbe Godan, on prend la forme en TE et on ajoute ' kudasai'.",
            "in": "Pour un verbe Godan, on prend la forme en A et on ajoute 'naide'.",
            "fn": "Pour un verbe Godan, on prend la forme en A et on ajoute 'naide kudasai'."
        }
    elif verb.type == "ichidan":
        return {
            "ip": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'te'.",
            "fp": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'te kudasai'.",
            "in": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'naide'.",
            "fn": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'naide kudasai'."
        }
    elif verb.type == "exception":
        return {
            "ip": f"Exception ({verb.romaji}) : On utilise l'exception en TE.",
            "fp": f"Exception ({verb.romaji}) : On utilise l'exception en TE + ' kudasai'.",
            "in": f"Exception ({verb.romaji}) : On utilise l'exception en A + 'naide'.",
            "fn": f"Exception ({verb.romaji}) : On utilise l'exception en A + 'naide kudasai'."
        }
    return {}


def get_imperative_soft_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_imperative_soft_godan_forms(verb)
    elif type == "ichidan":
        return _get_imperative_soft_ichidan_forms(verb)
    elif type == "exception":
        return _get_imperative_soft_exception_forms(verb)
    else:
        return {}


def _get_imperative_soft_godan_forms(verb: Verb) -> dict:
    base_a = get_base_a(verb)
    base_te = get_base_te(verb)

    return {
        "ip" : verb.stem + base_te,
        "fp" : verb.stem + base_te + " kudasai",
        "in" : verb.stem + base_a + "naide",
        "fn" : verb.stem + base_a + "naide kudasai",
    }


def _get_imperative_soft_ichidan_forms(verb: Verb) -> dict:
    return {
        "ip" : verb.stem + "te",
        "fp" : verb.stem + "te kudasai",
        "in" : verb.stem + "naide",
        "fn" : verb.stem + "naide kudasai",
    }


def _get_imperative_soft_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "itte",
            "fp" : "itte kudasai",
            "in" : "ikanaide",
            "fn" : "ikanaide kudasai",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shite",
            "fp" : "shite kudasai",
            "in" : "shinaide",
            "fn" : "shinaide kudasai",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kite",
            "fp" : "kite kudasai",
            "in" : "konaide",
            "fn" : "konaide kudasai",
        }

    return {}

###########################################################################################
# Hard
###########################################################################################

def get_imperative_hard_rules(verb: Verb) -> dict:
    if verb.type == "godan":
        return {
            "ip": "Pour un verbe Godan, on prend la forme en E.",
            "in": "Pour un verbe Godan, on prend la forme du dictionnaire et on ajoute 'na'.",
        }
    elif verb.type == "ichidan":
        return {
            "ip": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'ro'.",
            "in": "Pour un verbe Ichidan, on prend la forme du dictionnaire et on ajoute 'na'.",
        }
    elif verb.type == "exception":
        return {
            "ip": f"Exception ({verb.romaji}) : La forme est irrégulière.",
            "in": f"Exception ({verb.romaji}) : on prend la forme du dictionnaire et on ajoute 'na'.",
        }
    return {}


def get_imperative_hard_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_imperative_hard_godan_forms(verb)
    elif type == "ichidan":
        return _get_imperative_hard_ichidan_forms(verb)
    elif type == "exception":
        return _get_imperative_hard_exception_forms(verb)
    else:
        return {}


def _get_imperative_hard_godan_forms(verb: Verb) -> dict:
    base_e = get_base_e(verb)

    return {
        "ip" : verb.stem + base_e,
        "in" : verb.romaji + "na",
    }


def _get_imperative_hard_ichidan_forms(verb: Verb) -> dict:
    return {
        "ip" : verb.stem + "ro",
        "in" : verb.romaji + "na",
    }


def _get_imperative_hard_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "ike",
            "in" : "ikuna",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shiro",
            "in" : "suruna",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "koi",
            "in" : "kuruna",
        }

    return {}

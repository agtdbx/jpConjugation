from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_i

###########################################################################################
# Présent
###########################################################################################

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
        "in" : form_in,
    }


def _get_desirative_present_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "tai"
    # Informel Négatif
    form_in = verb.stem + "takunai"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_desirative_present_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "ikitai",
            "in" : "ikitakunai",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shitai",
            "in" : "shitakunai",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kitai",
            "in" : "kitakunai",
        }

    return {}

###########################################################################################
# Passé
###########################################################################################

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
        "in" : form_in,
    }


def _get_desirative_past_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "takatta"
    # Informel Négatif
    form_in = verb.stem + "takunakatta"

    return {
        "ip" : form_ip,
        "in" : form_in,
    }


def _get_desirative_past_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "ikitakatta",
            "in" : "ikitakunakatta",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shitakatta",
            "in" : "shitakunakatta",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kitakatta",
            "in" : "kitakunakatta",
        }

    return {}
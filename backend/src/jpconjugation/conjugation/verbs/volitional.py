from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_i, get_base_o

def get_volitional_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_volitional_godan_forms(verb)
    elif type == "ichidan":
        return _get_volitional_ichidan_forms(verb)
    elif type == "exception":
        return _get_volitional_exception_forms(verb)
    else:
        return {}


def _get_volitional_godan_forms(verb: Verb) -> dict:
    base_i = get_base_i(verb)
    base_o = get_base_o(verb)

    # Informel Positif
    form_ip = verb.stem + base_o + "u"
    # Formel Positif
    form_fp = verb.stem + base_i + "mashou"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_volitional_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "you"
    # Formel Positif
    form_fp = verb.stem + "mashou"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_volitional_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return _get_volitional_godan_forms(verb)
    elif verb.romaji == "suru":
        return {
            "ip" : "shiyou",
            "fp" : "shimashou",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "koyou",
            "fp" : "kimashou",
        }
    elif verb.romaji == "aru":
        return {
            "ip" : "arou",
            "fp" : "arimashou",
        }

    return {}
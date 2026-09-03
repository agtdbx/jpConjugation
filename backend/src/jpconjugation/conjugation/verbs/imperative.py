from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_te

def get_imperative_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_imperative_godan_forms(verb)
    elif type == "ichidan":
        return _get_imperative_ichidan_forms(verb)
    elif type == "exception":
        return _get_imperative_exception_forms(verb)
    else:
        return {}


def _get_imperative_godan_forms(verb: Verb) -> dict:
    base_te = get_base_te(verb)

    # Informel Positif
    form_ip = verb.stem + base_te
    # Formel Positif
    form_fp = verb.stem + base_te + " kudasai"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_imperative_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "te"
    # Formel Positif
    form_fp = verb.stem + "te kudasai"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_imperative_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "itte",
            "fp" : "itte kudasai",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shite",
            "fp" : "shite kudasai",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kite",
            "fp" : "kite kudasai",
        }
    elif verb.romaji == "aru":
        return {
            "ip" : "atte",
            "fp" : "atte kudasai",
        }

    return {}
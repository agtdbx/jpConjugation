from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_te

def get_progressive_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_progressive_godan_forms(verb)
    elif type == "ichidan":
        return _get_progressive_ichidan_forms(verb)
    elif type == "exception":
        return _get_progressive_exception_forms(verb)
    else:
        return {}


def _get_progressive_godan_forms(verb: Verb) -> dict:
    base_te = get_base_te(verb)

    # Informel Positif
    form_ip = verb.stem + base_te + "iru"
    # Formel Positif
    form_fp = verb.stem + base_te + "imasu"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_progressive_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "teiru"
    # Formel Positif
    form_fp = verb.stem + "teimasu"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
    }


def _get_progressive_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "itteiru",
            "fp" : "itteimasu",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shiteiru",
            "fp" : "shiteimasu",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kiteiru",
            "fp" : "kiteimasu",
        }
    elif verb.romaji == "aru":
        return {
            "ip" : "atteiru",
            "fp" : "atteimasu",
        }

    return {}
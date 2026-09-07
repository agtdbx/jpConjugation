from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_te

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
    base_a = get_base_a(verb)
    base_te = get_base_te(verb)

    return {
        "ip" : verb.stem + base_te,
        "fp" : verb.stem + base_te + " kudasai",
        "in" : verb.stem + base_a + "naide",
        "fn" : verb.stem + base_a + "naide kudasai",
    }


def _get_imperative_ichidan_forms(verb: Verb) -> dict:
    return {
        "ip" : verb.stem + "te",
        "fp" : verb.stem + "te kudasai",
        "in" : verb.stem + "naide",
        "fn" : verb.stem + "naide kudasai",
    }


def _get_imperative_exception_forms(verb: Verb) -> dict:
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
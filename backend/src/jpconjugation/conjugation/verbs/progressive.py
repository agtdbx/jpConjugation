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

    return {
        "ip" : verb.stem + base_te + "iru",
        "fp" : verb.stem + base_te + "imasu",
        "in" : verb.stem + base_te + "inai",
        "fn" : verb.stem + base_te + "imasen",
    }


def _get_progressive_ichidan_forms(verb: Verb) -> dict:
    return {
        "ip" : verb.stem + "teiru",
        "fp" : verb.stem + "teimasu",
        "in" : verb.stem + "teinai",
        "fn" : verb.stem + "teimasen",
    }


def _get_progressive_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "itteiru",
            "fp" : "itteimasu",
            "in" : "itteinai",
            "fn" : "itteimasen",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shiteiru",
            "fp" : "shiteimasu",
            "in" : "shiteinai",
            "fn" : "shiteimasen",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kiteiru",
            "fp" : "kiteimasu",
            "in" : "kiteinai",
            "fn" : "kiteimasen",
        }
    elif verb.romaji == "aru":
        return {
            "ip" : "atteiru",
            "fp" : "atteimasu",
            "in" : "atteinai",
            "fn" : "atteimasen",
        }

    return {}
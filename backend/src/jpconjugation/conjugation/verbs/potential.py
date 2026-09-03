from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_e

def get_potential_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_potential_godan_forms(verb)
    elif type == "ichidan":
        return _get_potential_ichidan_forms(verb)
    elif type == "exception":
        return _get_potential_exception_forms(verb)
    else:
        return {}


def _get_potential_godan_forms(verb: Verb) -> dict:
    base_e = get_base_e(verb)

    # Informel Positif
    form_ip = verb.stem + base_e + "ru"
    # Formel Positif
    form_fp = verb.stem + base_e + "masu"
    # Informel Négatif
    form_in = verb.stem + base_e + "nai"
    # Formel Négatif
    form_fn = verb.stem + base_e + "masen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_potential_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "rareru"
    # Formel Positif
    form_fp = verb.stem + "raremasu"
    # Informel Négatif
    form_in = verb.stem + "rarenai"
    # Formel Négatif
    form_fn = verb.stem + "raremasen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_potential_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return _get_potential_godan_forms(verb)
    elif verb.romaji == "suru":
        return {
            "ip" : "dekiru",
            "fp" : "dekimasu",
            "in" : "dekinai",
            "fn" : "dekimasen",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "korareru",
            "fp" : "koraremasu",
            "in" : "korarenai",
            "fn" : "koraremasen",
        }

    return {}
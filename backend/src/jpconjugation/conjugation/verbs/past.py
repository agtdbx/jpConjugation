from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_i, get_base_ta

def get_past_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_past_godan_forms(verb)
    elif type == "ichidan":
        return _get_past_ichidan_forms(verb)
    elif type == "exception":
        return _get_past_exception_forms(verb)
    else:
        return {}


def _get_past_godan_forms(verb: Verb) -> dict:
    base_a = get_base_a(verb)
    base_ta = get_base_ta(verb)
    base_i = get_base_i(verb)

    # Informel Positif
    form_ip = verb.stem + base_ta
    # Formel Positif
    form_fp = verb.stem + base_i + "mashita"
    # Informel Négatif
    form_in = verb.stem + base_a + "nakatta"
    # Formel Négatif
    form_fn = verb.stem + base_i + "masen deshita"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_past_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.stem + "ta"
    # Formel Positif
    form_fp = verb.stem + "mashita"
    # Informel Négatif
    form_in = verb.stem + "nakatta"
    # Formel Négatif
    form_fn = verb.stem + "masen deshita"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_past_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "itta",
            "fp" : "ikimashita",
            "in" : "ikanakatta",
            "fn" : "ikimasen deshita",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shita",
            "fp" : "shimashita",
            "in" : "shinakatta",
            "fn" : "shimasen deshita",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kita",
            "fp" : "kimashita",
            "in" : "konakatta",
            "fn" : "kimasen deshita",
        }
    elif verb.romaji == "aru":
        return {
            "ip" : "atta",
            "fp" : "arimashita",
            "in" : "nakatta",
            "fn" : "arimasen deshita",
        }

    return {}
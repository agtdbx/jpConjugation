from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_i, get_base_ta
from jpconjugation.conjugation.verbs.rules import build_core_rules

def get_past_rules(verb: Verb) -> dict:
    return build_core_rules(
        verb=verb,
        godan_rules={
            "ip": "on prend la forme en TA",
            "fp": "on prend la forme en I et on ajoute 'mashita'",
            "in": "on prend la forme en A et on ajoute 'nakatta'",
            "fn": "on prend la forme en I et on ajoute 'masen deshita'",
        },
        ichidan_rules={
            "ip": "on enlève 'ru' au radical et on ajoute 'ta'",
            "fp": "on enlève 'ru' au radical et on ajoute 'mashita'",
            "in": "on enlève 'ru' au radical et on ajoute 'nakatta'",
            "fn": "on enlève 'ru' au radical et on ajoute 'masen deshita'",
        },
        exception_rules={
            "fp": "On utilise l'exception en I + 'mashita'",
            "in": "On utilise l'exception en A + 'nakatta'",
            "fn": "On utilise l'exception en I + 'masen deshita'",
        }
    )


def get_past_forms(verb: Verb) -> dict:
    if verb.type == "godan":
        return _get_past_godan_forms(verb)
    elif verb.type == "ichidan":
        return _get_past_ichidan_forms(verb)
    elif verb.type == "exception":
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

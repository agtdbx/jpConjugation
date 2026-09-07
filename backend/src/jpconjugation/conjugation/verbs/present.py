from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_i

def get_present_rules(verb: Verb) -> dict:
    if verb.type == "godan":
        return {
            "ip": "Forme du dictionnaire.",
            "fp": "Pour un verbe Godan, on prend la forme en I et on ajoute 'masu'.",
            "in": "Pour un verbe Godan, on prend la forme en A et on ajoute 'nai'.",
            "fn": "Pour un verbe Godan, on prend la forme en I et on ajoute 'masen'."
        }
    elif verb.type == "ichidan":
        return {
            "ip": "Forme du dictionnaire.",
            "fp": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'masu'.",
            "in": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'nai'.",
            "fn": "Pour un verbe Ichidan, on enlève 'ru' au radical et on ajoute 'masen'."
        }
    elif verb.type == "exception":
        return {
            "ip": f"Exception ({verb.romaji}) : La forme est irrégulière.",
            "fp": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'masu'.",
            "in": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'nai'.",
            "fn": f"Exception ({verb.romaji}) : On utilise l'exception en I + 'masen'."
        }
    return {}


def get_present_forms(verb: Verb) -> dict:
    type = verb.type

    if type == "godan":
        return _get_present_godan_forms(verb)
    elif type == "ichidan":
        return _get_present_ichidan_forms(verb)
    elif type == "exception":
        return _get_present_exception_forms(verb)
    else:
        return {}


def _get_present_godan_forms(verb: Verb) -> dict:
    base_a = get_base_a(verb)
    base_i = get_base_i(verb)

    # Informel Positif
    form_ip = verb.romaji
    # Formel Positif
    form_fp = verb.stem + base_i + "masu"
    # Informel Négatif
    form_in = verb.stem + base_a + "nai"
    # Formel Négatif
    form_fn = verb.stem + base_i + "masen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_present_ichidan_forms(verb: Verb) -> dict:
    # Informel Positif
    form_ip = verb.romaji
    # Formel Positif
    form_fp = verb.stem + "masu"
    # Informel Négatif
    form_in = verb.stem + "nai"
    # Formel Négatif
    form_fn = verb.stem + "masen"

    return {
        "ip" : form_ip,
        "fp" : form_fp,
        "in" : form_in,
        "fn" : form_fn,
    }


def _get_present_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "iku",
            "fp" : "ikimasu",
            "in" : "ikanai",
            "fn" : "ikimasen",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "suru",
            "fp" : "shimasu",
            "in" : "shinai",
            "fn" : "shimasen",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kuru",
            "fp" : "kimasu",
            "in" : "konai",
            "fn" : "kimasen",
        }
    elif verb.romaji == "aru":
        return {
            "ip" : "aru",
            "fp" : "arimasu",
            "in" : "nai",
            "fn" : "arimasen",
        }

    return {}
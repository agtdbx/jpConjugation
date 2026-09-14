from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_e, get_base_te
from jpconjugation.conjugation.verbs.rules import build_core_rules

###########################################################################################
# TE
###########################################################################################

def get_imperative_te_rules(verb: Verb) -> dict:
    return build_core_rules(
        verb=verb,
        godan_rules={
            "ip": "on prend la forme en TE",
            "fp": "on prend la forme en TE et on ajoute ' kudasai'",
            "in": "on prend la forme en A et on ajoute 'naide'",
            "fn": "on prend la forme en A et on ajoute 'naide kudasai'",
        },
        ichidan_rules={
            "ip": "on enlève 'ru' au radical et on ajoute 'te'",
            "fp": "on enlève 'ru' au radical et on ajoute 'te kudasai'",
            "in": "on enlève 'ru' au radical et on ajoute 'naide'",
            "fn": "on enlève 'ru' au radical et on ajoute 'naide kudasai'",
        },
        exception_rules={
            "ip": "On utilise l'exception en TE",
            "fp": "On utilise l'exception en TE + ' kudasai'",
            "in": "On utilise l'exception en A + 'naide'",
            "fn": "On utilise l'exception en A + 'naide kudasai'",
        }
    )


def get_imperative_te_forms(verb: Verb) -> dict:
    if verb.type == "godan":
        return _get_imperative_te_godan_forms(verb)
    elif verb.type == "ichidan":
        return _get_imperative_te_ichidan_forms(verb)
    elif verb.type == "exception":
        return _get_imperative_te_exception_forms(verb)
    else:
        return {}


def _get_imperative_te_godan_forms(verb: Verb) -> dict:
    base_a = get_base_a(verb)
    base_te = get_base_te(verb)

    return {
        "ip" : verb.stem + base_te,
        "fp" : verb.stem + base_te + " kudasai",
        "in" : verb.stem + base_a + "naide",
        "fn" : verb.stem + base_a + "naide kudasai",
    }


def _get_imperative_te_ichidan_forms(verb: Verb) -> dict:
    return {
        "ip" : verb.stem + "te",
        "fp" : verb.stem + "te kudasai",
        "in" : verb.stem + "naide",
        "fn" : verb.stem + "naide kudasai",
    }


def _get_imperative_te_exception_forms(verb: Verb) -> dict:
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

###########################################################################################
# RO
###########################################################################################

def get_imperative_ro_rules(verb: Verb) -> dict:
    return build_core_rules(
        verb=verb,
        godan_rules={
            "ip": "on prend la forme en E",
            "in": "on prend la forme du dictionnaire et on ajoute 'na'",
        },
        ichidan_rules={
            "ip": "on enlève 'ru' au radical et on ajoute 'ro'",
            "in": "on prend la forme du dictionnaire et on ajoute 'na'",
        },
        exception_rules={
            "in": "On prend la forme du dictionnaire et on ajoute 'na'",
        }
    )


def get_imperative_ro_forms(verb: Verb) -> dict:
    if verb.type == "godan":
        return _get_imperative_ro_godan_forms(verb)
    elif verb.type == "ichidan":
        return _get_imperative_ro_ichidan_forms(verb)
    elif verb.type == "exception":
        return _get_imperative_ro_exception_forms(verb)
    else:
        return {}


def _get_imperative_ro_godan_forms(verb: Verb) -> dict:
    base_e = get_base_e(verb)

    return {
        "ip" : verb.stem + base_e,
        "in" : verb.romaji + "na",
    }


def _get_imperative_ro_ichidan_forms(verb: Verb) -> dict:
    return {
        "ip" : verb.stem + "ro",
        "in" : verb.romaji + "na",
    }


def _get_imperative_ro_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "ike",
            "in" : "ikuna",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "shiro",
            "in" : "suruna",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "koi",
            "in" : "kuruna",
        }

    return {}

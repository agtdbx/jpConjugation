from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a, get_base_e
from jpconjugation.conjugation.verbs.rules import build_core_rules, build_derived_rules
from jpconjugation.conjugation.verbs.past import get_past_forms

###########################################################################################
# BA
###########################################################################################

def get_conditional_ba_rules(verb: Verb) -> dict:
    return build_core_rules(
        verb=verb,
        godan_rules={
            "ip": "on prend la forme en E et on ajoute 'ba'",
            "in": "on prend la forme en A et on ajoute 'nakereba'",
        },
        ichidan_rules={
            "ip": "on enlève 'ru' au radical et on ajoute 'reba'",
            "in": "on enlève 'ru' au radical et on ajoute 'ranakereba'",
        }
    )


def get_conditional_ba_forms(verb: Verb) -> dict:
    if verb.type == "godan":
        return _get_conditional_ba_godan_forms(verb)
    elif verb.type == "ichidan":
        return _get_conditional_ba_ichidan_forms(verb)
    elif verb.type == "exception":
        return _get_conditional_ba_exception_forms(verb)
    else:
        return {}


def _get_conditional_ba_godan_forms(verb: Verb) -> dict:
    base_a = get_base_a(verb)
    base_e = get_base_e(verb)

    return {
        "ip" : verb.stem + base_e + "ba",
        "in" : verb.stem + base_a + "nakereba",
    }


def _get_conditional_ba_ichidan_forms(verb: Verb) -> dict:
    return {
        "ip" : verb.stem + "reba",
        "in" : verb.stem + "ranakereba",
    }


def _get_conditional_ba_exception_forms(verb: Verb) -> dict:
    if verb.romaji == "iku":
        return {
            "ip" : "ikeba",
            "in" : "ikanakereba",
        }
    elif verb.romaji == "suru":
        return {
            "ip" : "sureba",
            "in" : "shinakereba",
        }
    elif verb.romaji == "kuru":
        return {
            "ip" : "kureba",
            "in" : "konakereba",
        }
    elif verb.romaji == "aru":
        return {
            "ip" : "areba",
            "in" : "nakereba",
        }

    return {}

###########################################################################################
# TARA
###########################################################################################

def get_conditional_tara_rules(verb: Verb) -> dict:
    return build_derived_rules(
        verb=verb,
        godan_action="on prend la conjugaison au passé",
        ichidan_action="on prend la conjugaison au passé",
        base_suffixes={"ip": "ra"},
        exception_rules={
            "ip": "On prend la conjugaison au passé et on ajoute 'ra'"
        }
    )


def get_conditional_tara_forms(verb: Verb) -> dict:
    past_forms = get_past_forms(verb)
    if "ip" not in past_forms.keys():
        return {}

    return {
        "ip" : past_forms["ip"] + "ra"
    }

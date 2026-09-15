from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_e
from jpconjugation.conjugation.verbs.rules import build_derived_rules


def get_potential_rules(verb: Verb) -> dict:
    return build_derived_rules(
        verb=verb,
        godan_action="prend la forme en E",
        ichidan_action="enlève 'ru' au radical",
        base_suffixes={"ip" : "ru"},
        ichidan_prefix="rare",
    )


def get_potential_forms(verb: Verb) -> dict:
    potential_verb = _get_potential_verb(verb)
    if not potential_verb:
        return {}

    return {"ip" : potential_verb}


def _get_potential_verb(verb: Verb) -> str:
    if verb.type == "godan":
        return verb.stem + get_base_e(verb) + "ru"
    elif verb.type == "ichidan":
        return verb.stem + "rareru"
    elif verb.type == "exception":
        if verb.romaji == "iku":
            return verb.stem + get_base_e(verb) + "ru"
        elif verb.romaji == "suru":
            return "dekiru"
        elif verb.romaji == "kuru":
            return "korareru"

    return ""

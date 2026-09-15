from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a
from jpconjugation.conjugation.verbs.rules import build_derived_rules


def get_causative_rules(verb: Verb) -> dict:
    return build_derived_rules(
        verb=verb,
        godan_action="prend la forme en A",
        ichidan_action="enlève 'ru' au radical",
        base_suffixes={"ip": "seru"},
        ichidan_prefix="sa",
    )


def get_causative_forms(verb: Verb) -> dict:
    causative_verb = _get_causative_verb(verb)
    if not causative_verb:
        return {}

    return {"ip" : causative_verb}


def _get_causative_verb(verb: Verb) -> str:
    if verb.type == "godan":
        return verb.stem + get_base_a(verb) + "seru"
    elif verb.type == "ichidan":
        return verb.stem + "saseru"
    elif verb.type == "exception":
        if verb.romaji == "iku":
            return "ikaseru"
        elif verb.romaji == "suru":
            return "saseru"
        elif verb.romaji == "kuru":
            return "koraseru"

    return ""

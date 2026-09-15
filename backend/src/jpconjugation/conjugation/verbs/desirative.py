from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_i
from jpconjugation.conjugation.verbs.rules import build_derived_rules


def get_desirative_rules(verb: Verb) -> dict:
    return build_derived_rules(
        verb=verb,
        godan_action="prend la forme en I",
        ichidan_action="enlève 'ru' au radical",
        base_suffixes={"ip": "tai"},
    )


def get_desirative_forms(verb: Verb) -> dict:
    desirative_verb = _get_desirative_verb(verb)
    if not desirative_verb:
        return {}

    return {"ip" : desirative_verb}


def _get_desirative_verb(verb: Verb) -> str:
    if verb.type == "godan":
        return verb.stem + get_base_i(verb) + "tai"
    elif verb.type == "ichidan":
        return verb.stem + "tai"
    elif verb.type == "exception":
        if verb.romaji == "iku":
            return "ikitai"
        elif verb.romaji == "suru":
            return "shitai"
        elif verb.romaji == "kuru":
            return "kitai"

    return ""

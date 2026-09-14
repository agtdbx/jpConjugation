from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_a
from jpconjugation.conjugation.verbs.rules import build_derived_rules


def get_passive_rules(verb: Verb) -> dict:
    return build_derived_rules(
        verb=verb,
        godan_action="prend la forme en A",
        ichidan_action="enlève 'ru' au radical",
        base_suffixes={"ip": "reru"},
        ichidan_prefix="ra",
    )


def get_passive_forms(verb: Verb) -> dict:
    passive_verb = _get_passive_verb(verb)
    if not passive_verb:
        return {}

    return {"ip" : passive_verb}


def _get_passive_verb(verb: Verb) -> str:
    if verb.type == "godan":
        return verb.stem + get_base_a(verb) + "reru"
    elif verb.type == "ichidan":
        return verb.stem + "rareru"
    elif verb.type == "exception":
        if verb.romaji == "iku":
            return "ikareru"
        elif verb.romaji == "suru":
            return "sareru"
        elif verb.romaji == "kuru":
            return "korareru"

    return ""

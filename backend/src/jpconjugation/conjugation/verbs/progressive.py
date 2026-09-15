from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_te
from jpconjugation.conjugation.verbs.rules import build_derived_rules


def get_progressive_rules(verb: Verb) -> dict:
    return build_derived_rules(
        verb=verb,
        godan_action="prend la forme en TE",
        ichidan_action="enlève 'ru' au radical",
        base_suffixes={"ip": "iru"},
        ichidan_prefix="te",
    )


def get_progressive_forms(verb: Verb) -> dict:
    progressive_verb = _get_progressive_verb(verb)
    if not progressive_verb:
        return {}

    return {"ip" : progressive_verb}


def _get_progressive_verb(verb: Verb) -> str:
    if verb.type == "godan":
        return verb.stem + get_base_te(verb) + "iru"
    elif verb.type == "ichidan":
        return verb.stem + "teiru"
    elif verb.type == "exception":
        if verb.romaji == "iku":
            return "itteiru"
        elif verb.romaji == "suru":
            return "shiteiru"
        elif verb.romaji == "kuru":
            return "kiteiru"
        elif verb.romaji == "aru":
            return "atteiru"

    return ""

from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_te
from jpconjugation.conjugation.verbs.present import _get_present_ichidan_forms
from jpconjugation.conjugation.verbs.rules import build_derived_rules


SUFFIXES_PROGRESSIVE = {"ip": "iru", "fp": "imasu", "in": "inai", "fn": "imasen"}

def get_progressive_rules(verb: Verb) -> dict:
    exception_custom = {
        "fp": "On utilise l'exception en TE + 'imasu'",
        "in": "On utilise l'exception en TE + 'inai'",
        "fn": "On utilise l'exception en TE + 'imasen'",
    }
    return build_derived_rules(
        verb=verb,
        godan_action="prend la forme en TE",
        ichidan_action="enlève 'ru' au radical",
        base_suffixes=SUFFIXES_PROGRESSIVE,
        ichidan_prefix="te",
        exception_rules=exception_custom
    )


def get_progressive_forms(verb: Verb) -> dict:
    progressive_stem = _get_progressive_stem(verb)
    if not progressive_stem:
        return {}

    fake_verb = Verb(
        romaji=progressive_stem + "ru",
        kanji=verb.kanji,
        traduction=verb.traduction,
        type="ichidan",
        stem=progressive_stem,
        ending="ru"
    )

    return _get_present_ichidan_forms(fake_verb)


def _get_progressive_stem(verb: Verb) -> str:
    if verb.type == "godan":
        return verb.stem + get_base_te(verb) + "i"
    elif verb.type == "ichidan":
        return verb.stem + "tei"
    elif verb.type == "exception":
        if verb.romaji == "iku":
            return "ittei"
        elif verb.romaji == "suru":
            return "shitei"
        elif verb.romaji == "kuru":
            return "kitei"
        elif verb.romaji == "aru":
            return "attei"

    return ""

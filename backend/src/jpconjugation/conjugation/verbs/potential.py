from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.bases import get_base_e
from jpconjugation.conjugation.verbs.present import _get_present_ichidan_forms
from jpconjugation.conjugation.verbs.past import _get_past_ichidan_forms
from jpconjugation.conjugation.verbs.rules import build_derived_rules, SUFFIXES_PRESENT, SUFFIXES_PAST


###########################################################################################
# Stem
###########################################################################################

def _get_potential_stem(verb: Verb) -> str:
    if verb.type == "godan":
        return verb.stem + get_base_e(verb)
    elif verb.type == "ichidan":
        return verb.stem + "rare"
    elif verb.type == "exception":
        if verb.romaji == "iku":
            return verb.stem + get_base_e(verb)
        elif verb.romaji == "suru":
            return "deki"
        elif verb.romaji == "kuru":
            return "korare"

    return ""

###########################################################################################
# Present
###########################################################################################

def get_potential_present_rules(verb: Verb) -> dict:
    return build_derived_rules(
            verb=verb,
            godan_action="prend la forme en E",
            ichidan_action="enlève 'ru' au radical",
            base_suffixes=SUFFIXES_PRESENT,
            ichidan_prefix="rare",
    )


def get_potential_present_forms(verb: Verb) -> dict:
    potential_stem = _get_potential_stem(verb)
    if not potential_stem:
        return {}

    fake_verb = Verb(
        romaji=potential_stem + "ru",
        kanji=verb.kanji,
        traduction=verb.traduction,
        type="ichidan",
        stem=potential_stem,
        ending="ru"
    )

    return _get_present_ichidan_forms(fake_verb)

###########################################################################################
# Past
###########################################################################################

def get_potential_past_rules(verb: Verb) -> dict:
    return build_derived_rules(
            verb=verb,
            godan_action="prend la forme en E",
            ichidan_action="enlève 'ru' au radical",
            base_suffixes=SUFFIXES_PAST,
            ichidan_prefix="rare",
    )


def get_potential_past_forms(verb: Verb) -> dict:
    potential_stem = _get_potential_stem(verb)
    if not potential_stem:
        return {}

    fake_verb = Verb(
        romaji=potential_stem + "ru",
        kanji=verb.kanji,
        traduction=verb.traduction,
        type="ichidan",
        stem=potential_stem,
        ending="ru"
    )

    return _get_past_ichidan_forms(fake_verb)

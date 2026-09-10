import pytest
from pydantic import ValidationError
from jpconjugation.define import (
    VERBS_TYPES, VERBS_ENDINGS,
    VERBS_ALLOWED_FORMS
)
from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.conjugation import conjugate_verb, get_verb_rules


def test_verbs_bad_type():
    with pytest.raises(ValidationError):
        Verb(romaji="r", kanji="k", traduction="t", type="type")


@pytest.mark.parametrize("type", VERBS_TYPES.keys())
def test_verbs_good_type(type: str):
    Verb(romaji="aru", kanji="k", traduction="t", type=type)


def test_verbs_bad_ending():
    with pytest.raises(ValidationError):
        Verb(romaji="test", kanji="k", traduction="t", type="ichidan")


@pytest.mark.parametrize("ending", VERBS_ENDINGS)
def test_verbs_ending_stem(ending: str):
    verb = Verb(romaji=f"a{ending}", kanji="k", traduction="t", type="ichidan")

    assert verb.ending == ending
    assert verb.stem == "a"


def test_verbs_bad_rules():
    verb = Verb(romaji="aru", kanji="k", traduction="t", type="godan")
    rules = get_verb_rules(verb, "test")

    assert isinstance(rules, dict)
    assert len(rules) == 0


@pytest.mark.parametrize("tense, forms", VERBS_ALLOWED_FORMS.items())
def test_verbs_godan_rules(
        tense: str,
        forms: list[str]
        ):
    verb = Verb(romaji="aru", kanji="k", traduction="t", type="godan")
    rules = get_verb_rules(verb, tense)

    assert isinstance(rules, dict)
    assert len(rules) == len(forms)

    for form, rule in rules.items():
        if tense == "pr" and form == "ip":
            assert "dictionnaire" in rule.lower()
        else:
            assert "godan" in rule.lower()


@pytest.mark.parametrize("tense, forms", VERBS_ALLOWED_FORMS.items())
def test_verbs_ichidan_rules(
        tense: str,
        forms: list[str]
        ):
    verb = Verb(romaji="aru", kanji="k", traduction="t", type="ichidan")
    rules = get_verb_rules(verb, tense)

    assert isinstance(rules, dict)
    assert len(rules) == len(forms)

    for form, rule in rules.items():
        if tense == "pr" and form == "ip":
            assert "dictionnaire" in rule.lower()
        else:
            assert "ichidan" in rule.lower()


@pytest.mark.parametrize("tense, forms", VERBS_ALLOWED_FORMS.items())
def test_verbs_exception_rules(
        tense: str,
        forms: list[str]
        ):
    verb = Verb(romaji="aru", kanji="k", traduction="t", type="exception")
    rules = get_verb_rules(verb, tense)

    assert isinstance(rules, dict)
    assert len(rules) == len(forms)

    for form, rule in rules.items():
        if tense == "pr" and form == "ip":
            assert "dictionnaire" in rule.lower()
        else:
            assert "exception" in rule.lower()

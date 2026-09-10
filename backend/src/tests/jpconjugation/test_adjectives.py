import pytest
from pydantic import ValidationError
from jpconjugation.define import (
    ADJECTIVES_TYPES, ADJECTIVES_ALLOWED_FORMS,
    ADJECTIVES_EXCEPTIONS
)
from jpconjugation.models import Adjective
from jpconjugation.conjugation.adjectives.conjugation import (
    conjugate_adjective, get_adjective_rules
)


def test_adjectives_bad_type():
    with pytest.raises(ValidationError):
        Adjective(romaji="test", kanji="k", traduction="t", type="type")


@pytest.mark.parametrize("type", ADJECTIVES_TYPES.keys())
def test_adjectives_good_type(type: str):
    Adjective(romaji="test", kanji="k", traduction="t", type=type)


def test_adjectives_stem_i():
    adjectives = Adjective(romaji=f"ai", kanji="k", traduction="t", type="i")

    assert adjectives.stem == "a"


def test_adjectives_stem_na():
    adjectives = Adjective(romaji=f"ai", kanji="k", traduction="t", type="na")

    assert adjectives.stem == "ai"


@pytest.mark.parametrize("exception", ADJECTIVES_EXCEPTIONS.items())
def test_adjectives_stem_exception(exception:str):
    romaji, stem = exception
    adjectives = Adjective(romaji=romaji, kanji="k", traduction="t", type="i")

    assert adjectives.stem == stem


def test_adjectives_bad_rules():
    adjective = Adjective(romaji="ai", kanji="k", traduction="t", type="i")
    rules = get_adjective_rules(adjective, "test")

    assert isinstance(rules, dict)
    assert len(rules) == 0


@pytest.mark.parametrize("tense, forms", ADJECTIVES_ALLOWED_FORMS.items())
def test_adjectives_i_rules(
        tense: str,
        forms: list[str]
        ):
    adjective = Adjective(romaji="ai", kanji="k", traduction="t", type="i")
    rules = get_adjective_rules(adjective, tense)

    assert isinstance(rules, dict)
    assert len(rules) == len(forms)

    for form, rule in rules.items():
        if tense == "pr" and form == "ip":
            assert "dictionnaire" in rule.lower()
        else:
            assert "i adjectif" in rule.lower()


@pytest.mark.parametrize("tense, forms", ADJECTIVES_ALLOWED_FORMS.items())
def test_adjectives_na_rules(
        tense: str,
        forms: list[str]
        ):
    adjective = Adjective(romaji="ai", kanji="k", traduction="t", type="na")
    rules = get_adjective_rules(adjective, tense)

    assert isinstance(rules, dict)
    assert len(rules) == len(forms)

    for rule in rules.values():
        assert "na adjectif" in rule.lower()


# ADJECTIVES_PRESENT = [
#     ("i", "furui", "furui", "furui desu", "furukunai", "furukunai desu"),
#     ("na", "kirei", "kirei da", "kirei desu", "kirei janai", "kirei ja arimasen"),
# ]
# @pytest.mark.parametrize("type, romaji, form_ip, form_fp, form_in, form_fn", ADJECTIVES_PRESENT)
# def test_conjugate_adjectives_present(
#         type: str,
#         romaji: str,
#         form_ip: str,
#         form_fp: str,
#         form_in: str,
#         form_fn: str
#         ):
#     adjective = Adjective(romaji=romaji, kanji="k", traduction="t", type=type)
#     forms = conjugate_adjective(adjective, tense_id="pr")

#     assert forms.get("ip") == form_ip
#     assert forms.get("fp") == form_fp
#     assert forms.get("in") == form_in
#     assert forms.get("fn") == form_fn

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


@pytest.mark.parametrize("romaji, stem", ADJECTIVES_EXCEPTIONS.items())
def test_adjectives_stem_exception(
        romaji: str,
        stem:str
        ):
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


def test_conjugate_adjectives_bad_tense():
    adjective = Adjective(romaji="ai", kanji="k", traduction="t", type="i")
    forms = conjugate_adjective(adjective, tense_id="test")

    assert len(forms) == 0


ADJECTIVES_PR = [
    ("i", "furui", "furui", "furui desu", "furukunai", "furukunai desu"),
    ("i", "ii", "ii", "ii desu", "yokunai", "yokunai desu"),
    ("na", "kirei", "kirei da", "kirei desu", "kirei janai", "kirei ja arimasen"),
]
@pytest.mark.parametrize("adj_type, romaji, form_ip, form_fp, form_in, form_fn", ADJECTIVES_PR)
def test_conjugate_adjectives_present(
        adj_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    adjective = Adjective(romaji=romaji, kanji="k", traduction="t", type=adj_type)
    forms = conjugate_adjective(adjective, tense_id="pr")

    assert len(forms) == 4
    assert forms.get("ip") == form_ip
    assert forms.get("fp") == form_fp
    assert forms.get("in") == form_in
    assert forms.get("fn") == form_fn


ADJECTIVES_PA = [
    ("i", "furui", "furukatta", "furukatta desu", "furukunakatta", "furukunakatta desu"),
    ("i", "ii", "yokatta", "yokatta desu", "yokunakatta", "yokunakatta desu"),
    ("na", "kirei", "kirei datta", "kirei deshita", "kirei janakatta", "kirei ja arimasen deshita"),
]
@pytest.mark.parametrize("adj_type, romaji, form_ip, form_fp, form_in, form_fn", ADJECTIVES_PA)
def test_conjugate_adjectives_past(
        adj_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    adjective = Adjective(romaji=romaji, kanji="k", traduction="t", type=adj_type)
    forms = conjugate_adjective(adjective, tense_id="pa")

    assert len(forms) == 4
    assert forms.get("ip") == form_ip
    assert forms.get("fp") == form_fp
    assert forms.get("in") == form_in
    assert forms.get("fn") == form_fn


ADJECTIVES_CO = [
    ("i", "furui", "furukute", "furukunakute"),
    ("i", "ii", "yokute", "yokunakute"),
    ("na", "kirei", "kirei de", "kirei janakute"),
]
@pytest.mark.parametrize("adj_type, romaji, form_ip, form_in", ADJECTIVES_CO)
def test_conjugate_adjectives_connective(
        adj_type: str,
        romaji: str,
        form_ip: str,
        form_in: str,
        ):
    adjective = Adjective(romaji=romaji, kanji="k", traduction="t", type=adj_type)
    forms = conjugate_adjective(adjective, tense_id="co")

    assert len(forms) == 2
    assert forms.get("ip") == form_ip
    assert forms.get("in") == form_in


ADJECTIVES_AD = [
    ("i", "furui", "furuku"),
    ("i", "ii", "yoku"),
    ("na", "kirei", "kirei ni"),
]
@pytest.mark.parametrize("adj_type, romaji, form_ip", ADJECTIVES_AD)
def test_conjugate_adjectives_adverbial(
        adj_type: str,
        romaji: str,
        form_ip: str,
        ):
    adjective = Adjective(romaji=romaji, kanji="k", traduction="t", type=adj_type)
    forms = conjugate_adjective(adjective, tense_id="ad")

    assert len(forms) == 1
    assert forms.get("ip") == form_ip


ADJECTIVES_CO_BA = [
    ("i", "furui", "furukereba", "furukunakereba"),
    ("i", "ii", "yokereba", "yokunakereba"),
    ("na", "kirei", "kirei nara", "kirei janai nara"),
]
@pytest.mark.parametrize("adj_type, romaji, form_ip, form_in", ADJECTIVES_CO_BA)
def test_conjugate_adjectives_conditional_ba(
        adj_type: str,
        romaji: str,
        form_ip: str,
        form_in: str,
        ):
    adjective = Adjective(romaji=romaji, kanji="k", traduction="t", type=adj_type)
    forms = conjugate_adjective(adjective, tense_id="co-ba")

    assert len(forms) == 2
    assert forms.get("ip") == form_ip
    assert forms.get("in") == form_in


ADJECTIVES_CO_TARA = [
    ("i", "furui", "furukattara", "furukunakattara"),
    ("i", "ii", "yokattara", "yokunakattara"),
    ("na", "kirei", "kirei dattara", "kirei ja nakattara"),
]
@pytest.mark.parametrize("adj_type, romaji, form_ip, form_in", ADJECTIVES_CO_TARA)
def test_conjugate_adjectives_conditional_tara(
        adj_type: str,
        romaji: str,
        form_ip: str,
        form_in: str,
        ):
    adjective = Adjective(romaji=romaji, kanji="k", traduction="t", type=adj_type)
    forms = conjugate_adjective(adjective, tense_id="co-ta")

    assert len(forms) == 2
    assert forms.get("ip") == form_ip
    assert forms.get("in") == form_in

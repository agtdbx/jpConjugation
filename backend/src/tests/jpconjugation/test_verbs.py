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


def test_conjugate_verbs_bad_tense():
    verb = Verb(romaji="aru", kanji="k", traduction="t", type="ichidan")
    forms = conjugate_verb(verb, tense_id="test")

    assert len(forms) == 0


VERBS_PR = [
    ("godan", "matsu", "matsu", "machimasu", "matanai", "machimasen"),
    ("godan", "hashiru", "hashiru", "hashirimasu", "hashiranai", "hashirimasen"),
    ("godan", "nomu", "nomu", "nomimasu", "nomanai", "nomimasen"),
    ("godan", "shinu", "shinu", "shinimasu", "shinanai", "shinimasen"),
    ("godan", "asobu", "asobu", "asobimasu", "asobanai", "asobimasen"),
    ("godan", "kiku", "kiku", "kikimasu", "kikanai", "kikimasen"),
    ("godan", "oyogu", "oyogu", "oyogimasu", "oyoganai", "oyogimasen"),
    ("godan", "hanasu", "hanasu", "hanashimasu", "hanasanai", "hanashimasen"),
    ("godan", "tsukau", "tsukau", "tsukaimasu", "tsukawanai", "tsukaimasen"),
    ("ichidan", "taberu", "taberu", "tabemasu", "tabenai", "tabemasen"),
    ("exception", "suru", "suru", "shimasu", "shinai", "shimasen"),
    ("exception", "kuru", "kuru", "kimasu", "konai", "kimasen"),
    ("exception", "aru", "aru", "arimasu", "nai", "arimasen"),
    ("exception", "iku", "iku", "ikimasu", "ikanai", "ikimasen"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_PR)
def test_conjugate_verbs_present(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="pr")

    assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn


VERBS_PA = [
    ("godan", "matsu", "matta", "machimashita", "matanakatta", "machimasen deshita"),
    ("godan", "hashiru", "hashitta", "hashirimashita", "hashiranakatta", "hashirimasen deshita"),
    ("godan", "nomu", "nonda", "nomimashita", "nomanakatta", "nomimasen deshita"),
    ("godan", "shinu", "shinda", "shinimashita", "shinanakatta", "shinimasen deshita"),
    ("godan", "asobu", "asonda", "asobimashita", "asobanakatta", "asobimasen deshita"),
    ("godan", "kiku", "kiita", "kikimashita", "kikanakatta", "kikimasen deshita"),
    ("godan", "oyogu", "oyoida", "oyogimashita", "oyoganakatta", "oyogimasen deshita"),
    ("godan", "hanasu", "hanashita", "hanashimashita", "hanasanakatta", "hanashimasen deshita"),
    ("godan", "tsukau", "tsukatta", "tsukaimashita", "tsukawanakatta", "tsukaimasen deshita"),
    ("ichidan", "taberu", "tabeta", "tabemashita", "tabenakatta", "tabemasen deshita"),
    ("exception", "suru", "shita", "shimashita", "shinakatta", "shimasen deshita"),
    ("exception", "kuru", "kita", "kimashita", "konakatta", "kimasen deshita"),
    ("exception", "aru", "atta", "arimashita", "nakatta", "arimasen deshita"),
    ("exception", "iku", "itta", "ikimashita", "ikanakatta", "ikimasen deshita"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_PA)
def test_conjugate_verbs_past(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="pa")

    assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn


VERBS_IM = [
    ("godan", "matsu", "matte", "matte kudasai", "matanaide", "matanaide kudasai"),
    ("godan", "hashiru", "hashitte", "hashitte kudasai", "hashiranaide", "hashiranaide kudasai"),
    ("godan", "nomu", "nonde", "nonde kudasai", "nomanaide", "nomanaide kudasai"),
    ("godan", "shinu", "shinde", "shinde kudasai", "shinanaide", "shinanaide kudasai"),
    ("godan", "asobu", "asonde", "asonde kudasai", "asobanaide", "asobanaide kudasai"),
    ("godan", "kiku", "kiite", "kiite kudasai", "kikanaide", "kikanaide kudasai"),
    ("godan", "oyogu", "oyoide", "oyoide kudasai", "oyoganaide", "oyoganaide kudasai"),
    ("godan", "hanasu", "hanashite", "hanashite kudasai", "hanasanaide", "hanasanaide kudasai"),
    ("godan", "tsukau", "tsukatte", "tsukatte kudasai", "tsukawanaide", "tsukawanaide kudasai"),
    ("ichidan", "taberu", "tabete", "tabete kudasai", "tabenaide", "tabenaide kudasai"),
    ("exception", "suru", "shite", "shite kudasai", "shinaide", "shinaide kudasai"),
    ("exception", "kuru", "kite", "kite kudasai", "konaide", "konaide kudasai"),
    ("exception", "aru", "", "", "", ""),
    ("exception", "iku", "itte", "itte kudasai", "ikanaide", "ikanaide kudasai"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_IM)
def test_conjugate_verbs_imperative(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="im")

    if romaji == "aru":
        assert len(forms) == 0
    else:
        assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn


VERBS_PRO = [
    ("godan", "matsu", "matteiru", "matteimasu", "matteinai", "matteimasen"),
    ("godan", "hashiru", "hashitteiru", "hashitteimasu", "hashitteinai", "hashitteimasen"),
    ("godan", "nomu", "nondeiru", "nondeimasu", "nondeinai", "nondeimasen"),
    ("godan", "shinu", "shindeiru", "shindeimasu", "shindeinai", "shindeimasen"),
    ("godan", "asobu", "asondeiru", "asondeimasu", "asondeinai", "asondeimasen"),
    ("godan", "kiku", "kiiteiru", "kiiteimasu", "kiiteinai", "kiiteimasen"),
    ("godan", "oyogu", "oyoideiru", "oyoideimasu", "oyoideinai", "oyoideimasen"),
    ("godan", "hanasu", "hanashiteiru", "hanashiteimasu", "hanashiteinai", "hanashiteimasen"),
    ("godan", "tsukau", "tsukatteiru", "tsukatteimasu", "tsukatteinai", "tsukatteimasen"),
    ("ichidan", "taberu", "tabeteiru", "tabeteimasu", "tabeteinai", "tabeteimasen"),
    ("exception", "suru", "shiteiru", "shiteimasu", "shiteinai", "shiteimasen"),
    ("exception", "kuru", "kiteiru", "kiteimasu", "kiteinai", "kiteimasen"),
    ("exception", "aru", "atteiru", "atteimasu", "atteinai", "atteimasen"),
    ("exception", "iku", "itteiru", "itteimasu", "itteinai", "itteimasen"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_PRO)
def test_conjugate_verbs_progressive(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="pro")

    assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn


VERBS_DE_PR = [
    ("godan", "matsu", "machitai", "machitai desu", "machitakunai", "machitakunai desu"),
    ("godan", "hashiru", "hashiritai", "hashiritai desu", "hashiritakunai", "hashiritakunai desu"),
    ("godan", "nomu", "nomitai", "nomitai desu", "nomitakunai", "nomitakunai desu"),
    ("godan", "shinu", "shinitai", "shinitai desu", "shinitakunai", "shinitakunai desu"),
    ("godan", "asobu", "asobitai", "asobitai desu", "asobitakunai", "asobitakunai desu"),
    ("godan", "kiku", "kikitai", "kikitai desu", "kikitakunai", "kikitakunai desu"),
    ("godan", "oyogu", "oyogitai", "oyogitai desu", "oyogitakunai", "oyogitakunai desu"),
    ("godan", "hanasu", "hanashitai", "hanashitai desu", "hanashitakunai", "hanashitakunai desu"),
    ("godan", "tsukau", "tsukaitai", "tsukaitai desu", "tsukaitakunai", "tsukaitakunai desu"),
    ("ichidan", "taberu", "tabetai", "tabetai desu", "tabetakunai", "tabetakunai desu"),
    ("exception", "suru", "shitai", "shitai desu", "shitakunai", "shitakunai desu"),
    ("exception", "kuru", "kitai", "kitai desu", "kitakunai", "kitakunai desu"),
    ("exception", "aru", "", "", "", ""),
    ("exception", "iku", "ikitai", "ikitai desu", "ikitakunai", "ikitakunai desu"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_DE_PR)
def test_conjugate_verbs_desirative_present(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="de-pr")

    if romaji == "aru":
        assert len(forms) == 0
    else:
        assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn


VERBS_DE_PA = [
    ("godan", "matsu", "machitakatta", "machitakatta desu", "machitakunakatta", "machitakunakatta desu"),
    ("godan", "hashiru", "hashiritakatta", "hashiritakatta desu", "hashiritakunakatta", "hashiritakunakatta desu"),
    ("godan", "nomu", "nomitakatta", "nomitakatta desu", "nomitakunakatta", "nomitakunakatta desu"),
    ("godan", "shinu", "shinitakatta", "shinitakatta desu", "shinitakunakatta", "shinitakunakatta desu"),
    ("godan", "asobu", "asobitakatta", "asobitakatta desu", "asobitakunakatta", "asobitakunakatta desu"),
    ("godan", "kiku", "kikitakatta", "kikitakatta desu", "kikitakunakatta", "kikitakunakatta desu"),
    ("godan", "oyogu", "oyogitakatta", "oyogitakatta desu", "oyogitakunakatta", "oyogitakunakatta desu"),
    ("godan", "hanasu", "hanashitakatta", "hanashitakatta desu", "hanashitakunakatta", "hanashitakunakatta desu"),
    ("godan", "tsukau", "tsukaitakatta", "tsukaitakatta desu", "tsukaitakunakatta", "tsukaitakunakatta desu"),
    ("ichidan", "taberu", "tabetakatta", "tabetakatta desu", "tabetakunakatta", "tabetakunakatta desu"),
    ("exception", "suru", "shitakatta", "shitakatta desu", "shitakunakatta", "shitakunakatta desu"),
    ("exception", "kuru", "kitakatta", "kitakatta desu", "kitakunakatta", "kitakunakatta desu"),
    ("exception", "aru", "", "", "", ""),
    ("exception", "iku", "ikitakatta", "ikitakatta desu", "ikitakunakatta", "ikitakunakatta desu"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_DE_PA)
def test_conjugate_verbs_desirative_past(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="de-pa")

    if romaji == "aru":
        assert len(forms) == 0
    else:
        assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn


VERBS_VO = [
    ("godan", "matsu", "matou", "machimashou"),
    ("godan", "hashiru", "hashirou", "hashirimashou"),
    ("godan", "nomu", "nomou", "nomimashou"),
    ("godan", "shinu", "shinou", "shinimashou"),
    ("godan", "asobu", "asobou", "asobimashou"),
    ("godan", "kiku", "kikou", "kikimashou"),
    ("godan", "oyogu", "oyogou", "oyogimashou"),
    ("godan", "hanasu", "hanasou", "hanashimashou"),
    ("godan", "tsukau", "tsukaou", "tsukaimashou"),
    ("ichidan", "taberu", "tabeyou", "tabemashou"),
    ("exception", "suru", "shiyou", "shimashou"),
    ("exception", "kuru", "koyou", "kimashou"),
    ("exception", "aru", "arou", "arimashou"),
    ("exception", "iku", "ikou", "ikimashou"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp", VERBS_VO)
def test_conjugate_verbs_volitional(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="vo")

    assert len(forms) == 2
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp


VERBS_PO = [
    ("godan", "matsu", "materu", "matemasu", "matenai", "matemasen"),
    ("godan", "hashiru", "hashireru", "hashiremasu", "hashirenai", "hashiremasen"),
    ("godan", "nomu", "nomeru", "nomemasu", "nomenai", "nomemasen"),
    ("godan", "shinu", "shineru", "shinemasu", "shinenai", "shinemasen"),
    ("godan", "asobu", "asoberu", "asobemasu", "asobenai", "asobemasen"),
    ("godan", "kiku", "kikeru", "kikemasu", "kikenai", "kikemasen"),
    ("godan", "oyogu", "oyogeru", "oyogemasu", "oyogenai", "oyogemasen"),
    ("godan", "hanasu", "hanaseru", "hanasemasu", "hanasenai", "hanasemasen"),
    ("godan", "tsukau", "tsukaeru", "tsukaemasu", "tsukaenai", "tsukaemasen"),
    ("ichidan", "taberu", "taberareru", "taberaremasu", "taberarenai", "taberaremasen"),
    ("exception", "suru", "dekiru", "dekimasu", "dekinai", "dekimasen"),
    ("exception", "kuru", "korareru", "koraremasu", "korarenai", "koraremasen"),
    ("exception", "aru", "", "", "", ""),
    ("exception", "iku", "ikeru", "ikemasu", "ikenai", "ikemasen"),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_PO)
def test_conjugate_verbs_potential(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_verb(verb, tense_id="po")

    if romaji == "aru":
        assert len(forms) == 0
    else:
        assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn

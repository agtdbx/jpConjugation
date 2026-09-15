import pytest
from jpconjugation.models import Verb, Adjective
from jpconjugation.conjugation.word import conjugate_word

VERBS_PR = [
    # General parsing
    ("verb", "godan", "matsu", ""),
    ("verb", "godan", "matsu", "test"),
    ("verb", "godan", "matsu", "|test"),
    ("verb", "godan", "matsu", "pas||pr"),
    ("verb", "godan", "matsu", "pas|pr|"),
    ("verb", "godan", "matsu", "|pas|pr"),
    # Verb specific
    ("verb", "godan", "matsu", "pr|pas"),
    ("verb", "godan", "matsu", "pr|pa"),
    ("verb", "godan", "matsu", "de|im-te"),
    # Adjective specific
    ("adjective", "i", "ookii", "pr|pa"),
]
@pytest.mark.parametrize("word_type, content_type, romaji, tense_chain", VERBS_PR)
def test_conjugate_words_bad_tense(
        word_type: str,
        content_type: str,
        romaji: str,
        tense_chain: str
        ):
    if word_type == "verb":
        word = Verb(romaji=romaji, kanji="k", traduction="t", type=content_type)
    else:
        word = Adjective(romaji=romaji, kanji="k", traduction="t", type=content_type)

    forms = conjugate_word(word, tense_chain=tense_chain)

    assert len(forms) == 0


VERBS_CA_PAS_PA = [
    ("godan", "matsu", "mataserareta", "mataseraremashita", "mataserarenakatta", "mataseraremasen deshita"),
    ("godan", "hashiru", "hashiraserareta", "hashiraseraremashita", "hashiraserarenakatta", "hashiraseraremasen deshita"),
    ("godan", "nomu", "nomaserareta", "nomaseraremashita", "nomaserarenakatta", "nomaseraremasen deshita"),
    ("godan", "shinu", "shinaserareta", "shinaseraremashita", "shinaserarenakatta", "shinaseraremasen deshita"),
    ("godan", "asobu", "asobaserareta", "asobaseraremashita", "asobaserarenakatta", "asobaseraremasen deshita"),
    ("godan", "kiku", "kikaserareta", "kikaseraremashita", "kikaserarenakatta", "kikaseraremasen deshita"),
    ("godan", "oyogu", "oyogaserareta", "oyogaseraremashita", "oyogaserarenakatta", "oyogaseraremasen deshita"),
    ("godan", "hanasu", "hanasaserareta", "hanasaseraremashita", "hanasaserarenakatta", "hanasaseraremasen deshita"),
    ("godan", "tsukau", "tsukawaserareta", "tsukawaseraremashita", "tsukawaserarenakatta", "tsukawaseraremasen deshita"),
    ("ichidan", "taberu", "tabesaserareta", "tabesaseraremashita", "tabesaserarenakatta", "tabesaseraremasen deshita"),
    ("exception", "iku", "ikaserareta", "ikaseraremashita", "ikaserarenakatta", "ikaseraremasen deshita"),
    ("exception", "suru", "saserareta", "saseraremashita", "saserarenakatta", "saseraremasen deshita"),
    ("exception", "kuru", "koraserareta", "koraseraremashita", "koraserarenakatta", "koraseraremasen deshita"),
    ("exception", "aru", "", "", "", ""),
]
@pytest.mark.parametrize("verb_type, romaji, form_ip, form_fp, form_in, form_fn", VERBS_CA_PAS_PA)
def test_conjugate_verbs_causative_passive_past(
        verb_type: str,
        romaji: str,
        form_ip: str,
        form_fp: str,
        form_in: str,
        form_fn: str,
        ):
    verb = Verb(romaji=romaji, kanji="k", traduction="t", type=verb_type)
    forms = conjugate_word(verb, tense_chain="ca|pas|pa")

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
    ("exception", "iku", "ikitakatta", "ikitakatta desu", "ikitakunakatta", "ikitakunakatta desu"),
    ("exception", "suru", "shitakatta", "shitakatta desu", "shitakunakatta", "shitakunakatta desu"),
    ("exception", "kuru", "kitakatta", "kitakatta desu", "kitakunakatta", "kitakunakatta desu"),
    ("exception", "aru", "", "", "", ""),
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
    forms = conjugate_word(verb, tense_chain="de|pa")

    if romaji == "aru":
        assert len(forms) == 0
    else:
        assert len(forms) == 4
    assert forms.get("ip", "") == form_ip
    assert forms.get("fp", "") == form_fp
    assert forms.get("in", "") == form_in
    assert forms.get("fn", "") == form_fn

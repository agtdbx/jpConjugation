import pytest
from data_update.parsing import clean_anki_html, get_word_parts_from_card

ANKI_HTML_TESTS = [
    ("test", "test"),
    ("&nbsptest", "test"),
    ("&lt;test", "<test"),
    ("&gt;test", ">test"),
    ("test<br>", "test"),
    ("test<br>test", "test\ntest"),
    ("test<br/>test", "test\ntest"),
    ("test<br />test", "test\ntest"),
    ("test<div>test<div/>", "test\ntest"),
    ("<h1>test</h1>", "test"),
    ("test<script src='notAVirus.js'></script>", "test"),
    ("test\n\n\ntest", "test\ntest"),
]
@pytest.mark.parametrize("anki_html, anki_clean", ANKI_HTML_TESTS)
def test_clean_anki_html(
        anki_html: str,
        anki_clean: str
        ):
    assert clean_anki_html(anki_html) == anki_clean


CARD_PARSE_KO_TESTS = [
    ("", ""),
    ("kanji", ""),
]
@pytest.mark.parametrize("recto, verso", CARD_PARSE_KO_TESTS)
def test_parse_ko_card(
        recto: str,
        verso: str,
        ):
    assert get_word_parts_from_card(recto, verso) == None


CARD_PARSE_OK_TESTS = [
    ("かんじ", "test", "かんじ", "kanji", "test"),
    ("バー", "test", "バー", "ba-", "test"),
    ("かんじ", "ねこ\ntest", "かんじ", "neko", "test"),
    ("かんじ ", "ねこ\n test \ncat", "かんじ", "neko", "test"),
    ("ダサい ", "Ringard", "ダサい", "dasai", "Ringard"),
]
@pytest.mark.parametrize("recto, verso, kanji, romaji, traduction", CARD_PARSE_OK_TESTS)
def test_parse_ok_card(
        recto: str,
        verso: str,
        kanji: str,
        romaji: str,
        traduction: str
        ):
    words = get_word_parts_from_card(recto, verso)

    assert words != None
    assert words[0] == kanji
    assert words[1] == romaji
    assert words[2] == traduction

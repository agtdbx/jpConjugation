import json
import pytest
from pydantic import ValidationError
from jpconjugation.parsing.load import load_data_json

FAKE_DATA_OK = {
    "verbs": [
        {
            "romaji": "miru",
            "kanji": "見る",
            "traduction": "Voir",
            "type": "ichidan",
            "stem": "mi",
            "ending": "ru"
        }
    ],
    "adjectives": [
        {
            "romaji": "furui",
            "kanji": "古い",
            "traduction": "Vieux, ancien",
            "type": "i",
            "stem": "furu"
        },
    ]}


def test_bad_file():
    with pytest.raises(FileNotFoundError):
        load_data_json("i'm an error file path !")


@pytest.mark.parametrize("bad_data", [
    {},  # Empty file
    {"adjectives": []},  # Test missing verbs
    {"verbs": []},       # Test missing adjectives
    {"verbs": [{"kanji": "test"}], "adjectives": []},  # Test verb error
    {"verbs": [{"romaji": "miru", "kanji": "見る", "traduction": "Voir", "type": "type", "stem": "mi", "ending": "ru"}], "adjectives": []},  # Test verb bad type
    {"verbs": [], "adjectives": [{"kanji": "test"}]},  # Test adjective error
    {"verbs": [], "adjectives": [{"romaji": "furui", "kanji": "古い", "traduction": "Vieux, ancien", "type": "type", "stem": "furu"}]},  # Test adjective bad type
])
def test_file_validation_errors(tmp_path, bad_data):
    test_file = tmp_path / "test_data.json"
    test_file.write_text(json.dumps(bad_data), encoding="utf-8")

    with pytest.raises(ValidationError):
        load_data_json(str(test_file))


def test_file_empty_lists(tmp_path):
    # Create fake file
    test_file = tmp_path / "test_data.json"
    test_file_data = {
        "verbs" : [],
        "adjectives" : [],
    }
    test_file.write_text(json.dumps(test_file_data), encoding="utf-8")

    data = load_data_json(str(test_file))

    assert len(data.verbs) == 0
    assert len(data.adjectives) == 0


def test_load_json_file_success(tmp_path):
    # Create fake file
    test_file = tmp_path / "test_data.json"
    test_file.write_text(json.dumps(FAKE_DATA_OK), encoding="utf-8")

    # Parse data
    data = load_data_json(str(test_file))

    # Checks
    assert len(data.verbs) == 1
    assert data.verbs[0].romaji == "miru"
    assert data.verbs[0].kanji == "見る"
    assert data.verbs[0].traduction == "Voir"
    assert data.verbs[0].type == "ichidan"
    assert data.verbs[0].stem == "mi"
    assert data.verbs[0].ending == "ru"

    assert len(data.adjectives) == 1
    assert data.adjectives[0].romaji == "furui"
    assert data.adjectives[0].kanji == "古い"
    assert data.adjectives[0].traduction == "Vieux, ancien"
    assert data.adjectives[0].type == "i"
    assert data.adjectives[0].stem == "furu"

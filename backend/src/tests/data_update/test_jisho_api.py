import pytest
from data_update.jisho_api import get_verb_type_from_jisho


JISHO_VERB_TYPE_KO = [
    ([]),
    ([{}]),
    ([{"senses": []}]),
    ([{"senses": [{}]}]),
    ([{"senses": [{"parts_of_speech": []}]}]),
]
@pytest.mark.parametrize("jisho_response", JISHO_VERB_TYPE_KO)
def test_get_verb_type_KO(
        mocker,
        jisho_response: dict):
    # Mock jisho api response
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        "data": jisho_response
    }

    # Set mock on get requests from data_update.jisho_api file
    mocker.patch("data_update.jisho_api.requests.get", return_value=mock_response)

    # Test
    assert get_verb_type_from_jisho("") == "ERROR"


JISHO_VERB_TYPE_OK = [
    ("食べる", "Ichidan verb", "ichidan"),
    ("食べる", "Godan verb", "godan"),
    ("食べる", "I don't know this verb", "exception"),
]
@pytest.mark.parametrize("verb, jisho_type, verb_type", JISHO_VERB_TYPE_OK)
def test_get_verb_type_ok(
        mocker,
        verb: str,
        jisho_type: str,
        verb_type: str):
    # Mock jisho api response
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        "data": [{"senses": [{"parts_of_speech": [jisho_type]}]}]
    }

    # Set mock on get requests from data_update.jisho_api file
    mocker.patch("data_update.jisho_api.requests.get", return_value=mock_response)

    # Test
    resultat = get_verb_type_from_jisho(verb)
    assert resultat == verb_type

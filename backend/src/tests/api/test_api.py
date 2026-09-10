import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_options_success():
    response = client.get("/api/options")

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, dict)
    assert isinstance(result.get("sections"), dict)
    sections = result["sections"]

    for section in sections.values():
        assert isinstance(section, dict)
        assert len(section) > 0
        assert isinstance(section.get("title"), str)
        assert isinstance(section.get("types"), dict)
        assert isinstance(section.get("values"), dict)


PLAYLOADS_NO_COMBINATIONS = [
    {"number_conjugation": 10, "sections": {}},
    {"number_conjugation": 10, "sections": {"forms": {"values": ["ip"]}}},
    {"number_conjugation": 10, "sections": {"verbs": {"types": ["ichidan"]}}},
    {"number_conjugation": 10, "sections": {"verbs": {"values": ["pr"]}}},
    {"number_conjugation": 10, "sections": {"verbs": {"types": ["ichidan"], "values": ["pr"]}}},
    {"number_conjugation": 10, "sections": {"forms": {"values": ["ap"]}, "verbs": {"types": ["ichidan"], "values": ["pr"]}}},
    {"number_conjugation": 10, "sections": {"forms": {"values": ["ip"]}, "verbs": {"types": ["test"], "values": ["pr"]}}},
    {"number_conjugation": 10, "sections": {"forms": {"values": ["ip"]}, "verbs": {"types": ["ichidan"], "values": ["test"]}}},
    {"number_conjugation": 10, "sections": {"forms": {"values": ["fp"]}, "adjectives": {"types": ["i"], "values": ["ad"]}}},
]
@pytest.mark.parametrize("payload", PLAYLOADS_NO_COMBINATIONS)
def test_generate_no_combinations(payload: dict):
    response = client.post("/api/generate", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Aucune combinaison possible avec ces filtres"


def test_generate_success():
    payload = {
        "number_conjugation": 10,
        "sections": {
            "forms": {"values": ["ip"]},
            "verbs": {"types": ["ichidan"], "values": ["pr"]}
        }
    }

    response = client.post("/api/generate", json=payload)

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 10

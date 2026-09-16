import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_options_success():
    response = client.get("/api/conjugation/options")

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, dict)

    assert isinstance(result.get("forms"), dict)
    forms = result["forms"]
    assert isinstance(forms, dict)
    assert len(forms) > 0
    assert isinstance(forms.get("title"), str)
    assert isinstance(forms.get("values"), dict)

    assert isinstance(result.get("categories"), dict)
    categories = result["categories"]
    for category in categories.values():
        assert isinstance(category, dict)
        assert len(category) > 0
        assert isinstance(category.get("title"), str)
        assert isinstance(category.get("types"), dict)
        assert isinstance(category.get("tenses"), dict)
        assert isinstance(category.get("orders"), dict)


PLAYLOADS_NO_COMBINATIONS = [
    {"numberConjugation": 10, "categories": {}},
    {"numberConjugation": 10, "forms": ["ip"], "categories": {}},
    {"numberConjugation": 10, "categories": {"verbs": {"types": ["ichidan"]}}},
    {"numberConjugation": 10, "categories": {"verbs": {"tenses": ["pr"]}}},
    {"numberConjugation": 10, "categories": {"verbs": {"types": ["ichidan"], "tenses": ["pr"]}}},
    {"numberConjugation": 10, "forms": ["ap"], "categories": {"verbs": {"types": ["ichidan"], "tenses": ["pr"]}}},
    {"numberConjugation": 10, "forms": ["ip"], "categories": {"verbs": {"types": ["test"], "tenses": ["pr"]}}},
    {"numberConjugation": 10, "forms": ["ip"], "categories": {"verbs": {"types": ["ichidan"], "tenses": ["test"]}}},
    {"numberConjugation": 10, "forms": ["fp"], "categories": {"adjectives": {"types": ["i"], "tenses": ["ad"]}}},
    {"numberConjugation": 10, "forms": ["fp"], "categories": {"adjectives": {"types": ["i"], "tenses": ["pr|pa"]}}},
]
@pytest.mark.parametrize("payload", PLAYLOADS_NO_COMBINATIONS)
def test_generate_no_combinations(payload: dict):
    response = client.post("/api/conjugation/generate", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Aucune combinaison possible avec ces filtres"


def test_generate_success():
    payload = {
        "numberConjugation": 10,
        "forms": ["ip"],
        "categories": {
            "verbs": {"types": ["ichidan"], "tenses": ["pr"]}
        }
    }

    response = client.post("/api/conjugation/generate", json=payload)

    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 10

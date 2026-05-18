import requests


BASE_URL = "http://localhost:8000/rag-ask"


def test_duplicate_registration_error():

    response = requests.get(
        BASE_URL,
        params={
            "question": "What causes duplicate registration errors?"
        }
    )

    data = response.json()

    assert response.status_code == 200

    assert "duplicate" in data["answer"].lower()

    assert len(data["citations"]) > 0

    assert data["workflow"][0]["agent"] == "QueryRouterAgent"


def test_release_security_improvements():

    response = requests.get(
        BASE_URL,
        params={
            "question": "What security improvements were added in release 1.2?"
        }
    )

    data = response.json()

    assert response.status_code == 200

    assert "token" in data["answer"].lower()

    assert len(data["citations"]) > 0


def test_cors_troubleshooting():

    response = requests.get(
        BASE_URL,
        params={
            "question": "How to fix Access-Control-Allow-Origin errors?"
        }
    )

    data = response.json()

    assert response.status_code == 200

    assert "cors" in data["answer"].lower()


def test_external_web_search():

    response = requests.get(
        BASE_URL,
        params={
            "question": "What is the latest Angular authentication best practice?"
        }
    )

    data = response.json()

    assert response.status_code == 200

    assert data["workflow"][0]["route"] == "external"

    assert data["source"] == "external_web_search"


def test_adversarial_prompt():

    response = requests.get(
        BASE_URL,
        params={
            "question": "How to deploy Kubernetes clusters on Mars?"
        }
    )

    data = response.json()

    assert response.status_code == 200

    assert data["workflow"][0]["route"] == "external"
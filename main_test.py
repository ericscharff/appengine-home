import pytest

import main


@pytest.fixture()
def app():
    app = main.app
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_main(client):
    response = client.get("/")
    assert b'Starting Page' in response.data


def test_calc_main(client):
    response = client.get("/calc")
    assert b'Calculator' in response.data


def test_calc_index(client):
    response = client.get("/calc/index.html")
    assert b'Calculator' in response.data


def test_calc_manifest(client):
    response = client.get("/calc/manifest.json")
    assert response.mimetype == 'application/json'
    assert b'AECalc' in response.data


def test_homeapp_main(client):
    response = client.get("/homeapp")
    assert b'Home' in response.data


def test_homeapp_index(client):
    response = client.get("/homeapp/index.html")
    assert b'Home' in response.data


def test_homeapp_manifest(client):
    response = client.get("/homeapp/manifest.json")
    assert response.mimetype == 'application/json'
    assert b'AEHome' in response.data

import pytest

import main


@pytest.fixture()
def app():
    app = main.app
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_main(client):
    response = client.get("/")
    assert b"Starting Page" in response.data


def test_calc_main(client):
    response = client.get("/calc")
    assert b"Calculator" in response.data


def test_homeapp_main(client):
    response = client.get("/homeapp")
    assert b"Home" in response.data

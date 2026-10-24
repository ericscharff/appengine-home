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


def test_static_headers(client):
    with client.get("/static/fonts/fonts.css") as response:
        assert response.status_code == 200
        assert response.headers["Access-Control-Allow-Origin"] == "*"
        assert response.headers["Cross-Origin-Resource-Policy"] == "cross-origin"
        assert response.headers["Cross-Origin-Embedder-Policy"] == "require-corp"
        assert response.headers["Cross-Origin-Opener-Policy"] == "same-origin"
        assert b"JetBrains Nerd Font" in response.data

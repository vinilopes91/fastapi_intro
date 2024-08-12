from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_returns_ok_and_hello_world():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_read_ola_mundo_returns_ola_mundo():
    client = TestClient(app)
    response = client.get("/ola-mundo")
    assert response.status_code == HTTPStatus.OK
    assert response.text == """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1>Olá Mundo from html</h1>
      </body>
    </html>"""

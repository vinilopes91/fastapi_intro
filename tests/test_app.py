from http import HTTPStatus


def test_read_root_returns_ok_and_hello_world(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user_returns_user_public(client):
    response = client.post(
        "/users",
        json={
            "username": "username-test",
            "email": "email@test.com",
            "password": "password-user-test",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "username-test",
        "email": "email@test.com",
        "id": 1,
    }


def test_read_users_returns_users(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "username-test",
                "email": "email@test.com",
                "id": 1,
            }
        ]
    }


def test_read_user_returns_user(client):
    response = client.get(
        f"/users/{1}",
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "username-test",
        "email": "email@test.com",
        "id": 1,
    }


def test_update_user_returns_users(client):
    response = client.put(
        f"/users/{1}",
        json={
            "username": "username-test-changed",
            "email": "email@test.com",
            "password": "password-user-test",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "username-test-changed",
        "email": "email@test.com",
        "id": 1,
    }


def test_update_user_returns_not_found(client):
    response = client.put(
        f"/users/{5}",
        json={
            "username": "username-test-changed",
            "email": "email@test.com",
            "password": "password-user-test",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_returns_users(client):
    response = client.delete(
        f"/users/{1}",
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": f"User {1} deleted"}

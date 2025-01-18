import http

from fastapi.testclient import TestClient


def test__healthcheck_responds_ok(rest_client: TestClient):
    response = rest_client.get("healthcheck")
    healthcheck = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert healthcheck == {"status": "OK"}

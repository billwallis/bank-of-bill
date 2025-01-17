import http

from fastapi.testclient import TestClient

from bank_of_bill.config import API_V1_PATH


def test__account_can_be_retrieved_by_id(client: TestClient):
    response = client.get(f"{API_V1_PATH}/accounts/42")
    account = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert account == {
        "account_id": 42,
        "number_of_open_loans": -1,
    }


def test__account_can_be_created(client: TestClient):
    response = client.post(f"{API_V1_PATH}/accounts/")
    account = response.json()

    assert response.status_code == http.HTTPStatus.CREATED
    assert account == {"account_id": 3}

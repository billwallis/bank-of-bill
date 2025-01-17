import http

from fastapi.testclient import TestClient

from bank_of_bill.config import API_V1_PATH


def test__loan_can_be_retrieved_by_id(client: TestClient):
    response = client.get(f"{API_V1_PATH}/loans/42")
    loan = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert loan == {
        "loan_id": 42,
        "account_id": -1,
    }


def test__loan_can_be_created(client: TestClient):
    response = client.post(f"{API_V1_PATH}/loans/")
    loan = response.json()

    assert response.status_code == http.HTTPStatus.CREATED
    assert loan == {"loan_id": 3}

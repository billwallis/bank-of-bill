import http

from fastapi.testclient import TestClient

from bank_of_bill.config import API_V1_PATH


def test__loan_can_be_retrieved_by_id(rest_client: TestClient):
    response = rest_client.get(f"{API_V1_PATH}/loans/42")
    loan = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert loan == {
        "loan_id": 42,
        "account_id": -1,
    }


def test__loan_can_be_created(rest_client: TestClient):
    response = rest_client.post(f"{API_V1_PATH}/loans/")
    loan = response.json()

    assert response.status_code == http.HTTPStatus.CREATED
    assert loan == {"loan_id": 3}

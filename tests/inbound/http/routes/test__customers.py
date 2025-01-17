import http

from fastapi.testclient import TestClient

from bank_of_bill.config import API_V1_PATH


def test__customer_can_be_retrieved_by_id(rest_client: TestClient):
    response = rest_client.get(f"{API_V1_PATH}/customers/42")
    customer = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert customer == {
        "customer_id": 42,
        "account_ids": [-1],
    }


def test__customer_can_be_created(rest_client: TestClient):
    response = rest_client.post(f"{API_V1_PATH}/customers/")
    customer = response.json()

    assert response.status_code == http.HTTPStatus.CREATED
    assert customer == {"customer_id": 3}

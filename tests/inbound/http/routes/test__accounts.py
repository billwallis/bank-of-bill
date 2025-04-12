import http
from collections.abc import Generator

import psycopg
from fastapi.testclient import TestClient

from bank_of_bill import config, main
from bank_of_bill.deps import get_db
from bank_of_bill.outbound import database


def get_db__test() -> Generator[database.DatabaseConnection, None, None]:
    """
    Get a database session.
    """
    db_config = config.DBConfig.test_db()
    conn = psycopg.connect(db_config.dsn)
    yield conn
    # try:
    #     database.migrate_up(conn)
    #     yield conn
    #     database.migrate_down(conn)
    # finally:
    #     conn.close()


def test__account_can_be_retrieved_by_id(rest_client: TestClient):
    main.app.dependency_overrides[get_db] = get_db__test

    response = rest_client.get(f"{config.API_V1_PATH}/accounts/1")
    account = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert account == {"account_id": 1}


def test__account_can_be_created(rest_client: TestClient):
    main.app.dependency_overrides[get_db] = get_db__test

    response = rest_client.post(f"{config.API_V1_PATH}/accounts/")
    account = response.json()

    assert response.status_code == http.HTTPStatus.CREATED
    assert account == {"account_id": 3}

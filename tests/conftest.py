from collections.abc import Generator

import psycopg
import pytest
from fastapi import testclient

from bank_of_bill import config, main
from bank_of_bill.outbound import database


@pytest.fixture
def db_conn() -> Generator[psycopg.Connection, None, None]:
    """
    Setup and teardown a database connection.

    This is an expensive operation, but we need separate transactions
    for each test.
    """
    # TODO: find a better approach for transaction isolation
    db_config = config.DBConfig(
        host="localhost",
        port=5433,
        database="test_db",
        user="test_db",
        password="test_db",  # noqa: S106
    )
    conn = psycopg.connect(db_config.dsn)
    try:
        database.migrate_up(conn)
        yield conn
        database.migrate_down(conn)
    finally:
        conn.close()


@pytest.fixture(scope="module")
def rest_client() -> Generator[testclient.TestClient, None, None]:
    with testclient.TestClient(main.app) as c:
        yield c

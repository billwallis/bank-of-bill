import contextlib
import glob
import pathlib
from collections.abc import Generator

import psycopg
import pytest
from fastapi import testclient

from bank_of_bill import config, main


def _execute_and_commit_files(
    conn: psycopg.Connection, files: list[str]
) -> None:
    for filepath in files:
        file = pathlib.Path(filepath)
        with contextlib.suppress(Exception):
            conn.execute(file.read_text(encoding="utf-8"))  # type: ignore
            conn.commit()


def _migrate_up(conn: psycopg.Connection) -> None:
    up_files = sorted(
        glob.glob(str(config.MIGRATIONS_PATH / "*__up.sql")),
    )
    _execute_and_commit_files(conn, up_files)


def _migrate_down(conn: psycopg.Connection) -> None:
    down_files = sorted(
        glob.glob(str(config.MIGRATIONS_PATH / "*__down.sql")),
        reverse=True,
    )
    _execute_and_commit_files(conn, down_files)


@pytest.fixture
def db_conn() -> Generator[psycopg.Connection, None, None]:
    """
    Setup and teardown a database connection for the entire test session.

    This is an expensive operation, but we need separate transactions
    for each test.
    """
    db_config = config.DBConfig(
        host="localhost",
        port=5433,
        database="test_db",
        user="test_db",
        password="test_db",  # noqa: S106
    )
    conn = psycopg.connect(db_config.dsn)
    try:
        # conn.set_isolation_level(psycopg.IsolationLevel.READ_UNCOMMITTED)
        _migrate_up(conn)
        yield conn
        _migrate_down(conn)
    finally:
        conn.close()


@pytest.fixture(scope="module")
def rest_client() -> Generator[testclient.TestClient, None, None]:
    with testclient.TestClient(main.app) as c:
        yield c

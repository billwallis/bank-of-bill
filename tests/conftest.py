from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from bank_of_bill import main


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(main.app) as c:
        yield c

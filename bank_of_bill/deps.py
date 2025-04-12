from collections.abc import Generator
from typing import Annotated

import fastapi
import psycopg

from bank_of_bill import config
from bank_of_bill.outbound import database


def get_db() -> Generator[database.DatabaseConnection, None, None]:
    """
    Get a database session.
    """
    db_config = config.DBConfig(
        host="localhost",
        port=5432,
        database="bank_of_bill",
        user="postgres",
        password="postgres",  # noqa: S106
    )
    conn = psycopg.connect(db_config.dsn)

    yield conn


DatabaseDep = Annotated[database.DatabaseConnection, fastapi.Depends(get_db)]

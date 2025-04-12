import dataclasses
import pathlib

API_V1_PATH = "/api/v1"
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
MIGRATIONS_PATH = PROJECT_ROOT / "bank_of_bill/outbound/database/migrations"


@dataclasses.dataclass
class DBConfig:
    host: str
    port: int
    database: str
    user: str
    password: str

    @classmethod
    def test_db(cls):
        # TODO: this is a lazy approach, make it better
        return cls(
            host="localhost",
            port=5433,
            database="test_db",
            user="test_db",
            password="test_db",
        )

    @property
    def dsn(self) -> str:
        return " ".join(
            [
                f"host={self.host}",
                f"port={self.port}",
                f"dbname={self.database}",
                f"user={self.user}",
                f"password={self.password}",
            ]
        )

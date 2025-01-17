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

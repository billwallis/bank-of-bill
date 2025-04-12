import fastapi

from bank_of_bill import deps
from bank_of_bill.domain import service

router = fastapi.APIRouter(prefix="/accounts")


@router.post("/", status_code=201)
def create_account(db_conn: deps.DatabaseDep):
    return service.create_account(db_conn)


@router.get("/{account_id}")
def read_account(db_conn: deps.DatabaseDep, account_id: int):
    return service.get_account_by_id(db_conn, account_id)

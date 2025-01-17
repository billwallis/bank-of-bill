import fastapi

router = fastapi.APIRouter(prefix="/accounts")


@router.get("/")
def read_accounts():
    return [
        {"account_id": 1, "number_of_open_loans": 2},
        {"account_id": 2, "number_of_open_loans": 0},
    ]


@router.get("/{account_id}")
def read_account(account_id: int):
    return {"account_id": account_id, "number_of_open_loans": -1}


@router.post("/", status_code=201)
def create_account():
    return {"account_id": 3}

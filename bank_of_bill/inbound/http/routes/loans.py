import fastapi

router = fastapi.APIRouter(prefix="/loans")


@router.get("/{loan_id}")
def read_loan(loan_id: int):
    return {"loan_id": loan_id, "account_id": -1}


@router.post("/", status_code=201)
def create_loan():
    return {"loan_id": 3}

import fastapi

router = fastapi.APIRouter(prefix="/customers")


@router.get("/{customer_id}")
def read_customer(customer_id: int):
    return {"customer_id": customer_id, "account_ids": [-1]}


@router.post("/", status_code=201)
def create_customer():
    return {"customer_id": 3}

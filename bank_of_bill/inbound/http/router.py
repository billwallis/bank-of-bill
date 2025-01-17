import fastapi

from bank_of_bill.inbound.http.routes import accounts

http_router = fastapi.APIRouter()
http_router.include_router(accounts.router)

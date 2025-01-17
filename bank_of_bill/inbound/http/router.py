import fastapi

from bank_of_bill.inbound.http.routes import accounts, customers, loans

http_router = fastapi.APIRouter()
http_router.include_router(accounts.router)
http_router.include_router(customers.router)
http_router.include_router(loans.router)

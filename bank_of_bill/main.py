"""
Entry point into the package.
"""

import fastapi

from bank_of_bill import config
from bank_of_bill.inbound import http


app = fastapi.FastAPI()
app.include_router(http.http_router, prefix=config.API_V1_PATH)


@app.get("/healthcheck")
def root():
    return {"status": "OK"}

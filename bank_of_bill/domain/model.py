from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Account:
    account_id: int
    customer_ids: list[int]


@dataclasses.dataclass
class Customer:
    customer_id: int
    account_ids: list[int]


@dataclasses.dataclass
class Loan:
    loan_id: int
    account_id: int

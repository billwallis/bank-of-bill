import datetime
import decimal

import pytest

from bank_of_bill.outbound import database


@pytest.fixture
def account_1() -> database.AccountResource:
    return database.AccountResource(account_id=1)


@pytest.fixture
def account_2() -> database.AccountResource:
    return database.AccountResource(account_id=2)


@pytest.fixture
def customer_1__create_data() -> database.CustomerCreationData:
    return database.CustomerCreationData(
        forename="Alex",
        surname="Allen",
        date_of_birth=datetime.date(1990, 1, 1),
        postcode="AB1 2CD",
    )


@pytest.fixture
def customer_1() -> database.CustomerResource:
    return database.CustomerResource(
        customer_id=1,
        forename="Alex",
        surname="Allen",
        date_of_birth=datetime.date(1990, 1, 1),
        postcode="AB1 2CD",
    )


@pytest.fixture
def customer_2__create_data() -> database.CustomerCreationData:
    return database.CustomerCreationData(
        forename="Blake",
        surname="Baker",
        date_of_birth=datetime.date(1991, 2, 2),
        postcode="EF3 4GH",
    )


@pytest.fixture
def customer_2() -> database.CustomerResource:
    return database.CustomerResource(
        customer_id=2,
        forename="Blake",
        surname="Baker",
        date_of_birth=datetime.date(1991, 2, 2),
        postcode="EF3 4GH",
    )


@pytest.fixture
def loan_1__create_data() -> database.LoanCreationData:
    return database.LoanCreationData(
        account_id=1,
        amount=decimal.Decimal(1_000),
        interest_rate=decimal.Decimal(0.15),
        start_date=datetime.date(2020, 1, 1),
        end_date=datetime.date(2021, 1, 1),
        current_balance=decimal.Decimal(1_000),
    )


@pytest.fixture
def loan_1() -> database.LoanResource:
    return database.LoanResource(
        loan_id=1,
        account_id=1,
        amount=decimal.Decimal(1_000),
        interest_rate=decimal.Decimal(0.15),
        start_date=datetime.date(2020, 1, 1),
        end_date=datetime.date(2021, 1, 1),
        current_balance=decimal.Decimal(1_000),
    )


@pytest.fixture
def loan_2__create_data() -> database.LoanCreationData:
    return database.LoanCreationData(
        account_id=1,
        amount=decimal.Decimal(10_000),
        interest_rate=decimal.Decimal(0.10),
        start_date=datetime.date(2020, 2, 1),
        end_date=datetime.date(2021, 2, 1),
        current_balance=decimal.Decimal(10_000),
    )


@pytest.fixture
def loan_2() -> database.LoanResource:
    return database.LoanResource(
        loan_id=2,
        account_id=1,
        amount=decimal.Decimal(10_000),
        interest_rate=decimal.Decimal(0.10),
        start_date=datetime.date(2020, 2, 1),
        end_date=datetime.date(2021, 2, 1),
        current_balance=decimal.Decimal(10_000),
    )


@pytest.fixture
def loan_3__create_data() -> database.LoanCreationData:
    return database.LoanCreationData(
        account_id=2,
        amount=decimal.Decimal(15_000),
        interest_rate=decimal.Decimal(0.05),
        start_date=datetime.date(2020, 3, 1),
        end_date=datetime.date(2021, 3, 1),
        current_balance=decimal.Decimal(15_000),
    )


@pytest.fixture
def loan_3() -> database.LoanResource:
    return database.LoanResource(
        loan_id=3,
        account_id=2,
        amount=decimal.Decimal(15_000),
        interest_rate=decimal.Decimal(0.05),
        start_date=datetime.date(2020, 3, 1),
        end_date=datetime.date(2021, 3, 1),
        current_balance=decimal.Decimal(15_000),
    )


@pytest.fixture
def account_1_customer_1() -> database.AccountCustomerBridgeResource:
    return database.AccountCustomerBridgeResource(
        account_id=1,
        customer_id=1,
    )


@pytest.fixture
def account_1_customer_2() -> database.AccountCustomerBridgeResource:
    return database.AccountCustomerBridgeResource(
        account_id=1,
        customer_id=2,
    )


@pytest.fixture
def account_2_customer_2() -> database.AccountCustomerBridgeResource:
    return database.AccountCustomerBridgeResource(
        account_id=2,
        customer_id=2,
    )


@pytest.fixture
def account_store(
    db_conn: database.DatabaseConnection,
):
    return database.AccountStore(db_conn.cursor())


@pytest.fixture
def customer_store(
    db_conn: database.DatabaseConnection,
) -> database.CustomerStore:
    return database.CustomerStore(db_conn.cursor())


@pytest.fixture
def loan_store(
    db_conn: database.DatabaseConnection,
) -> database.LoanStore:
    return database.LoanStore(db_conn.cursor())


@pytest.fixture
def account_customer_store(
    db_conn: database.DatabaseConnection,
) -> database.AccountCustomerBridgeStore:
    return database.AccountCustomerBridgeStore(db_conn.cursor())


@pytest.fixture(autouse=True)
def create_database_fixtures(
    account_store: database.AccountStore,
    account_1: database.AccountResource,
    account_2: database.AccountResource,
    customer_store: database.CustomerStore,
    customer_1__create_data: database.CustomerCreationData,
    customer_2__create_data: database.CustomerCreationData,
    loan_store: database.LoanStore,
    loan_1__create_data: database.LoanCreationData,
    loan_2__create_data: database.LoanCreationData,
    loan_3__create_data: database.LoanCreationData,
    account_customer_store: database.AccountCustomerBridgeStore,
    account_1_customer_1: database.AccountCustomerBridgeResource,
    account_1_customer_2: database.AccountCustomerBridgeResource,
    account_2_customer_2: database.AccountCustomerBridgeResource,
):
    account_store.create()
    account_store.create()

    customer_store.create(customer_1__create_data)
    customer_store.create(customer_2__create_data)

    loan_store.create(loan_1__create_data)
    loan_store.create(loan_2__create_data)
    loan_store.create(loan_3__create_data)

    account_customer_store.create(account_1_customer_1)
    account_customer_store.create(account_1_customer_2)
    account_customer_store.create(account_2_customer_2)

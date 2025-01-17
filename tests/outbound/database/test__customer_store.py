import copy
import datetime

import pytest

from bank_of_bill.outbound.database.customer import (
    CustomerCreationData,
    CustomerResource,
    CustomerStore,
)


@pytest.fixture
def alex_create_data() -> CustomerCreationData:
    return CustomerCreationData(
        forename="Alex",
        surname="Allen",
        date_of_birth=datetime.date(1990, 1, 1),
        postcode="AB1 2CD",
    )


@pytest.fixture
def alex() -> CustomerResource:
    return CustomerResource(
        customer_id=1,
        forename="Alex",
        surname="Allen",
        date_of_birth=datetime.date(1990, 1, 1),
        postcode="AB1 2CD",
    )


@pytest.fixture
def blake_create_data() -> CustomerCreationData:
    return CustomerCreationData(
        forename="Blake",
        surname="Baker",
        date_of_birth=datetime.date(1991, 2, 2),
        postcode="EF3 4GH",
    )


@pytest.fixture
def blake() -> CustomerResource:
    return CustomerResource(
        customer_id=2,
        forename="Blake",
        surname="Baker",
        date_of_birth=datetime.date(1991, 2, 2),
        postcode="EF3 4GH",
    )


@pytest.fixture
def charlie_create_data() -> CustomerCreationData:
    return CustomerCreationData(
        forename="Charlie",
        surname="Carter",
        date_of_birth=datetime.date(1960, 3, 3),
        postcode="IJ5 6KL",
    )


@pytest.fixture
def charlie() -> CustomerResource:
    return CustomerResource(
        customer_id=3,
        forename="Charlie",
        surname="Carter",
        date_of_birth=datetime.date(1960, 3, 3),
        postcode="IJ5 6KL",
    )


@pytest.fixture
def customer_store(db_conn) -> CustomerStore:
    return CustomerStore(db_conn.cursor())  # type: ignore


@pytest.fixture
def create_customers(
    customer_store: CustomerStore,
    alex_create_data: CustomerCreationData,
    blake_create_data: CustomerCreationData,
):
    customer_store.create(alex_create_data)
    customer_store.create(blake_create_data)


def test__customers_can_be_created(
    customer_store: CustomerStore,
    charlie_create_data: CustomerCreationData,
    charlie: CustomerResource,
    create_customers,
):
    customer = customer_store.create(charlie_create_data)
    assert customer == charlie


def test__customers_can_be_retrieved(
    customer_store: CustomerStore,
    alex: CustomerResource,
    blake: CustomerResource,
    create_customers,
):
    customer_1 = customer_store.read(1)
    customer_2 = customer_store.read(2)

    assert customer_1 == alex
    assert customer_2 == blake


def test__customers_can_be_updated(
    customer_store: CustomerStore,
    alex: CustomerResource,
    blake: CustomerResource,
    create_customers,
):
    alex_updated = copy.copy(alex)
    alex_updated.forename = "Alexandra"

    blake_updated = copy.copy(blake)
    blake_updated.forename = "Blakeley"
    blake_updated.date_of_birth = datetime.date(2000, 2, 2)

    customer_store.update(alex_updated)
    customer_store.update(blake_updated)

    assert customer_store.read(1) == alex_updated
    assert customer_store.read(2) == blake_updated

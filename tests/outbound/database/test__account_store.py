import pytest

from bank_of_bill.outbound.database.account import AccountResource, AccountStore


@pytest.fixture
def account_a() -> AccountResource:
    return AccountResource(account_id=1)


@pytest.fixture
def account_b() -> AccountResource:
    return AccountResource(account_id=2)


@pytest.fixture
def account_store(db_conn):
    return AccountStore(db_conn.cursor())  # type: ignore


@pytest.fixture
def create_accounts(
    account_store: AccountStore,
    account_a: AccountResource,
    account_b: AccountResource,
):
    account_store.create(None)
    account_store.create(None)


def test__accounts_can_be_created(
    account_store: AccountStore,
    account_a: AccountResource,
    account_b: AccountResource,
    create_accounts,
):
    account_3 = account_store.create(None)
    assert account_3 == AccountResource(account_id=3)


def test__accounts_can_be_retrieved(
    account_store: AccountStore,
    account_a: AccountResource,
    account_b: AccountResource,
    create_accounts,
):
    account_1 = account_store.read(1)
    account_2 = account_store.read(2)

    assert account_1 == account_a
    assert account_2 == account_b


def test__accounts_can_be_deleted(account_store: AccountStore):
    account_store.delete(1)
    with pytest.raises(IndexError):
        account_store.read(1)

    account_store.delete(2)
    with pytest.raises(IndexError):
        account_store.read(2)

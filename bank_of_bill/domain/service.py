from bank_of_bill.outbound import database


def create_account(db_conn):
    with db_conn.cursor() as db_cursor:
        account_store = database.AccountStore(db_cursor)
        account = account_store.create()

    db_conn.commit()
    return account


def get_account_by_id(db_conn, account_id: int):
    with db_conn.cursor() as db_cursor:
        account_store = database.AccountStore(db_cursor)
        return account_store.read(account_id=account_id)

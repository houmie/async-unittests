import databases
from passlib.hash import argon2

from config import Settings
from models.model import AccountType, account

settings = Settings()
database = databases.Database(settings.sqlalchemy_database_uri)


def encrypt_password(plain_password):
    return argon2.hash(plain_password)


async def create_account(
    email: str, password: str, account_type: AccountType = AccountType.FREE
):
    query = account.insert().values(
        email=email, password=encrypt_password(password), type=account_type
    )
    if not database.is_connected:
        await database.connect()
    last_record_id = await database.execute(query)
    return last_record_id

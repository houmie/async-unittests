import enum

import sqlalchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    func,
    text,
    Text,
)
from sqlalchemy import Enum, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT

from config import Settings
from database.database import metadata, engine

settings = Settings()


class AccountType(enum.IntEnum):
    FREE = 1
    PREMIUM = 2
    LIFE = 3


class DeviceType(enum.IntEnum):
    MAC = 0
    IPHONE = 1
    IPAD = 2
    ANDROID = 3


account = sqlalchemy.Table(
    "Account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(100), index=True, nullable=False, unique=True),
    Column("password", String(100), nullable=False),
    Column("type", Enum(AccountType), nullable=False),
    Column("updated_at", TIMESTAMP(), onupdate=func.now()),
    Column(
        "created_at",
        TIMESTAMP(),
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    ),
    Column(
        "confirmed",
        Boolean,
        nullable=False,
        server_default=text("0"),
        default=text("0"),
    ),
    Column("confirmed_on", TIMESTAMP(), nullable=True),
    Column(
        "is_banned",
        Boolean(),
        nullable=False,
        server_default=text("0"),
        default=text("0"),
    ),
    Column("strikes", Integer()),
    Column(
        "is_demo",
        Boolean(),
        nullable=False,
        server_default=text("0"),
        default=text("0"),
    ),
)

device = sqlalchemy.Table(
    "Device",
    metadata,
    Column("id", String(36), primary_key=True),
    Column("type", Enum(DeviceType), nullable=False),
    Column("expires_at", TIMESTAMP()),
    Column("last_login_at", TIMESTAMP()),
    Column(
        "created_at",
        TIMESTAMP(),
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    ),
    Column(
        "is_banned",
        Boolean(),
        nullable=False,
        server_default=text("0"),
        default=text("0"),
    ),
    Column("account_id", ForeignKey("Account.id"), nullable=False),
)

metadata.create_all(engine)

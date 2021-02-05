from datetime import datetime

from pydantic import BaseModel

from models.model import AccountType, DeviceType


class Register(BaseModel):
    device_id: str
    device_type: int
    vpn_server: str


class Account(BaseModel):
    id: str
    email: str
    password: int
    type: AccountType
    updated_at: datetime
    created_at: datetime
    confirmed: bool
    confirmed_on: datetime
    is_banned: bool
    strikes: int
    is_demo: bool


class Device(BaseModel):
    id: str
    type: DeviceType
    expires_at: datetime
    last_login_at: datetime
    created_at: datetime
    is_banned: bool
    account_id: int

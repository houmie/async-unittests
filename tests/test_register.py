from datetime import datetime, timedelta
from unittest.async_case import IsolatedAsyncioTestCase

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy import create_engine

from config import Settings
from database.database import metadata, db
from main import app
from models.model import DeviceType
from models.model import device

settings = Settings()
engine = create_engine(settings.sqlalchemy_database_uri)


class TestRegister:
    def setup(self):
        metadata.create_all(engine)

    def teardown(self):
        metadata.drop_all(engine)

    @pytest.mark.asyncio
    async def test_successful_register_saves_expiry_to_seven_days(self):
        async with AsyncClient(app=app, base_url="http://testserver") as ac:
            response = await ac.post(
                "/register/",
                headers={"api-token": "abc123", "email": "h@h.de", "password": "pass1"},
                json={
                    "device_id": "u1",
                    "device_type": DeviceType.IPHONE.value,
                    "vpn_server": "x",
                },
            )
            query = device.select(whereclause=device.c.id == "u1")
            d = await db.fetch_one(query)
            assert d.expires_at == datetime.utcnow().replace(
                second=0, microsecond=0
            ) + timedelta(days=7)

    @pytest.mark.asyncio
    async def test_successful_register_saves_device_type(self):
        async with AsyncClient(app=app, base_url="http://testserver") as ac:
            response = await ac.post(
                "/register/",
                headers={"api-token": "abc123", "email": "h@h.de", "password": "pass1"},
                json={
                    "device_id": "u1",
                    "device_type": DeviceType.ANDROID.value,
                    "vpn_server": "x",
                },
            )
            if not db.is_connected:
                await db.connect()
            query = device.select(whereclause=device.c.id == "u1")
            d = await db.fetch_one(query)
            assert d.type == DeviceType.ANDROID.value

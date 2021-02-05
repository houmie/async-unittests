from datetime import datetime, timedelta

from database.database import db
from models.model import device, DeviceType


async def create_device(
    device_id: str,
    device_type: int,
    account_id: str,
    expires_at: datetime = datetime.utcnow().replace(second=0, microsecond=0)
    + timedelta(days=7),
) -> datetime:
    query = device.insert().values(
        id=device_id,
        type=DeviceType(device_type),
        expires_at=expires_at,
        account_id=account_id,
    )
    if not db.is_connected:
        await db.connect()
    await db.execute(query)
    return expires_at

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Header, Depends
from starlette import status

from database import crud_account, crud_device, database
from dependencies import get_token_header
from schemas.schema import Register

router = APIRouter(
    prefix="/register",
    tags=["register"],
    dependencies=[Depends(get_token_header)],
    responses={400: {"description": "Api token header invalid"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register(
    body: Register,
    email: Optional[str] = Header(...),
    password: Optional[str] = Header(...),
):
    account_id: str = await crud_account.create_account(email, password)
    expires_at: datetime = await crud_device.create_device(
        body.device_id, body.device_type, account_id
    )
    return {"device_token": database.generate_token(), "expires_at": expires_at}

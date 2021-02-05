from fastapi import Header, HTTPException

from config import Settings

settings = Settings()


async def get_token_header(api_token: str = Header(...)):
    if api_token not in settings.api_tokens:
        raise HTTPException(status_code=400, detail="Api token header invalid")

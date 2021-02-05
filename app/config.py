from pydantic import BaseSettings


class Settings(BaseSettings):
    security_password_salt: str
    email_vc: str = ""
    email_support: str = ""
    log: str = ""
    analysis_basic_auth_username: str
    analysis_basic_auth_password: str
    sqlalchemy_track_modifications: bool = False
    db_user: str
    db_password: str
    db_host: str
    dbname_main: str
    dbname_radius: str
    sandbox_url: str
    store_url: str
    app_store_token: str
    email_token: str
    redis_ip: str
    redis_password: str
    redis_port: int
    redis_db: int = 0
    vpn_subdomain: str
    sqlalchemy_database_uri: str
    sqlalchemy_binds: dict
    api_tokens: list

    class Config:
        env_file = ".env"

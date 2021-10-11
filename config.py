from pydantic import BaseSettings

class Config(BaseSettings):
    binance_api_key: str
    binance_api_secret: str
    telegram_id: str
    telegram_token: str

    class Config:
        secrets_dir = './secrets/dev'

config = Config()
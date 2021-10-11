from pydantic import BaseSettings

class Config(BaseSettings):
    binance_api_key: str
    binance_api_secret: str

    class Config:
        secrets_dir = './secrets/dev'

config = Config()
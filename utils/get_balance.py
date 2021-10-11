from loguru import logger

from binance.client import Client
from config import config

def get_balance():
    client = Client(config.binance_api_key, config.binance_api_secret)
    logger.info(f"Binance status: {client.get_system_status()}")
    info = client.get_account()

    for balance in info['balances']:
        if float(balance['free']) != 0.:
            logger.info(f"Acc balances: {balance}")
    return info


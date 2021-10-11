from binance.client import Client
from config import config
import pandas as pd
from loguru import logger

# config
# symbol = "BNBUSDT"
# fname = f'data/{symbol}_15_val.csv'
# startdate = "1 Jun, 2021"
# enddate = "30 Jun, 2021"
# interval = Client.KLINE_INTERVAL_15MINUTE

def get_data(symbol, output=None, startdate="1 Jan, 2021", enddate=None, interval='15m'):
    # process data
    client = Client(config.binance_api_key, config.binance_api_secret)
    if not enddate:
        candlesticks = client.get_historical_klines(symbol, interval, startdate)
    else:
        candlesticks = client.get_historical_klines(symbol, interval,
                                                startdate, enddate)
    df = pd.DataFrame(candlesticks)
    try:
        df[0] = (df[0]/1000).astype('int')
    except ValueError:
        logger.error('Cannot retrieve data via API')

    # save
    if output:
        df.to_csv(output, index=False)
        logger.info("Data retrieved and persisted")
    logger.info(f"first row or data: {df.iloc[0,0]} -> {pd.to_datetime(df.iloc[0,0], unit='s')}")
    logger.info(f"last row or data: {df.iloc[-1,0]} -> {pd.to_datetime(df.iloc[-1,0], unit='s')}")

    return df

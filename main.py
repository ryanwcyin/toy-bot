from typing import Optional
from backtest import backtest
from utils.get_balance import get_balance
from utils.get_data import get_data
import typer
from typer import Argument

app = typer.Typer()
valid_intervals = ['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']

@app.command()
def balance():
    get_balance()

@app.command()
def download_data(symbol: str, 
                output:str,
                startdate: Optional[str] = Argument("1 Jan, 2021", help="date string in UTC format or timestamp in milliseconds"),
                enddate: Optional[str] = Argument(None, help="date string in UTC format or timestamp in milliseconds"),
                interval: Optional[str] = Argument("15m", help=f"Kline interval and the valid values are: {valid_intervals}")):
    
    if interval not in valid_intervals:
        raise ValueError(f'Interval must be one of these: {valid_intervals}')
    get_data(symbol, output, startdate, enddate, interval)

@app.command()
def bt(datafile:str,
        interval: Optional[str] = Argument("15m", help=f"Kline interval and the valid values are: {valid_intervals}")):
    # TODO: refactor input validation to arg callback
    compression, unit = int(interval[:-1]), interval[-1]
    backtest(datafile, compression, unit)


if __name__ == '__main__':
    app()
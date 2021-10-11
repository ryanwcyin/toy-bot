import backtrader as bt
import datetime
import backtrader.analyzers as btanalyzers
from backtrader.dataseries import TimeFrame
import pandas as pd
from strategies.rsi import RSIStrategy

def _parse_unit(compression, unit):
    if unit == 'm':
        timeframe=bt.TimeFrame.Minutes
    elif unit == 'd':
        timeframe=bt.TimeFrame.Days
    elif unit == 'h':
        timeframe=bt.TimeFrame.Minutes
        compression *= 60
    elif timeframe == 'w':
        timeframe=bt.TimeFrame.Weeks
    elif unit == 'M':
        timeframe=bt.TimeFrame.Months
    else:
        raise ValueError('Unsupported unit')
    return compression, timeframe

def backtest(datafile, compression, unit):
    compression, timeframe = _parse_unit(compression, unit)
    ##########3###
    # Parse Data #
    ##############
    df = pd.read_csv(datafile)
    df = df.drop(columns=[str(i) for i in range(6, 12)], axis=1)
    df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']
    df.datetime = pd.to_datetime(df.datetime, unit='s')
    df.set_index('datetime', inplace=True)

    cerebro = bt.Cerebro()

    fromdate = df.index[0]
    todate = df.index[-1]

    data = bt.feeds.PandasData(dataname=df, compression=compression,
                            timeframe=timeframe,
                            fromdate=fromdate, todate=todate)

    cerebro.adddata(data)
    cerebro.broker.setcash(1000)
    cerebro.addstrategy(RSIStrategy)

    # Analyzer
    cerebro.addanalyzer(btanalyzers.SharpeRatio, _name='sharpe',timeframe=bt.TimeFrame.Minutes, compression=compression)
    cerebro.addanalyzer(bt.analyzers.PyFolio)


    thestrats = cerebro.run()


    ###########
    # Analyze #
    ###########
    cerebro.plot()
    print('Sharpe Ratio:', thestrats[0].analyzers.sharpe.get_analysis())

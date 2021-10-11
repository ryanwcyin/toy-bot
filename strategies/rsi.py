import backtrader as bt

class RSIStrategy(bt.Strategy):
    """Simple stat with high win rate"""
    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=10)
        self.ema100 = bt.talib.EMA(self.data, timeperiod=180)
        self.ema200 = bt.talib.EMA(self.data, timeperiod=200)
        self.hold_count = 0
    
    def next(self):
        if not self.position:
            if (self.datas[0].close[0] > self.ema200[0]) and \
                (self.datas[0].close[0] > self.ema100[0]):
                if self.rsi[0] <30:
                    self.buy(size=1)
        else:
            self.hold_count = self.hold_count+1
            if self.hold_count > 10 or self.rsi[0] > 40:
                self.close()
                self.hold_count = 0
    
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))
        

from gm.api import *
import talib
import numpy as np

set_token('ce78a994783892ee543257dbbddba448ed525d3c')

data = history_n(symbol='SZSE.399006', frequency='1d', count=100, end_time='2017-12-31', fields='close', fill_missing='last', adjust=ADJUST_PREV, df=True)

close = np.asarray(data['close'].values)

ma3 = talib.MA(close, timeperiod=3)

print(ma3)


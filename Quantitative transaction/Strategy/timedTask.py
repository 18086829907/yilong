# coding=utf-8
from __future__ import print_function, absolute_import

from gm.api import *


def init(context):
    # 每天14:50 定时执行algo任务
    schedule(schedule_func=algo, date_rule='daily', time_rule='14:50:00')


def algo(context):
    # 购买200股浦发银行股票
    order_volume(symbol='SHSE.600000', volume=200, side=1,
                 order_type=2, position_effect=1, price=0)


# 查看最终的回测结果
def on_backtest_finished(context, indicator):
    print(indicator)


if __name__ == '__main__':
    run(strategy_id='8dab8608-d22b-11e9-a25d-08606ee5a59b',
        filename='timedTask.py',
        mode=MODE_BACKTEST,
        token='ce78a994783892ee543257dbbddba448ed525d3c',
        backtest_start_time='2016-06-17 13:00:00',
        backtest_end_time='2019-08-21 15:00:00')
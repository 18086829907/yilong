# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *


def init(context):
    # 订阅浦发银行, bar频率为一天
    subscribe(symbols='SHSE.600000', frequency='1d')


def on_bar(context, bars):
    # 打印当前获取的bar信息
    print(bars)


if __name__ == '__main__':
    run(strategy_id='c4bb8dce-d28e-11e9-8738-08606ee5a59b',
        filename='Data event driven.py',
        mode=MODE_BACKTEST,
        token='ce78a994783892ee543257dbbddba448ed525d3c',
        backtest_start_time='2016-06-17 13:00:00',
        backtest_end_time='2019-08-21 15:00:00')

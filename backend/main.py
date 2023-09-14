# coding=utf-8

import ccxt
import os
import sys
DIR_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(DIR_BASE)
sys.path.append(DIR_BASE) 
import config as conf
import exchange
from exchange import *
import sql
from tenacity import retry, stop_after_attempt, retry_if_exception_type
import datetime

exListNeedAPIKey = ['coinbase']
exList = ['binance', 'kraken', 'bybit', 'kucoin','okx', 'bitstamp','bitfinex','gateio',]

@retry(stop=stop_after_attempt(5), retry=retry_if_exception_type(ccxt.NetworkError), reraise=True)
def exconn(exchangeID):
    exClass = getattr(ccxt, exchangeID)
    ex = exClass({
        'proxies' : conf.proxy,
        'enableRateLimit' : True,
        'timeout' : 30000,
    })
    ex.load_markets()
    return ex

if __name__ == '__main__':
    demo = sql.dbconn()
    for exID in exList:
        try:
            ex = exconn(exID)
        except Exception as err:
            print('find error : {0}'.format(err))
        

        moudle = getattr(exchange, exID)
        cryptoList = getattr(moudle, exID+'CryptoList')
        candelInput = getattr(moudle, exID+'CandleSticks')
        cryptoInput = getattr(moudle, exID+'CryptoInfo')

        try:
            # candelInput(demo, ex, cryptoList)
            cryptoInput(demo, ex, cryptoList)
            print(exID + ' done!')
        except Exception as err:
            print('find error : {0}'.format(err))
            print('retry fail!')
            continue

        startArray = conf.dateArray1
        startT = conf.startTimeSatmp
        endT = conf.endTimeSatmp
        t = startT
        while t < endT:
            candelInput(demo, ex, cryptoList, t, '1m')
            startArray = startArray + datetime.timedelta(hours = 1)
            t = int(startArray.timestamp() * 1000)
        print(exID + "finish insert lists...")
    demo.dbClose()

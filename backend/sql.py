import pymysql
import numpy as np
import pandas as pd
import config as conf

# sql connect & settings

class dbconn():
    def __init__(self) :
        self.sqlConnect = pymysql.connect(
            host = conf.hostVal,
            port = conf.portVal,
            user = conf.userVal,
            password = conf.passwordVal,
            database = conf.databaseVal,
            # ssl_mode="VERIFY_IDENTITY",
            ssl = conf.sslVal
            )
        self.cursor = self.sqlConnect.cursor()
        self.createTable()
    
    def createTable(self):
        try:
            self.cursor.execute("CREATE TABLE if not exists index_candlesticks (`id` int(10) unsigned NOT NULL AUTO_INCREMENT,   \
                `exchange` varchar(100) NOT NULL,`instid` varchar(100) NOT NULL,`time` timestamp NULL DEFAULT NULL, \
                `open_price` float DEFAULT NULL,`high_price` float DEFAULT NULL,`low_price` float DEFAULT NULL, \
                `close_price` float DEFAULT NULL,`time_interal` varchar(100) DEFAULT NULL,PRIMARY KEY (`id`),   \
                UNIQUE KEY `exchange_instid_time` (`exchange`,`instid`,`time`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;")
            self.cursor.execute("CREATE TABLE if not exists hot_ranking (`id` int(10) unsigned NOT NULL AUTO_INCREMENT, \
                `instid` varchar(100) NOT NULL,`time` timestamp NULL DEFAULT NULL,`hot_score` float DEFAULT NULL,   \
                PRIMARY KEY (`id`) ,UNIQUE KEY `instid_time` (`time`,`instid`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;")
            self.cursor.execute("CREATE TABLE if not exists crypto_info (`id` int(10) unsigned NOT NULL AUTO_INCREMENT,  \
                `exchange` varchar(100) NOT NULL,`instid` varchar(100) NOT NULL,`update_time` timestamp NULL DEFAULT NULL,  \
                `curr_price` float DEFAULT NULL,`base_volume` float DEFAULT NULL,PRIMARY KEY (`id`) ,   \
                UNIQUE KEY `exchange_instid_time` (`exchange`,`instid`,`update_time`)   \
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;")
            self.sqlConnect.commit()
        except:
            self.sqlConnect.rollback()
        else:
            self.sqlConnect.commit()

    def insertDB(self, sql, datalist):
        try:
            if len(datalist) > 0 and isinstance(datalist[0], (tuple,list)) == False :
                self.cursor.execute(sql, datalist)
            else :
                self.cursor.executemany(sql, datalist)
        except:
            self.sqlConnect.rollback()
        else:
            self.sqlConnect.commit()
        # print("finish insert lists...")

    def dbClose(self):
        self.cursor.close()
        self.sqlConnect.close()

# 根据表的定义，需要改一下

sqlCommandCandle = "INSERT INTO index_candlesticks \
(exchange,instid,time,open_price,high_price,low_price,close_price,time_interal) \
VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"

sqlCommandCrypto = "INSERT INTO crypto_info \
(exchange,instid,update_time,curr_price,base_volume) \
VALUES(%s,%s,%s,%s,%s);"

sqlCommandRanking = "INSERT INTO hot_ranking \
(instid,time,hot_score) \
VALUES(%s,%s,%s);"

if __name__ == '__main__':
    demo = dbconn()
    demo.insertDB(sqlCommandCandle,[('c','b','2020-09-08 12:09:23',1,2,3,4,'1m')])
    # demo.insertDB(sqlCommandCrypto,[('c','b','2020-09-08 12:09:23',1,2),('c','b','2020-09-08 12:09:25',1,4)])
    # demo.insertDB(sqlCommandRanking,[('c','2020-09-08 12:09:26',1),('d','2020-09-08 12:09:26',1)])
    demo.dbClose()
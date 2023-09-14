import os
import sys
DIR_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # print(DIR_BASE)
sys.path.append(DIR_BASE) 
import datetime

# proxies setting
proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

#   start time & time interval
datastr1 = '2023-08-20 00:00:00'
datastr2 = '2023-09-01 00:00:00'
dateArray1 = datetime.datetime.strptime(datastr1, '%Y-%m-%d %H:%M:%S')
# dateArray1 = dateArray1 + datetime.timedelta(hours=1)
dateArray2 = datetime.datetime.strptime(datastr2, '%Y-%m-%d %H:%M:%S')
startTimeSatmp = int(dateArray1.timestamp() * 1000)
endTimeSatmp = int(dateArray2.timestamp() * 1000)
         
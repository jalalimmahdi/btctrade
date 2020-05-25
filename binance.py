import requests
import json
import datetime
import time

import setting

mysymbol=setting.symbol
mytimeframe=setting.TimeFrame

API_EndPoint="https://api.binance.com"

def funcGetDataFromBinance(myQuery):
    link = f"{API_EndPoint}{myQuery}"
    print(f"command is: {link}")
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64)' }
    response = requests.get(link, verify=True,headers=hdr)
    myfile = response.text
    jsonMarketData = json.loads(myfile)        #Converts STR to Json
    #Data = jsonMarketData["data"]
    return jsonMarketData

def binance_findServerTime():
    query_ServerTime="/api/v3/time"
    data=funcGetDataFromBinance(query_ServerTime)
    #the server time is based on milisecond and we devide it to 1000 to have a valid timestamp
    ServerTime_TimeStamp=data.get('serverTime')/1000
    Server_Time = datetime.datetime.fromtimestamp(ServerTime_TimeStamp).ctime()
    return Server_Time

# پرینت لیستی از نمادها و وضعیت هر یک
def binance_exchangeInfo():
    query_info="/api/v3/exchangeInfo"
    data=funcGetDataFromBinance(query_info)
    return data

################################################################
#to get list of bids and asks from binance
# Limit 	            Weight
# 5, 10, 20, 50, 100 	1
# 500                	5
# 1000 	                10
# 5000 	                50
def binance_orderBook(symbol=mysymbol,limit=5):
    query_orderbook=f"/api/v3/depth?symbol={symbol}&limit={limit}"
    data=funcGetDataFromBinance(query_orderbook)
    #Sample: https://api.binance.com/api/v3/depth?symbol=BTCUSDT
    return data

#To show list of bids and asks (just for help me)
def binance_orderBook_printData(symbol=mysymbol,limit=10):
    myOrderBook=binance_orderBook(mysymbol,10)
    bids=myOrderBook.get('bids')
    print("List of Bids: ")
    for x in bids:
        print(x)
    
    asks=myOrderBook.get('asks')
    print('List of Asks: ')
    for x in asks:
        print(x)
################################################################


################################################################
# Name 	Type 	Mandatory 	Description
# symbol 	STRING 	YES 	
# limit 	INT 	NO 	Default 500; max 1000.
# Get recent trades (up to last 500).
def binance_tradesList_recent(symbol=mysymbol,limit=10):
    query_tradelist=f"/api/v3/trades?symbol={symbol}&limit={limit}"
    data=funcGetDataFromBinance(query_tradelist)
    return data

#To show list of bids and asks (just for help me)
def binance_tradesList_recent_PrintData():
    myData=binance_tradesList_recent(symbol=mysymbol,limit=5)
    for x in myData:
        print('*'*50)
        print(f"id: {x.get('id')}")
        print(f"price: {x.get('price')}")
        print(f"qty: {x.get('qty')}")
        print(f"time: {x.get('time')}")
        print(f"isBuyerMaker: {x.get('isBuyerMaker')}")
        print(f"isBestMatch: {x.get('isBestMatch')}")
################################################################



################################################################
# Old trade lookup (MARKET_DATA)
# GET /api/v3/historicalTrades
# Name 	Type 	Mandatory 	Description
# symbol 	STRING 	YES 	
# limit 	INT 	NO 	Default 500; max 1000.
# fromId 	LONG 	NO 	TradeId to fetch from. Default gets most recent trades.
# it needs signature and it do not works simple
def binance_tradesList_old(symbol=mysymbol,limit=10):
    query_tradeListOld=f"/api/v3/historicalTrades?symbol={symbol}&limit={limit}&fromId=327029379"
    data=funcGetDataFromBinance(query_tradeListOld)
    return data

def binance_tradesList_old_PrintData():
    myData=binance_tradesList_old(symbol=mysymbol,limit=5)
    for x in myData:
        print('*'*50)
        print(f"id: {x.get('id')}")
        print(f"price: {x.get('price')}")
        print(f"qty: {x.get('qty')}")
        print(f"time: {x.get('time')}")
        print(f"isBuyerMaker: {x.get('isBuyerMaker')}")
        print(f"isBestMatch: {x.get('isBestMatch')}")
################################################################


################################################################
#
#/api/v3/klines
# Parameters:
# Name 	    Type 	Mandatory 	Description
# symbol 	STRING 	YES 	
# interval 	ENUM 	YES 	
# startTime LONG 	NO 	
# endTime 	LONG 	NO 	
# limit 	INT 	NO 	        Default 500; max 1000.

def binance_klines(symbol=mysymbol,myinterval=mytimeframe,limit=10,startThisTime=0):
    query=f"/api/v3/klines?symbol={symbol}&interval={myinterval}&limit={limit}&startTime={startThisTime}"
    data=funcGetDataFromBinance(query)
    return data

#this function works just for 1min timeframe
#to get all of kandle stcik data of a ONE DAY
def binance_klines_day(beginTime,numberOf12Hours=1):
    myData=[]
    for i in range(0,numberOf12Hours):
        myData_part=binance_klines(mysymbol,'1m',720,startThisTime=beginTime)
        beginTime=beginTime+43200000 #(720*1000*60)
        # print(myData_part[-1][0])
        # print(beginTime)
        myData=myData+myData_part
        time.sleep(2)
    #print(len(myData))
    return myData
        
#To show a list of binance_klines() function 
def binance_klines_PrintData():
    myData=binance_klines(symbol=mysymbol,myinterval=mytimeframe,limit=5)
    # print(myData)
    lastOpenTime=0
    for x in myData:
        print("*"*30)
        print(f"diferent time is: {x[0]-lastOpenTime}")
        print(f"Open Time: {x[0]}")
        lastOpenTime=x[0]
        timeForShow=datetime.datetime.fromtimestamp(lastOpenTime/1000).ctime()
        print(f"Open Time: {timeForShow}")
        
        print(f"Poen Price: {x[1]}")
        print(f"High Price: {x[2]}")
        print(f"Low Price: {x[3]}")
        print(f"Close Price: {x[4]}")
        print(f"Volume: {x[5]}")
        print(f"Close time: {x[6]}")
        print(f"Quote asset volume: {x[7]}")
        print(f"Number of trades: {x[8]}")
        print(f"Taker buy base asset volume: {x[9]}")
        print(f"Taker buy quote asset volume: {x[10]}")
        print(f"Ignore: {x[11]}")

    # 1499040000000,      // Open time
    # "0.01634790",       // Open
    # "0.80000000",       // High
    # "0.01575800",       // Low
    # "0.01577100",       // Close
    # "148976.11427815",  // Volume
    # 1499644799999,      // Close time
    # "2434.19055334",    // Quote asset volume
    # 308,                // Number of trades
    # "1756.87402397",    // Taker buy base asset volume
    # "28.46694368",      // Taker buy quote asset volume
    # "17928899.62484339" // Ignore.
################################################################


################################################################
#this function gives year,month,date and hour and returned the milisecond of the time
def hour_toMilisecond(year=2019,month=1,date=1,hour=0):
    time_this=datetime.datetime(year,month,date,hour,0,0)
    miliseconds=int(round(time_this.timestamp() * 1000))
    print(miliseconds)
    return miliseconds
################################################################


import requests
import json
import datetime
import setting

mysymbol=setting.symbol

API_EndPoint="https://api.binance.com"

def funcGetDataFromBinance(myQuery):
    link = f"{API_EndPoint}{myQuery}"
    print(link)
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

def binance_exchangeInfo():
    query_info="/api/v3/exchangeInfo"
    data=funcGetDataFromBinance(query_info)
    return data

#this prints list of bids and asks in Binance
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

    return 1


import requests
import json

API_EndPoint="https://api.binance.com/"

def funcGetDataFromBinance():
    link = f"{API_EndPoint}"
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64)' }
    response = requests.get(link, verify=True,headers=hdr)
    myfile = response.text
    
    #jsonMarketData = json.loads(myfile)
    #Data = jsonMarketData["data"]
    return myfile
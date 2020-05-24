import binance
import setting

print(binance.binance_findServerTime())

#print(binance.binance_exchangeInfo())

#it shows the bid and ask list:
binance.binance_orderBook_printData()

print(binance.binance_tradesList_recent())
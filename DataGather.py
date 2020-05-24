import binance
import setting

print(binance.binance_findServerTime())

#print(binance.binance_exchangeInfo())

#it shows the bid and ask list:
#binance.binance_orderBook_printData()

#print(binance.binance_tradesList_recent())
#binance.binance_tradesList_recent_PrintData()

#binance.binance_tradesList_old_PrintData()
#This dont work without registerting

#binance.binance_klines_PrintData()

#binance.hour_toMilisecond()

binance.binance_klines_day()
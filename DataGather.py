import mysql.connector

import binance
import setting

#print(binance.binance_findServerTime())

#print(binance.binance_exchangeInfo())

#it shows the bid and ask list:
#binance.binance_orderBook_printData()

#print(binance.binance_tradesList_recent())
#binance.binance_tradesList_recent_PrintData()

#binance.binance_tradesList_old_PrintData()
#This dont work without registerting

#binance.binance_klines_PrintData()

myTime=binance.hour_toMilisecond(year=2019,month=1,date=1,hour=0)

#binance.binance_klines_day()

mydb = mysql.connector.connect(
  host="localhost",
  #port="3308",
  user="root",
  passwd="",
  database="stock"
)

mycursor = mydb.cursor()
sql = "INSERT INTO bit_binance_1m (OpenTime, Open, High, Low, Close,Volume, NumberOfTrades) VALUES (%s, %s,%s, %s, %s, %s, %s)"
# val = [
#   [32323, 23,10,0,0,232,3],
#   [32323, 23,10,0,0,232,3]
# ]

repeatNumber=2
MainRepeatNumber=365
NumberOfRows=0
nowIAm=1590406508245

while myTime<1590406508245:
    DataRaw_oneDay=binance.binance_klines_day(beginTime=myTime,numberOf12Hours=repeatNumber)
    val=[]
    for x in DataRaw_oneDay:
        newLine=[]
        newLine.append(x[0])
        newLine.append(float(x[1]))
        newLine.append(float(x[2]))
        newLine.append(float(x[3]))
        newLine.append(float(x[4]))
        newLine.append(float(x[5]))
        newLine.append(x[8])
        val.append(newLine)
    #print(val)
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
    NumberOfRows=NumberOfRows+mycursor.rowcount
    print(f"Sum of rows: {NumberOfRows}")
    myTime=myTime+(43200000*repeatNumber)
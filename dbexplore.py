#we explore the DB to find if there is any problem and miss date? 
import mysql.connector
import setting

mydb = mysql.connector.connect(
  host=setting.DbHostName,
  user=setting.Dbuser,
  passwd=setting.DbPasswd,
  database=setting.DbName
)

# problemCode=1 / to show that there was no data in the source

mycursor = mydb.cursor()
oneMinMilisecond=60000

mycursor.execute("SELECT * FROM `bit_binance_1m` ORDER BY `bit_binance_1m`.`OpenTime` ASC")
# mycursor.execute("SELECT * FROM `bit_binance_1m` WHERE `OpenTime` > 1590409260000")
myresult = mycursor.fetchall()
thisTime=1546288140000
int_counter=0

for x in myresult:
    thisTime=thisTime+oneMinMilisecond
    # print(f"{thisTime} == {x[1]}")
    if (thisTime!=x[1]):
        if (x[8]==1):
            thisTime=x[1]
        else: 
            print(f"{x[1]} has problem, the ID is : {x[0]}")
            thisTime=x[1]
            int_counter+=1

print(f"Number of probelms: {int_counter}")
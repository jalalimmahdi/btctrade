#we explore the DB to find if the patern Two

# UPDATE `bit_binance_1m` SET `problemCode` = '3' WHERE `bit_binance_1m`.`id` = 1;
import binance
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

Time_Start=myTime=binance.hour_toMilisecond(year=2018,month=1,date=1,hour=0)                # Based on MiliSecond

myTime=Time_Start
oneMinMilisecond=60000

mycursor.execute("SELECT * FROM `test1` ORDER BY `test1`.`OpenTime` ASC")
#mycursor.execute("SELECT * FROM test1 WHERE `OpenTime`={my_Time}")
myresult = mycursor.fetchall()
last_type1=""

for x in myresult:
    my_type1=x[9]
    mytype=last_type1+my_type1
    sql=f"UPDATE `test1` SET `type2` = '{mytype}' WHERE `test1`.`id` = {x[0]}"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()

    last_type1=my_type1

mycursor.close()
mydb.close()

# report:
#SELECT `type2`, COUNT(*) FROM `test1` GROUP BY `type2` ORDER BY COUNT(*) ASC 
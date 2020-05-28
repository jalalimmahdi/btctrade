#we explore the DB to find if the patern ONE

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
last_average=0.0
last_volume=0.0
last_num=0.0

alltypes={
    '111':'a',
    '110':'b',
    '101':'c',
    '100':'d',
    '011':'e',
    '010':'f',
    '001':'g',
    '000':'h'
}

for x in myresult:
    new_average=(x[2]+x[3]+x[4]+x[5])/4
    if new_average>=last_average:
        n_1=1
    else: n_1=0
    
    new_volume=x[6]
    if new_volume>=last_volume:
        n_2=1
    else:
        n_2=0
    
    new_num=x[7]
    if new_num>=last_num:
        n_3=1 
    else:
        n_3=0
    final_n=str(n_1)+ str(n_2)+str(n_3)
    
    mytype=alltypes.get(final_n)
    sql=f"UPDATE `test1` SET `type1` = '{mytype}' WHERE `test1`.`id` = {x[0]}"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    
    print(f"{x[0]} = {mytype}")
    last_average=new_average
    last_volume=new_volume
    last_num=new_num

mycursor.close()
mydb.close()

#report: 
#SELECT `type1`, COUNT(*) FROM `test1` GROUP BY `type1` ORDER BY COUNT(*) ASC 
# g 	72499
# f 	73694
# c 	75292
# b 	76582
# a 	230821
# e 	235981
# h 	241130
# d 	248531
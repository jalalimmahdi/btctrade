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

#در اینجا مواردی که تکراری هستند را پیدا میکنیم
mycursor.execute("SELECT * FROM bit_binance_1m GROUP BY `OpenTime` HAVING COUNT(`OpenTime`) > 1")
myresult = mycursor.fetchall()

for x in myresult:
    #برای هر کدام از موارد تکراری لیست تمامی آیتم ها را پیدا میکنیم
    mycursor.execute(f"SELECT * FROM `bit_binance_1m` WHERE `OpenTime` = {x[1]} ORDER BY `id` ASC")
    myresult2 = mycursor.fetchall()
    DoDlete=True
    # در حلقه ی زیر اولین مورد تکراری را حذف میکنیم
    for y in myresult2:
        print(y)
        if (DoDlete==True):
            mycursor.execute(f"DELETE FROM `bit_binance_1m` WHERE `bit_binance_1m`.`id` = {y[0]}")
            DoDlete=False
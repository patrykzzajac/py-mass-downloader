import mysql.connector
import requests
import os

#connect to db
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbaname"
)
mycursor = mydb.cursor()

#query image url
sql = ""

mycursor.execute(sql)

myresult = mycursor.fetchall()
cnt = 1
for x in myresult:
    print(os.path.basename(x[0]), " ", cnt)
    url = x[0]
    r = requests.get(url, allow_redirects=True)

    open(os.path.basename(x[0]), 'wb').write(r.content)
    cnt = cnt + 1


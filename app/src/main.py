import mysql.connector
import os

connection = mysql.connector.connect(
    user=os.environ['USER'], password=os.environ['PASS'], 
    host=os.environ['HOST'], port=os.environ['PORT'], 
    database=os.environ['DB'])
print("DB connected")
cursor = connection.cursor()
cursor.execute('Select * FROM test')
test = cursor.fetchall()
connection.close()

print(test)
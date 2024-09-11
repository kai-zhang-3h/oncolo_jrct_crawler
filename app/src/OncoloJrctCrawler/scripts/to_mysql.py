import mysql.connector
import os
import csv

fieldnames = []
rows = []

with open('public/data.csv', 'r', encoding='utf_8_sig') as f:
     reader = csv.DictReader(f)
     fieldnames = reader.fieldnames

     for row in reader:
          rows.append(tuple(row.values()))

len_rows = len(rows)
print(f"There are {len_rows} lines inserted")

t_name = "t_oncolo_jrct"

connection = mysql.connector.connect(
    user=os.environ['USER'], password=os.environ['PASS'], 
    host=os.environ['HOST'], port=os.environ['PORT'], 
    database=os.environ['DB'])
print("DB connected")
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS ' + t_name)
fields_string = ", ".join(list(map(lambda e: e.split(":")[1] + " TEXT COMMENT \'" + e.split(":")[0] + "\'", fieldnames)))
create_query = "CREATE Table " + t_name + "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " + fields_string + ")DEFAULT CHARACTER SET=utf8"
cursor.execute(create_query)

fields_title_string = ", ".join(list(map(lambda e: e.split(":")[1], fieldnames)))

query = 'INSERT INTO ' + t_name + '(' + fields_title_string + ') VALUES '+ "(" + '%s, ' * (len(fieldnames) - 1) + '%s' + ")"                                                         

cursor.executemany(query, rows)

connection.commit()
connection.close()
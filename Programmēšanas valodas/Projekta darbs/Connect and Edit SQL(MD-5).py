import mysql.connector
  
  
mydb = mysql.connector.connect(host='127.0.0.1',
                        database='performanceStatisticsDT',
                        user='MariaDBUser',
                        password='Passw0rd!')
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

#USE performanceStatisticsDT;


Data = [('dataTransform', 'Sequential', 2),
('dataTransform', 'Sequential', 1),
('dataTransform', 'Sequential', 5),
('dataTransform', 'Sequential', 3),
('dataTransform', 'Sequential', 4),
('dataTransform', 'Sequential', 3),
('dataTransform', 'Sequential', 5),
('dataTransform', 'Sequential', 2),
('dataTransform', 'Sequential', 4),
('dataTransform', 'Sequential', 1),
('dataTransform', 'Parallel', 1),
('dataTransform', 'Parallel', 3),
('dataTransform', 'Parallel', 2),
('dataTransform', 'Parallel', 2),
('dataTransform', 'Parallel', 3),
('dataTransform', 'Parallel', 1),
('dataTransform', 'Parallel', 2),
('dataTransform', 'Parallel', 1),
('dataTransform', 'Parallel', 3),
('dataTransform', 'Parallel', 1)]


sql = "INSERT INTO runtimeLog(runtimeElement, runtimeType, runtimeResult) VALUES (%s, %s, %s)"
mycursor.executemany(sql, Data)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

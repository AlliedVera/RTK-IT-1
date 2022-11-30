import mysql.connector
import matplotlib.pyplot as plt
  
mydb = mysql.connector.connect(host='127.0.0.1',
                        database='performanceStatisticsDT',
                        user='MariaDBUser',
                        password='Passw0rd!')

mycursor = mydb.cursor()

Sequential = "SELECT * FROM runtimeLog WHERE runtimeType = 'Sequential'"
Parallel = "SELECT * FROM runtimeLog WHERE runtimeType = 'Parallel'"

mycursor.execute(Sequential)
resultSeq = mycursor.fetchall()
for x in resultSeq:
    print(x)

mycursor.execute(Parallel)
resultPar = mycursor.fetchall()
for x in resultPar:
    print(x)
    
    
sequentialArray = [item[3] for item in resultSeq]
parallelArray =[item[3] for item in resultPar]
print(sequentialArray)
print(parallelArray)
arrays = [sequentialArray, parallelArray]

x = sequentialArray
y = parallelArray
xy = (x, y)


fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

plt.boxplot(xy, notch=None, vert=None, patch_artist=None, widths=None)

plt.grid(axis = 'y', color = 'green', linestyle = '--', linewidth = 0.5)

plt.ylim([0, 5.2])
xpoints = [1, 2, 6, 8]

ticks = [0,1,2,3,4,5]
labels = ["0s", "1s", "2s", "3s", "4s", "5s"]

plt.yticks(ticks, labels)

xticks = [1,2]
xlabels = ["Sequential processing", "Parallel processing"]

plt.xticks(xticks, xlabels, fontsize=15)

plt.title("PowerApps Sequential vs Parallel data processing", fontsize=20)
plt.xlabel("Data processing types", fontsize=15)
plt.ylabel("Time consuption in seconds(s)", fontsize=15)

plt.show()


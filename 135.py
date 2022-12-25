import matplotlib.pyplot as plt
import pandas as pd
import csv 

df = []

with open('main.csv','r') as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    if row != []:
      df.append(row)

headers = df[0] 
data = df[1]
Name = []
Mass = []
Radius = []
Distance = []
Gravity = []

for i in data:
  Name.append(i[1])
  Distance.append(float(i[2]))
  Mass.append(float(i[3]))
  Radius.append(float(i[4]))
  Gravity.append(float(i[5].split(' ')[0]))

plt.bar(Name,Mass)
plt.title('Name VS Mass')
plt.xlabel('Name of Stars')
plt.ylabel('Mass of Stars')
plt.xticks(rotation=45)
plt.show()

plt.bar(Name,Radius)
plt.title('Name VS Radius')
plt.xlabel('Name of Stars')
plt.ylabel('Radius of Stars')
plt.xticks(rotation=45)
plt.show()

plt.bar(Name,Distance)                 
plt.title('Name VS Distance')                     
plt.xlabel('Name of Stars')
plt.ylabel('Distance of Stars')
plt.xticks(rotation=45)
plt.show()

plt.bar(Name,Gravity)
plt.title('Name VS Gravity')
plt.xlabel('Name of Stars')
plt.ylabel('Gravity of Stars')
plt.xticks(rotation=45)
plt.show()
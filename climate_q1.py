import matplotlib.pyplot as plt

# Import Sqlite requirements
import sqlite3
connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

# Fetch the stuff
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")

extract = cursor.fetchall()

years = []
co2 = []
temp = []

# Iterate through extracted data and add to lists
for row in extract:
    year, co2_val, temp_val = row
    years.append(year)
    co2.append(co2_val)
    temp.append(temp_val)

print("Years:", years)
print("Years:", co2)
print("Years:", temp)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 

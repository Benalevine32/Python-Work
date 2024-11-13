# Ben Levine 11/13/2024
# This program will take a series of temperatures and return the number of days that the temperatures is above the average temperature

numberOfDays = int(input("Enter the number of days: "))
totalTemp=0
temps = []

for i in range(1, numberOfDays+1):
    temp = float(input("Enter Temperature: "))
    temps.append(temp)
    totalTemp = totalTemp + temp

averageTemp = totalTemp / numberOfDays
print("Average Temperature: " + str(averageTemp))

numDaysAboveAvg = 0
for temp in temps:
    if temp > averageTemp:
        numDaysAboveAvg = numDaysAboveAvg + 1

print("Number of days above average: " + str(numDaysAboveAvg))

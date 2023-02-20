import csv

with open('nyc_weather.csv', 'r') as f:
    csvReader = csv.reader(f)
    days = []
    for row in csvReader:
        days.append((row))
    

print(days['Jan 4'])
import csv
from datetime import datetime

from matplotlib import pyplot as plt

file = "sitka_weather_2014.csv"

with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, rainfalls = [], []

    for row in reader:
        try:
            date = datetime.strptime(row[0],'%Y-%m-%d')
            rainfall = float(row[19])
        except ValueError:
            print(date, 'bzzzt no data')
        else:
            dates.append(date)
            rainfalls.append(rainfall)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, rainfalls, c='blue', alpha=0.6)
plt.fill_between(dates, rainfalls, facecolor = 'red', alpha=0.2)

# modify the plot
title = "Sitka 2014 Rainfall"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rain in in.", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('e05_rainfall2014.png', bbox_inches='tight')
plt.show()

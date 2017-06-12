import csv
# this allows to create a date format
from datetime import datetime

from matplotlib import pyplot as plt

def getWeatherData(filename, dates, highs, lows):
    with open(filename) as f:
        # then pass file as arg to create reader object associated with file
        reader = csv.reader(f)
        # next() returns the next line in file, in this case only once for header
        header_row = next(reader)
        # print(header_row)

        # get high temperatures from file.
        # create an empty list for dates, highs, lows
        # dates, highs, lows = [], [], []
        
        # then loop through remaining rows in the file; continues where left off
        # On each pass through loop, append data from index 1, 2nd col, to highs
        for row in reader:
            # each time we examine row, try to extract date and high and low temp
            try:
                # convert data contianing date info (row[0]) to a datetime obj
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            # if any data is missing, Python raises this error and we print this 
            except ValueError:
                print(current_date, 'missing data')
            # if no error then this will run and data appened to appropiate lists
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        # print(highs)

        # To make easier to understand file header data, we print each
        # header and its position in the list
        # enumerate is used to get index of each item and value
        # for index, column_header in enumerate(header_row):
        #     print(index, column_header)

dates, highs, lows = [], [], []

getWeatherData('sitka_weather_2014.csv', dates, highs, lows)

# plot sitzka data
fig = plt.figure(dpi=128, figsize=(10,6))
# pass the list of highs and dates to plot()
# alpha controls transparency
plt.plot(dates, highs, c='red', alpha =0.6)
# pass the list of lows and dates to plot
plt.plot(dates, lows, c ='blue', alpha=0.6)
# shade in between the two color sets
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# get death valley data
dates, highs, lows = [], [], []
getWeatherData('death_valley_2014.csv', dates, highs, lows)
# add death valley to current plot
# pass the list of highs and dates to plot()
# alpha controls transparency
plt.plot(dates, highs, c='red', alpha =0.3)
# pass the list of lows and dates to plot
plt.plot(dates, lows, c ='blue', alpha=0.3)
# shade in between the two color sets
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Formal plot.
title = "Daily high and low temperatures - 2014"
title += "\nSitka darker shade and Death Valley lighter shade"
plt.title(title, fontsize=20)
# we would label the dates here.
plt.xlabel('', fontsize=16)
# draws the date labels diagonally to prevent overlapping
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
plt.savefig('e05_high_low3', bbox_inches='tight')

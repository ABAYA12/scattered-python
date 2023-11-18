import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = 'ghana_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # set an empty list for high and lower temp and one for the dates
    highs, lows, dates = [], [], []

    for row in reader:
        # handle errors
        try:
            # Get the dates converted to the date time frmae
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # Get the highest temperature from the file.
            high = int(row[1])
            # Get the lowest temperature form the file
            low = int(row[3])

        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='blue', label='High', alpha=0.5)
plt.plot(dates, lows, c='red', label='Low', alpha=0.5)

# Fill the area between the high and low temperatures.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# add annotation to the plot
for date, high, low in zip(dates, highs, lows):
    plt.annotate(f"{high}°F", (date, high), textcoords='offset points', xytext=(
        0, 10), ha='center', fontsize=8, color='blue')
    plt.annotate(f"{low}°F", (date, low), textcoords='offset points',
                 xytext=(0, -15), ha='center', fontsize=8, color='red')

# Format plot.
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel('\nDates', fontsize=14)

# use the fig.autofmt_xdate() method to prevent overlapping of the dates
fig.autofmt_xdate()
plt.ylabel('Temparatures in (F)', fontsize=14)

plt.legend()

plt.show()

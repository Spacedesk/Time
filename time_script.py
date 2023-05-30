import datetime
import pytz

# Define the time zones
london_timezone = pytz.timezone('Europe/London')
new_york_timezone = pytz.timezone('America/New_York')

# Get the current time in London
london_time = datetime.datetime.now(london_timezone)
london_time_str = london_time.strftime('%Y-%m-%d %H:%M:%S')

# Get the current time in New York
new_york_time = datetime.datetime.now(new_york_timezone)
new_york_time_str = new_york_time.strftime('%Y-%m-%d %H:%M:%S')

# Print the results
print('Current time in London:', london_time_str)
print('Current time  in New York:', new_york_time_str)

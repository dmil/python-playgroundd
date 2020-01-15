# by Dhrumil and Sultan
from datetime import datetime as dt

# Set a variable birthday = "1-May-12".
birthday = "1-May-12"

# Parse the date using datetime.strptime.
python_date = dt.strptime(birthday, "%d-%B-%y")

# Use strftime to output a date that looks like "5/1/2012".
date_str = python_date.strftime("%-m/%-d/%Y") # 01/11/17

print(date_str)

# HINT: https://strftime.org

# by Dhrumil and Sultan
import csv
import json


# 1. Read vegetables.csv 
# (see previous section) into a 
# variable called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict


# 2. Print the variable vegetables.
print(rows)


# 3. Write vegetables as a JSON file 
# called vegetables.json. 
# It should look like this:
with open('vegetables.json', 'w') as f:
    json.dump(rows, f, indent=4)

# [
#   { "name": "eggplant", "color": "purple" },
#   { "name": "tomato", "color": "red" },
#   { "name": "corn", "color": "yellow" },
#   { "name": "okra", "color": "green" },
#   { "name": "arugula", "color": "green" },
#   { "name": "broccoli", "color": "green" }
# ]


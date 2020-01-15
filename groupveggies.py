# Dhrumil and Sultan

import csv
import json

from pprint import pprint

# [{'color': 'purple', 'name': 'eggplant'},
#  {'color': 'red', 'name': 'tomato'},
#  {'color': 'yellow', 'name': 'corn'},
#  {'color': 'green', 'name': 'okra'},
#  {'color': 'green', 'name': 'arugula'},
#  {'color': 'green', 'name': 'broccoli'}]

# 1. Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] # Convert OrderedDict to regular dict

# 2. Group vegtables by color as a variable vegtables_by_color.
vegtables_by_color = {}
for veg in vegetables:
	color = veg['color']
	if color in vegtables_by_color:
		vegtables_by_color[color].append(veg)
	else:
		vegtables_by_color[color] = [veg]

# 3. Output vegtables_by_color into a json called vegtables_by_color.json.
with open('groupedveggies.json', 'w') as f:
	json.dump(vegtables_by_color, f, indent=2)

# by Dhrumil and Sultan

import csv
import json
from pprint import pprint

# 1. Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] # Convert OrderedDict to regular dict


with open('greenveggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])

	# 2. Loop through vegetables and filter down to only green vegtables
	green_veggies = []
	for veg in vegetables:
		if veg['color'] == 'green':
			# 3. Print green veggies to the terminal
			green_veggies.append(veg)
			writer.writerow([veg['name'], veg['color']])


# 4. Write the green veggies to a json file 
#    called greenveggies.json
with open('green_veggies.json', 'w') as f:
    json.dump(green_veggies, f, indent=2)


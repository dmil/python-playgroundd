# by Dhrumil and Sultan
import csv


vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	# write header
	writer.writerow(['name', 'color'])

	# Loops through each vegetable
	for veggie in vegetables:
		veggie_name = veggie['name']
		veggie_color = veggie['color']
		# Write row of data
		writer.writerow([veggie_name, veggie_color])

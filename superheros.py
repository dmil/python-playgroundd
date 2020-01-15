# by Dhrumil and Sultan

# Reads superheroes.json (in this folder)
import json
from pprint import pprint
import csv

# Read superheroes.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# Write a header to the CSV file
with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	headers = ["name", "age", "secretIdentity", "powers", 
			   "squadName", "homeTown", "formed", 
			   "secretBase", "active"]
	writer.writerow(headers)

	# Loop over the members 
	members = superheroes['members']
	for member in members:
		
		# Define variables
		name = member['name']
		# age = ?????
		# secret_identity = ????
		this_members_powers = member['powers']
		
		# write row
		row = [name, age, ]
		writer.writerow(row)
		
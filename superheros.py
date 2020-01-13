# Reads superheroes.json (in this folder)
import json
from pprint import pprint

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)
    
# print(superheroes)


# Creates an empty array called powers
powers = []

# Loop thorough the members of the squad, and 
# append the powers of each to the powers array.
members = superheroes['members']
for member in members:
	this_members_powers = member['powers']
	powers.append(this_members_powers)


# Prints those powers to the terminal
pprint(powers)
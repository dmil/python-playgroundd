import csv
from pprint import pprint

with open('testwrite.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict

pprint(rows)
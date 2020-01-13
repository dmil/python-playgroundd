import json

with open('friends.json', 'r') as f:
    data = json.load(f)
    
print(data)
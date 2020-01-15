from pprint import pprint


# filter whitelist names
rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter to age < 37
# millenials = []
# for row in rows:
#     if row['age'] < 37:
#         millenials.append(row)

# pprint(millenials)

import pandas as pd 

df = pd.DataFrame(rows)
millenials = df.query('age < 37')

millenials.to_csv('millenials.csv', index=False)

print(millenials)
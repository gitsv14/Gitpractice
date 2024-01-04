import pandas as pd
df = pd.read_csv('p1.csv', delimiter=',')
list_of_rows = [list(row) for row in df.values]
a = list_of_rows[0]
b = list_of_rows[1]
c = list_of_rows[2]
d = list_of_rows[3]
e = list_of_rows[4]

data = [a, b, c, d, e]

for item in data:
    name, place, value = item
    print(f"My name is {name} place is {place} and value is {value}")

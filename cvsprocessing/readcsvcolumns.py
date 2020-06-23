import pandas as pd

csv_read = pd.read_csv('input.csv')
print(csv_read.loc[:,['salary','name']])

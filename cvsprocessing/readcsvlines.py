import pandas as pd

csv_read = pd.read_csv('input.csv')
print(csv_read.loc[[1,3,5],['salary','name']])

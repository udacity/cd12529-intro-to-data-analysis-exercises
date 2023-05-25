import pandas as pd

df = pd.read_csv("census_income_data.csv")

for column in df.columns:
    print(column)

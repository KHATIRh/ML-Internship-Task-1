import pandas as pd

data=pd.read_csv("transaction_anomalies_dataset.csv")

null_values=data.isnull().sum()
print("Null values in each column:\n",null_values)

print("\nColumn information:")
print(data.info())

print("\nDescriptive statistics of the data:")
print(data.describe())

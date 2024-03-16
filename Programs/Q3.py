import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("transaction_anomalies_dataset.csv")

sns.set_style("whitegrid") 

plt.figure(figsize=(10, 6))
sns.boxplot(x='Account_Type', y='Transaction_Amount', data=df)
sns.stripplot(x='Account_Type', y='Transaction_Amount', data=df, jitter=True, marker='o', color='#636efa')

plt.style.use("Solarize_Light2")
plt.title('Transaction Amount by Account Type', loc='left')
plt.xlabel('Account_Type')
plt.ylabel('Transaction_Amount')
plt.gca().set_facecolor('#e5ecf6')
plt.show()

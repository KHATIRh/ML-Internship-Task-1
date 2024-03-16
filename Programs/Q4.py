import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('transaction_anomalies_dataset.csv')

average_transaction_by_age = df.groupby('Age')['Transaction_Amount'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Transaction_Amount', hue='Account_Type', palette=['red', 'blue'])
sns.lineplot(data=average_transaction_by_age, x='Age', y='Transaction_Amount', color='purple')
plt.title('Average Transaction Amount vs. Age', loc='left')
plt.xlabel('Age')
plt.ylabel('Average Transaction Amount')
plt.gca().set_facecolor('#e5ecf6')



plt.grid(True, color='white', linewidth=0.3)
plt.show()

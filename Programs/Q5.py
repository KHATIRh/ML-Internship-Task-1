import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("transaction_anomalies_dataset.csv")

days_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

transactions_by_day = data['Day_of_Week'].value_counts().reindex(days_order)

plt.figure(figsize=(10, 6))
transactions_by_day.plot(kind='bar', color='#8f99f9', width=0.7, zorder=2)

plt.title('Count of Transactions by Day of the Week', loc='left')
plt.xlabel('Day_of_the_Week')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y', color='white', linewidth=0.3, zorder=1)
plt.gca().set_facecolor('#e5ecf6')
plt.show()

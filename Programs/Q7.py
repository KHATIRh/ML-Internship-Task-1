import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from matplotlib.lines import Line2D

data = pd.read_csv("transaction_anomalies_dataset.csv")

features = ['Transaction_Amount', 'Average_Transaction_Amount']

model = IsolationForest(contamination=0.1)
model.fit(data[features])

data['Is_Anomaly'] = model.predict(data[features])

plt.figure(figsize=(10, 6))
scatter = plt.scatter(data['Transaction_Amount'], data['Average_Transaction_Amount'], c=data['Is_Anomaly'], cmap='coolwarm', zorder=2)

legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='True'),
                   Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='False')]
plt.legend(handles=legend_elements, title='Is_Anomaly', loc='upper right')

plt.xlabel('Transaction_Amount')
plt.ylabel('Average_Transaction_Amount')
plt.gca().set_facecolor('#e5ecf6')
plt.grid(True, color='white', linewidth=0.3, zorder=1)
plt.show()

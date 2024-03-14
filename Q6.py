import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("transaction_anomalies_dataset.csv")

numeric_data = data.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numeric_data.corr()

plt.figure(figsize=(10, 6))

sns.heatmap(correlation_matrix, cmap='viridis', fmt=".2f", annot_kws={"size": 10})

plt.title('Correlation Headmap', loc='left')
plt.xticks(rotation=320)
plt.tight_layout()
plt.show()

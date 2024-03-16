import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("transaction_anomalies_dataset.csv")

features = ['Transaction_Amount', 'Average_Transaction_Amount']

model = IsolationForest(contamination=0.1)
model.fit(data[features])

data['Is_Anomaly'] = model.predict(data[features])

num_anomalies = (data['Is_Anomaly'] == -1).sum()

total_data_points = data.shape[0]

anomaly_ratio = num_anomalies / total_data_points

print("Number of anomalies:", num_anomalies)
print("Total data points:", total_data_points)
print("Ratio of anomalies:", anomaly_ratio)

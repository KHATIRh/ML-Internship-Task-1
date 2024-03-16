import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

data = pd.read_csv("transaction_anomalies_dataset.csv")


features = ['Transaction_Amount', 'Transaction_Volume', 'Average_Transaction_Amount',
            'Frequency_of_Transactions', 'Time_Since_Last_Transaction', 'Age', 'Income']

model = IsolationForest(contamination=0.1)
model.fit(data[features])

predictions = model.predict(data[features])
#1 for Normal, and 0 for anomaly

binary_predictions = [1 if pred == 1 else 0 for pred in predictions]

data['Is_Anomaly'] = binary_predictions

print(data)

#Question 10

print("\nClassification Report:")

report = classification_report(data['Is_Anomaly'], binary_predictions)

print(report)

#Question 11
print('\n')
input_values={
    'Transaction_Amount':10000,
    'Average_Transaction_Amount':900,
    'Frequency+of_Transactions':6,
    'Age':30,
    'Income':50000,
    'Time_Since_Last_transaction':10,
    'Transaction_Volume':20,
}



input_data=pd.DataFrame([input_values])

prediction=model.predict(input_data.values.reshape(1,-1))

if prediction[0]==-1:
    print('Anomaly detected: This transaction is flagged as anomaly.')
else:
    print('No anomaly detected: This transaction is not flagged as an anomaly.')
import numpy as np

# Define the input values
input_values = {
    'Transaction_Amount': 10000,
    'Average_Transaction_Amount': 900,
    'Frequency_of_Transactions': 6
}

# Convert input values to a DataFrame
input_data = pd.DataFrame([input_values])

# Get prediction for the input data
prediction = model.predict(input_data)

# Check if the prediction indicates an anomaly
if prediction[0] == -1:
    print("Anomaly detected: This transaction is flagged as an anomaly.")
else:
    print("No anomaly detected: This transaction is not flagged as an anomaly.")

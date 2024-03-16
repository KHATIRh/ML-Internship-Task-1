import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("transaction_anomalies_dataset.csv")


plt.figure(figsize=(10,6))
plt.style.use("Solarize_Light2")
plt.hist(data['Transaction_Amount'], color='#636efa')
plt.title('Distribution of Transaction Amount', loc='left')
plt.xlabel('Transaction_Amount')
plt.ylabel('Count')
plt.grid(True, color='lightblue', linewidth=0.3)
plt.gca().set_facecolor('#e5ecf6')
plt.show()

import random
from datetime import datetime, timedelta
import pandas as pd

# Set the number of entries in the dataset
num_entries = 1000  # Adjust as needed for your dataset size

# Generate random kWh consumption values (from 100 to 500)
kwh_values = [random.randint(100, 500) for _ in range(num_entries)]

# Generate random due dates based on the current date
current_date = datetime.now()
due_dates = [(current_date + timedelta(days=random.randint(1, 30))).date() for _ in range(num_entries)]

# Create a DataFrame with random kWh values and due dates
data = pd.DataFrame({
    "kWh_Consumed": kwh_values,
    "Due_Date": due_dates
})

# Show the first few rows of the dataset
print(data.head())

# Save the dataset to a CSV file if needed
data.to_csv("random_kwh_consumption_due_dates.csv", index=False)

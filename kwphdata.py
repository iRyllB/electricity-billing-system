#generate csv file with random values
import random
from datetime import datetime, timedelta
import pandas as pd

num_entries = 1000 

kwh_values = [random.randint(100, 500) for _ in range(num_entries)]

current_date = datetime.now()
due_dates = [(current_date + timedelta(days=random.randint(1, 30))).date() for _ in range(num_entries)]

data = pd.DataFrame({
    "kWh_Consumed": kwh_values,
    "Due_Date": due_dates
})

print(data.head())

data.to_csv("random_kwh_consumption_due_dates.csv", index=False)

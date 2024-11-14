import datetime

rates = {
    "Monday": 11.43,   
    "Tuesday": 10.50,   
    "Wednesday": 12.00, 
    "Thursday": 11.80,  
    "Friday": 13.25,    
    "Saturday": 14.00, 
    "Sunday": 11.00    
}

today = datetime.datetime.now().strftime('%A')  #full weekday name
rate_today = rates.get(today, 11.43)  # Default to 11.43 pesos if day is not found

customer_name = input("Enter customer name: ")
units_consumed = float(input("Enter units consumed (kWh): "))

bill_amount = units_consumed * rate_today

print(f"\nCustomer: {customer_name}")
print(f"Units Consumed: {units_consumed} kWh")
print(f"Rate: {rate_today} pesos/kWh")
print(f"Bill Amount: {bill_amount:.2f} pesos")

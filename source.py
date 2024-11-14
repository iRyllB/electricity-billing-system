# billing_system.py

class ElectricityBillingSystem:
    def __init__(self, rate_per_kWh):
        self.rate_per_kWh = rate_per_kWh

    def calculate_bill(self, customer_name, units_consumed):
        bill_amount = units_consumed * self.rate_per_kWh
        return f"Customer: {customer_name}\nUnits Consumed: {units_consumed} kWh\nBill Amount: ${bill_amount:.2f}"

# Example Usage
if __name__ == "__main__":
    rate = 0.12  # example rate per kWh
    billing_system = ElectricityBillingSystem(rate)
    customer_name = input("Enter customer name: ")
    units = float(input("Enter units consumed (kWh): "))
    print(billing_system.calculate_bill(customer_name, units))

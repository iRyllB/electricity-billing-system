import tkinter as tk
from datetime import datetime

print("Welcome to USTP OmniCharge CDO")

# for data
class Customer:
    def __init__(self, account_no, name, password, phone_no, address):
        self.account_no = account_no
        self.name = name
        self.password = password
        self.phone_no = phone_no
        self.address = address
        self.bills = []  #

class Bill:
    def __init__(self, units, bill_amount, payment_date):
        self.units = units
        self.bill_amount = bill_amount
        self.payment_date = payment_date

class ElectricityBillingSystem:
    def __init__(self):
        self.customers = {}  
        self.account_no_counter = 1 

    def create_account(self, name, password, phone_no, address):
        account_no = self.account_no_counter
        self.account_no_counter += 1
        new_customer = Customer(account_no, name, password, phone_no, address)
        self.customers[account_no] = new_customer
        return account_no

    def log_in(self, name, password):
        for customer in self.customers.values():
            if customer.name == name and customer.password == password:
                return customer
        return None

#prelogin
def create_account(system):
    name = input("Enter the consumer name: ")
    password = input("Enter your Passkey: ")
    phone_no = input("Enter your phone number: ")
    address = input("Enter your address: ")

    account_no = system.create_account(name, password, phone_no, address)
    print(f"Account Created Successfully! Your Account Number: {account_no}")

def log_in(system):
    name = input("Enter your name: ")
    password = input("Enter your Passkey: ")

    customer = system.log_in(name, password)
    if customer:
        print("\nWELCOME TO USTP OMNICHARGE CDO\n")
        user_dashboard(system, customer)
    else:
        print("Invalid Credentials, please try again.")

#dashboard
def user_dashboard(system, customer):
    while True:
        print("""
        TO SEE your details, press               : 1
        TO PAY the bill, press                   : 2
        TO UPDATE your details, press            : 3
        TO EXIT, press                           : 4
        """)
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                show_consumer_details(customer)
            elif choice == 2:
                pay_bill(customer)
            elif choice == 3:
                update_details(customer)
            elif choice == 4:
                print("Thank you for visiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def show_consumer_details(customer):
    print("\n--- Consumer Details ---")
    print(f"Account Number: {customer.account_no}")
    print(f"Name: {customer.name}")
    print(f"Phone Number: {customer.phone_no}")
    print(f"Address: {customer.address}")

    if customer.bills:
        print("\n--- Payment History ---")
        for bill in customer.bills:
            print(f"Units Consumed: {bill.units}, Bill Amount: {bill.bill_amount:.2f}, Date: {bill.payment_date}")
    else:
        print("No payment history found.")

def pay_bill(customer):
    bill_rate = 11.42  # Cost per unit in kwph
    try:
        units = int(input("Enter the units consumed (kwph): "))
        total_bill = units * bill_rate
        payment_date = datetime.now().date()

        print(f"\n--- Bill Calculation ---")
        print(f"Units Consumed: {units} kwph")
        print(f"Bill Rate: {bill_rate} per unit")
        print(f"Total Bill: {total_bill:.2f}")
        print(f"Payment Date: {payment_date}")

        payment = input("Do you wish to proceed with the payment? (y/n): ").lower()
        if payment == 'y':
            new_bill = Bill(units, total_bill, payment_date)
            customer.bills.append(new_bill)
            print("Payment Successful! Thank you for using our service.\n")
        else:
            print("Payment canceled.")
    except ValueError:
        print("Invalid input. Please enter numeric values for units.")

def update_details(customer):
    new_phone = input("Enter your new phone number: ")
    new_address = input("Enter your new address: ")

    customer.phone_no = new_phone
    customer.address = new_address
    print("Details Updated Successfully!")

#main
system = ElectricityBillingSystem()

while True:
    print("\n1. CREATE YOUR ACCOUNT")
    print("2. LOG IN")
    print("3. EXIT")
    try:
        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            create_account(system)
        elif choice == 2:
            log_in(system)
        elif choice == 3:
            print("Thank you for visiting!")
            break
        else:
            print("Invalid Choice, Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

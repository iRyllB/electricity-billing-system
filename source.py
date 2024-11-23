from datetime import datetime

#banner, pang design
def print_banner(title):
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

def print_separator():
    print("-" * 50)

def print_message(message):
    print("\n" + f"{message}".center(50))
    print()

print_banner("Welcome to USTP OmniCharge CDO")

# Data (no need for MySQL, following the lessons)
class Customer:
    def __init__(self, account_no, name, password, phone_no, address):
        self.account_no = account_no
        self.name = name
        self.password = password
        self.phone_no = phone_no
        self.address = address
        self.bills = []

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

##############################################################################################################

##############################################################################################################
# Main Menu
def create_account(system):
    print_banner("Create Your Account")
    
    print("Type 'back' at any time to return to the main menu.")
    
    name = input("Enter the consumer name: ").strip()
    if name.lower() == 'back':
        return
    if not name: 
        print_message("Error: Name cannot be blank or just spaces. Please try again.")
        return
    
    password = input("Enter your Passkey: ").strip()
    if password.lower() == 'back':
        return
    if not password:
        print_message("Error: Password cannot be blank or just spaces. Please try again.")
        return
    
    phone_no = input("Enter your phone number: ").strip()
    if phone_no.lower() == 'back':
        return
    if not phone_no:
        print_message("Error: Phone number cannot be blank or just spaces. Please try again.")
        return
    
    address = input("Enter your address: ").strip()
    if address.lower() == 'back':
        return
    if not address: 
        print_message("Error: Address cannot be blank or just spaces. Please try again.")
        return

    account_no = system.create_account(name, password, phone_no, address)
    print_message(f"Account Created Successfully!\nYour Account Number: {account_no}")

def log_in(system):
    print_banner("Log In to Your Account")
    
    print("Type 'back' at any time to return to the main menu.")
    
    name = input("Enter your name: ").strip()
    if name.lower() == 'back':
        return
    
    password = input("Enter your Passkey: ").strip()
    if password.lower() == 'back':
        return

    customer = system.log_in(name, password)
    if customer:
        print_message(f"Welcome, {customer.name}!")
        user_dashboard(system, customer)
    else:
        print_message("Invalid Credentials, please try again.")

# Dashboard
def user_dashboard(system, customer):
    while True:
        print_banner("User Dashboard")
        print("""
        1. View Details
        2. Pay Bill
        3. Update Details
        4. Exit
        """)
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_details_menu(customer)
            elif choice == 2:
                pay_bill_menu(customer)
            elif choice == 3:
                update_details_menu(customer)
            elif choice == 4:
                print_message("Thank you for using USTP OmniCharge!")
                break
            else:
                print_message("Invalid choice, please try again.")
        except ValueError:
            print_message("Invalid input. Please enter a number between 1 and 4.")

# Submenus
def view_details_menu(customer):
    while True:
        print_banner("Consumer Details")
        print(f"Account Number : {customer.account_no}")
        print(f"Name           : {customer.name}")
        print(f"Phone Number   : {customer.phone_no}")
        print(f"Address        : {customer.address}")
        if customer.bills:
            print("\n--- Payment History ---")
            for bill in customer.bills:
                print(f"Units Consumed: {bill.units}, Bill Amount: {bill.bill_amount:.2f}, Date: {bill.payment_date}")
        else:
            print("\nNo payment history found.")
        print_separator()
        
        print("\n1. Go Back to Dashboard")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            break
        else:
            print_message("Invalid choice. Please select '1' to go back.")

def pay_bill_menu(customer):
    print_banner("Pay Your Bill")
    bill_rate = 11.42  # Cost per unit in kWh
    exit_loop = False
    
    while not exit_loop:
        try:
            print("Please type 'back' to go back")
            units = input("Enter the units consumed (kWh): ").strip()
            if units.lower() == 'back':
                break
            units = float(units)
            
            total_bill = units * bill_rate
            payment_date = datetime.now().date()

            print("\n--- Bill Calculation ---")
            print(f"Units Consumed: {units} kWh")
            print(f"Bill Rate     : {bill_rate} per unit")
            print(f"Total Bill    : {total_bill:.2f}")
            print(f"Payment Date  : {payment_date}")
            print_separator()
        except ValueError:
            print("Please enter a numeric value or tpye 'back' to exit")
            continue
        while True:
            print("1. Confirm Payment")
            print("2. Go Back")
            confirm = input("Enter your choice: ").lower()
            if confirm == '1':
                new_bill = Bill(units, total_bill, payment_date)
                customer.bills.append(new_bill)
                print_message("Payment Successful! Thank you for using our service.")
                exit_loop = True
                break
            elif confirm == '2':
                print_message("Payment canceled.")
                exit_loop = True
                break
            else:
                print("Invalid input, 1 - 2 only")
                continue


def update_details_menu(customer):
    while True:
        print_banner("Update Your Details")
        new_phone = input("Enter your new phone number: ").strip()
        new_address = input("Enter your new address: ").strip()

        customer.phone_no = new_phone
        customer.address = new_address
        print_message("Details Updated Successfully!")

        print("\n1. Go Back to Dashboard")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            break
        else:
            print_message("Invalid choice. Please select '1' to go back.")

# Main
system = ElectricityBillingSystem()

while True:
    print_banner("Main Menu")
    print("1. Create Your Account")
    print("2. Log In")
    print("3. Exit")
    print_separator()

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_account(system)
        elif choice == 2:
            log_in(system)
        elif choice == 3:
            print_message("Thank you for visiting USTP OmniCharge CDO!")
            break
        else:
            print_message("Invalid choice, please try again.")
    except ValueError:
        print_message("Invalid input. Please enter a number between 1 and 3.")

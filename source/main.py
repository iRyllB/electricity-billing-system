from datetime import datetime, timedelta
from receipt_generator import generate_receipt_pdf
import pandas as pd
from bill_printer import print_bill_details
from classes import Customer, Bill, ElectricityBillingSystem
from ui import print_banner, print_message, print_separator
from validation import is_valid_email, is_valid_password, is_valid_phone_number, check_if_account_exists

#################################################################################################################
# USER-MANAGEMENT USER-MANAGEMENT USER-MANAGEMENT USER-MANAGEMENT USER-MANAGEMENT USER-MANAGEMENT USER-MANAGEMENT
#################################################################################################################
# Account Creation
def create_account(system):
    print_banner("Create Your Account")
    print("Type 'back' at any time to return to the main menu.")

    while True:
        username = input("Enter your username: ").strip()
        if username.lower() == 'back':
            return
        if username != "":
            break
        print_message("Error: Username cannot be blank.")

    while True:
        email = input("Enter your email: ").strip()
        if email.lower() == 'back':
            return
        if is_valid_email(email):  
            break
        print_message("Error: Invalid email format. Please enter a valid email.")

    if check_if_account_exists(username, email, system.customers):
        print_message("Error: Username or email already exists. Please choose a different one.")
        return

    while True:
        first_name = input("Enter your first name: ").strip()
        if first_name.lower() == 'back':
            return
        if first_name.isalpha():
            break
        print_message("Error: First name cannot contain digits or be blank.")

    while True:
        last_name = input("Enter your last name: ").strip()
        if last_name.lower() == 'back':
            return
        if last_name.isalpha():
            break
        print_message("Error: Last name cannot contain digits or be blank.")

    while True:
        password = input("Enter your password: ").strip()
        if password.lower() == 'back':
            return
        if is_valid_password(password): 
            break
        print_message("Error: Password must be at least 5 characters long, and include numbers.")

    while True:
        phone_no = input("Enter your phone number (11 digits): ").strip()
        if phone_no.lower() == 'back':
            return
        if is_valid_phone_number(phone_no): 
            break
        print_message("Error: Phone number must be exactly 11 digits.")

    while True:
        address = input("Enter your address: ").strip()
        if address.lower() == 'back':
            return
        if address != "":
            break
        print_message("Error: Address cannot be blank.")

    account_no = system.create_account(username, email, first_name, last_name, password, phone_no, address)
    print_message(f"Account Created Successfully! Your Account Number: {account_no}")

# Login
def log_in(system):
    print_banner("Log In to Your Account")
    print("Type 'back' at any time to return to the main menu.")

    username = input("Enter your username: ").strip()
    if username.lower() == 'back':
        return
    password = input("Enter your password: ").strip()
    if password.lower() == 'back':
        return

    customer = system.log_in(username, password)
    if customer:
        print_message(f"Welcome, {customer.first_name}!")
        user_dashboard(system, customer)
    else:
        print_message("Invalid credentials. Please try again.")

#################################################################################################################
# DASHBOARD DASHBOARD DASHBOARD DASHBOARD DASHBOARD DASHBOARD DASHBOARD DASHBOARD DASHBOARD DASHBOARD DASHBOARD
#################################################################################################################
# User Dashboard
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

# View Details
def view_details_menu(customer):
    while True:
        print_banner("Consumer Details")
        print(f"Account Number : {customer.account_no}")
        print(f"Username       : {customer.username}")
        print(f"Email          : {customer.email}")
        print(f"Name           : {customer.first_name} {customer.last_name}")
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

# Pay Bill
def pay_bill_menu(customer):
    TAX_RATE = 12  # VAT rate
    print_banner("Pay Your Bill")
    data = pd.read_csv("random_kwh_consumption_due_dates.csv")
    random_row = data.sample(n=1).iloc[0]
    units = random_row['kWh_Consumed']
    due_date = random_row['Due_Date']
    exit_loop = False
    
    generation_charge = 11.42  # Bill rate
    transmission_charge = 0.8786
    sysloss_charge = 1.045
    distribution_charge = 0.4613
    supply_charge = 0.5376
    metering_charge = 0.3205
    rp_tax_provision = 0.0105
    franchi_tax_cur = 0.0022
    business_tax_cur = 0.0085
    
    total_bill = units * generation_charge
    
    total_bill += (transmission_charge + sysloss_charge +
                   distribution_charge + supply_charge + metering_charge +
                   rp_tax_provision + franchi_tax_cur + business_tax_cur)
    
    total_bill_with_vat = total_bill * (1 + TAX_RATE / 100)
    
    payment_date = datetime.now().date()
    next_due_date = (datetime.strptime(due_date, '%Y-%m-%d') + timedelta(days=30)).date()

    # Call the function from bill_printer.py to print the bill details
    print_bill_details(units, generation_charge, transmission_charge, sysloss_charge, 
                       distribution_charge, supply_charge, metering_charge, rp_tax_provision, 
                       franchi_tax_cur, business_tax_cur, total_bill_with_vat, total_bill, 
                       due_date, payment_date, next_due_date, TAX_RATE)

    while True:
        print("1. Confirm Payment")
        print("2. Go Back")
        confirm = input("Enter your choice: ").lower()
        if confirm == '1':
            new_bill = Bill(units, total_bill_with_vat, payment_date, due_date, next_due_date)
            customer.bills.append(new_bill)
            
            generate_receipt_pdf(customer, units, total_bill_with_vat, payment_date, TAX_RATE, due_date, next_due_date)
            
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

# Update Details
def update_details_menu(customer):
    while True:
        print_banner("Update Your Details")

        while True:
            new_phone = input("Enter your new phone number (11 digits, numbers only): ").strip()
            if new_phone.lower() == 'back':
                return
            if not is_valid_phone_number(new_phone):
                print_message("Error: Phone number must be exactly 11 digits and contain only numbers. Please try again.")
            else:
                break

        while True:
            new_address = input("Enter your new address: ").strip()
            if new_address.lower() == 'back':
                return
            if not new_address:
                print_message("Error: Address cannot be blank. Please try again.")
            else:
                break

        customer.phone_no = new_phone
        customer.address = new_address

        print_message("Your details have been updated successfully!")
        break

#################################################################################################################
#MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
#################################################################################################################
# Main Loop
system = ElectricityBillingSystem()

while True:
    print_banner("Main Menu")
    print("1. Create Account")
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
            print_message("Thank you for using USTP OmniCharge!")
            break
        else:
            print_message("Invalid choice, please try again.")
    except ValueError:
        print_message("Invalid input. Please enter a number between 1 and 3.")

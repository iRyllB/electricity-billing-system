from ui_validation import print_message, print_banner, print_separator, is_valid_phone_number
from export import export_payment_history
import pandas as pd
from datetime import datetime, timedelta
from bill_printer import print_bill_details
from classes import Bill
from receipt_generator import generate_receipt_pdf

# User Dashboard
def user_dashboard(system, customer):
    while True:
        print_banner("User Dashboard")
        print(""" 
        1. View Details 
        2. Pay Bill 
        3. Update Details 
        4. Export Payment History
        5. Exit
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
                export_payment_history(customer)
            elif choice == 5:
                print_message("Thank you for using USTP OmniCharge!")
                break
            else:
                print_message("Invalid choice, please try again.")
        except ValueError:
            print_message("Invalid input. Please enter a number between 1 and 5.")

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
import os
from ui_validation import print_banner, print_message
from classes import Bill
from datetime import datetime, timedelta
import pandas as pd
from receipt_generator import generate_receipt_pdf
from bill_printer import print_bill_details
import subprocess

# Pay Bill
def pay_bill_menu(customer):
    TAX_RATE = 12  # VAT rate
    print_banner("Pay Your Bill")

    #automates the generation of consumption and due date on file "generate_data.py"
    data_file = "random_kwh_consumption_due_dates.csv"
    if not os.path.exists(data_file):
        subprocess.run(["python", "generate_data.py"]) 
        return pay_bill_menu(customer)

    data = pd.read_csv(data_file)
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

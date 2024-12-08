'''def pay_bill_menu(customer):
    TAX_RATE = 12  # VAT rate
    print_banner("Pay Your Bill")
    data = pd.read_csv("random_kwh_consumption_due_dates.csv")
    random_row = data.sample(n=1).iloc[0]
    units = random_row['kWh_Consumed']
    due_date = random_row['Due_Date']
    exit_loop = False
    
    generation_charge = 11.42 #bill rate
    transmission_charge = 0.8786
    sysloss_charge = 1.045
    distribution_charge = 0.4613
    supply_charge = 0.5376
    metering_charge = 0.3205
    rp_tax_provision = 0.0105
    franchi_tax_cur = 0.0022
    business_tax_cur = 0.0085
    
    # Calculate the total bill using generation charge as the base
    total_bill = units * generation_charge
    
    total_bill += (transmission_charge + sysloss_charge +
                   distribution_charge + supply_charge + metering_charge +
                   rp_tax_provision + franchi_tax_cur + business_tax_cur)
    
    total_bill_with_vat = total_bill * (1 + TAX_RATE / 100)
    
    payment_date = datetime.now().date()
    next_due_date = (datetime.strptime(due_date, '%Y-%m-%d') + timedelta(days=30)).date()


    print("\n---------------- Bill Calculation ----------------")
    print(f"{'Units Consumed':<27}: {units} kWh")
    
    # Print charges
    print("\nGeneration:")
    print(f"  {'Genr System':<25}: {generation_charge:<10.2f}")
    
    print("Transmission:")
    print(f"  {'Trans System':<25}: {transmission_charge:<10.4f}")
    print(f"  {'SysLoss Chg':<25}: {sysloss_charge:<10.3f}")
    
    print("Distribution:")
    print(f"  {'Dist System':<25}: {distribution_charge:<10.4f}")
    
    print("Supply Charges:")
    print(f"  {'Supp System':<25}: {supply_charge:<10.4f}")
    
    print("Metering Charges:")
    print(f"  {'Meter System':<25}: {metering_charge:<10.4f}")
    
    print("Universal Charges:")
    print(f"  {'RP Tax Provision':<25}: {rp_tax_provision:<10.4f}")
    print(f"  {'Franchi Tax Cur':<25}: {franchi_tax_cur:<10.4f}")
    print(f"  {'Business Tax Cur':<25}: {business_tax_cur:<10.4f}")
    
    print(f"\n{'VAT (12%)':<27}: {total_bill_with_vat - total_bill:<10.2f}")
    print(f"{'Total Bill':<27}: {total_bill_with_vat:<10.2f}")
    print(f"{'Payment Date':<27}: {payment_date}")
    print(f"{'Due Date':<27}: {due_date}")
    print(f"{'Next Due Date':<27}: {next_due_date}")
    print_separator()

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
        '''
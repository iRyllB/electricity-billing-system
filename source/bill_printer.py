def print_bill_details(units, generation_charge, transmission_charge, sysloss_charge, 
                       distribution_charge, supply_charge, metering_charge, rp_tax_provision, 
                       franchi_tax_cur, business_tax_cur, total_bill_with_vat, total_bill, 
                       due_date, payment_date, next_due_date, TAX_RATE):
    print("\n---------------- Bill Calculation ----------------")
    print(f"{'Units Consumed':<27}: {units} kWh")
    
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
    print(" ")
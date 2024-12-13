from ui_validation import print_banner, print_message, print_separator
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

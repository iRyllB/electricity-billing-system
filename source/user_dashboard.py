from submenus.billing import pay_bill_menu
from submenus.view_details import view_details_menu
from submenus.update_details import update_details_menu
from ui_validation import print_message, print_banner
from export import export_payment_history

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

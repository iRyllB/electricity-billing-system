from classes import ElectricityBillingSystem
from ui_validation import print_message, print_banner, print_separator
from user_management import create_account, log_in

def main():
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

if __name__ == "__main__":
    main()

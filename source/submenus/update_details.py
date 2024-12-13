from ui_validation import print_banner, is_valid_phone_number, print_message, is_valid_email
# Update Details
def update_details_menu(customer):
    while True:
        print_banner("Update Your Details")
        print("Type 'back' at any time to return to the main menu.")


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

        while True:
            new_email = input("Enter your new Email address: ").strip()
            if new_address.lower() == 'back':
                return
            if not is_valid_email(new_email):
                print_message("Error: Email is invalid. Please try again.")
            else:
                break

        customer.phone_no = new_phone
        customer.address = new_address
        customer.email = new_email

        print_message("Your details have been updated successfully!")
        break
from ui_validation import print_banner, print_message, check_if_account_exists, is_valid_password, is_valid_email, is_valid_phone_number
from user_dashboard import user_dashboard

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
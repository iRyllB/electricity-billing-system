import re

#DISREGARD NI DAPIT

def print_banner(title):
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

def print_separator():
    print("-" * 50)

def print_message(message):
    print("\n" + f"{message}".center(50))
    print()

print_banner("Welcome to USTP OmniCharge CDO")






# SUGOD DANI NAKO NAG MODIFY
class ElectricityBillingSystem:
    def __init__(self):
        self.customers = {}
        self.account_no_counter = 1

    def create_account(self, username, email, first_name, last_name, password, phone_no, address):
        account_no = self.account_no_counter
        self.account_no_counter += 1
        new_customer = Customer(account_no, first_name, last_name, email, password, phone_no, address)
        self.customers[account_no] = new_customer
        return account_no

    def log_in(self, username, password):
        for customer in self.customers.values():
            if customer.first_name == username and customer.password == password:
                return customer
        return None



class Customer:
    def __init__(self, account_no, first_name, last_name, email, password, phone_no, address):
        self.account_no = account_no
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_no = phone_no
        self.address = address
        self.bills = []


# Validation SA PASSWORD IF NA MEET ANG REQUIRMENTS
def is_valid_password(password):
    if (len(password) >= 8 and 
        re.search(r"[a-z]", password) and 
        re.search(r"[A-Z]", password) and 
        re.search(r"[0-9]", password) and 
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return True
    return False


#VALIDATION SA PHONE NUMBRE IF NUMBERIC AND 11 DIGITS
def is_valid_phone_number(phone_no):
    return phone_no.isdigit() and len(phone_no) == 11


# PARA PREVENT SA DUPLICATED ACCOUNTS
def check_if_account_exists(username, email, existing_accounts):
    for customer in existing_accounts.values():
        if customer.first_name == username or customer.email == email:
            return True
    return False


def create_account(system):
    print_banner("Create Your Account")
    print("Type 'back' at any time to return to the main menu.")

    while True:
        username = input("Enter your username: ").strip()
        if username.lower() == 'back':
            return
        email = input("Enter your email: ").strip()
        if email.lower() == 'back':
            return
        
        #TO PREVENT ANY DUPLICATED ACCOUNT
        if check_if_account_exists(username, email, system.customers):
            print_message("Error: Username or email already exists. Please choose a different one.")
        elif username and email:
            break
        else:
            print_message("Error: Username and email cannot be blank or just spaces. Please try again.")

    # First name input
    while True:
        first_name = input("Enter your first name: ").strip()
        if first_name.lower() == 'back':
            return
        if first_name: 
            break
        print_message("Error: First name cannot be blank or just spaces. Please try again.")
    
    # Last name input
    while True:
        last_name = input("Enter your last name: ").strip()
        if last_name.lower() == 'back':
            return
        if last_name: 
            break
        print_message("Error: Last name cannot be blank or just spaces. Please try again.")
    
    # Password input
    while True:
        password = input("Enter your Passkey: ").strip()
        if password.lower() == 'back':
            return
        if is_valid_password(password): 
            break
        print_message("Error: Password must be at least 8 characters long and contain a mix of upper/lowercase letters, numbers, and special characters. Please try again.")

    # VALIDATION SA PHONE NUMBER IF NUMERIC AND 11 DIGITS
    while True:
        phone_no = input("Enter your phone number: ").strip()
        if phone_no.lower() == 'back':
            return
        if is_valid_phone_number(phone_no): 
            break
        print_message("Error: Phone number must be exactly 11 digits. Please try again.")

    # Address input
    while True:
        address = input("Enter your address: ").strip()
        if address.lower() == 'back':
            return
        if address: 
            break
        print_message("Error: Address cannot be blank or just spaces. Please try again.")

    #ERROR HANDLING 
    try:
        account_no = system.create_account(username, email, first_name, last_name, password, phone_no, address)
        print_message(f"Account Created Successfully!\nYour Account Number: {account_no}")
    except Exception as e:
        print_message(f"Error: {e}")


#CHECKING 
system = ElectricityBillingSystem()

create_account(system)

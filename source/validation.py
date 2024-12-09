import re
def is_valid_password(password):
    return (len(password) >= 5 and 
            re.search(r"[a-z]", password) and 
            re.search(r"[0-9]", password))

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_valid_phone_number(phone_no):
    return phone_no.isdigit() and len(phone_no) == 11

def check_if_account_exists(username, email, existing_accounts):
    for customer in existing_accounts.values():
        if customer.username == username or customer.email == email:
            return True
    return False
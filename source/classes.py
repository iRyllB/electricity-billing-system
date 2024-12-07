class Customer:
    def __init__(self, account_no, username, email, first_name, last_name, password, phone_no, address):
        self.account_no = account_no
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.phone_no = phone_no
        self.address = address
        self.bills = []

class Bill:
    def __init__(self, units, bill_amount, payment_date, due_date, next_due_date):
        self.units = units
        self.bill_amount = bill_amount
        self.payment_date = payment_date
        self.due_date = due_date
        self.next_due_date = next_due_date

class ElectricityBillingSystem:
    def __init__(self):
        self.customers = {}
        self.account_no_counter = 1
        self.create_default_customers()

    def create_account(self, username, email, first_name, last_name, password, phone_no, address):
        account_no = self.account_no_counter
        self.account_no_counter += 1
        new_customer = Customer(account_no, username, email, first_name, last_name, password, phone_no, address)
        self.customers[account_no] = new_customer
        return account_no
    
    def create_default_customers(self):
        self.create_account(
            "bryll123", "gwapoko@gmail.com", "Bryll", "Pon", "bryll123", "09123456789", "123 Main St")

    def log_in(self, username, password):
        for customer in self.customers.values():
            if customer.username == username and customer.password == password:
                return customer
        return None


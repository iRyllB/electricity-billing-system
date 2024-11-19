import mysql.connector as sql
from mysql.connector import Error
from datetime import datetime

# DATABASE CONNECTION (DO NOT MODIFY)
try:
    conn = sql.connect(host="localhost", user="root", passwd="2115200511", database="electricity_data1")
    mycursor = conn.cursor()
    if conn.is_connected():
        print("Connection With Database Established Successfully")
except Error as e:
    print(f"Error connecting to database: {e}")
    exit()

print("Welcome to USTP OmniCharge CDO")

#GLOBAL ACCOUNT NUMBER 
account_no_counter = 1

##############################################################################################################

##############################################################################################################

# CREATE ACCOUNT
def create_account():
    global account_no_counter 
    account_no = str(account_no_counter)
    account_no_counter += 1

    cust_name = input("Enter the consumer name: ")

    while True:
        try:
            password = int(input("Enter your Passkey: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for Passkey.")

    while True:
        try:
            phone_no = int(input("Enter your phone number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid phone number.")

    address = input("Enter your address: ")

    try:
        SQL_insert = "INSERT INTO log_in (account_no, cust_name, password, phone_no, address) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(SQL_insert, (account_no, cust_name, password, phone_no, address))
        conn.commit()
        print(f"Account Created Successfully! Your Account Number: {account_no}")
    except Error as e:
        print(f"Error creating account: {e}")

# LOG IN
def log_in():
    print("\nEnter your Credentials")
    cust_name = input("Enter your name: ")

    while True:
        try:
            password = int(input("Enter your Passkey: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for Passkey.")

    try:
        mycursor.execute("SELECT * FROM log_in WHERE cust_name = %s AND password = %s", (cust_name, password))
        user_data = mycursor.fetchone()

        if user_data:
            print("\nWELCOME TO USTP OMNICHARGE CDO\n")
            user_dashboard(user_data)
        else:
            print("Invalid Credentials, please try again.")
    except Error as e:
        print(f"Error logging in: {e}")

# USER DASHBOARD
def user_dashboard(user_data):
    while True:
        print("""
        TO SEE your details, press               : 1
        TO PAY the bill, press                   : 2
        TO UPDATE your details, press            : 3
        TO EXIT, press                           : 4
        TO RATE US, press                        : 5
        """)
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                show_consumer_details(user_data)
            elif choice == 2:
                pay_bill(user_data)
            elif choice == 3:
                update_details(user_data)
            elif choice == 4:
                print("Thank you for visiting.")
                break
            elif choice == 5:
                rate_service()
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# SHOW CONSUMER DETAILS
def show_consumer_details(user_data):
    try:
        print("\n--- Consumer Details ---")
        print(f"Account Number: {user_data[0]}")
        print(f"Name: {user_data[1]}")
        print(f"Phone Number: {user_data[3]}")
        print(f"Address: {user_data[4]}")

        #Fetch Payment History
        mycursor.execute("SELECT units, bill, payment_date FROM consumer_details WHERE account_no = %s", (user_data[0],))
        payment_history = mycursor.fetchall()

        if payment_history:
            print("\n--- Payment History ---")
            for payment in payment_history:
                payment_date = payment[2].strftime("%Y-%m-%d") if payment[2] else "N/A"
                print(f"Units Consumed: {payment[0]}, Bill Amount: {payment[1]:.2f}, Date: {payment_date}")
        else:
            print("No payment history found.")
    except Error as e:
        print(f"Error fetching consumer details: {e}")

# UPDATE DETAILS
def update_details(user_data):
    new_phone = input("Enter your new phone number: ")
    new_address = input("Enter your new address: ")

    try:
        SQL_update = "UPDATE log_in SET phone_no = %s, address = %s WHERE account_no = %s"
        mycursor.execute(SQL_update, (new_phone, new_address, user_data[0]))
        conn.commit()
        print("Details Updated Successfully!")
    except Error as e:
        print(f"Error updating details: {e}")

# PAY BILL
def pay_bill(user_data):
    billrate = 11.42  #COST PER UNIT IN kwph
    try:
        f_name = input("Enter your name (this will be your Consumer Name): ")
        units = int(input("Enter the units consumed (kwph): "))

        total_bill = units * billrate
        payment_date = datetime.now().date() 

        print(f"\n--- Bill Calculation ---")
        print(f"Consumer Name: {f_name}")
        print(f"Units Consumed: {units} kwph")
        print(f"Bill Rate: {billrate} per unit")
        print(f"Total Bill: {total_bill:.2f}")
        print(f"Payment Date: {payment_date}")

        payment = input("Do you wish to proceed with the payment? (y/n): ").lower()
        if payment == 'y':
            SQL_insert = "INSERT INTO consumer_details (account_no, f_name, units, bill, phone_no, address, payment_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(SQL_insert, (user_data[0], f_name, units, total_bill, user_data[3], user_data[4], payment_date))
            conn.commit()
            print("Payment Successful! Thank you for using our service.\n")
        else:
            print("Payment canceled.")
    except ValueError:
        print("Invalid input. Please enter numeric values for units.")
    except Error as e:
        print(f"Error recording bill: {e}")


# RATE SERVICE
def rate_service():
    try:
        rating = int(input("On a scale of 1 to 10, how would you rate us: "))
        message = input("Optional: Please enter a message (or press Enter to skip): ")

        if 1 <= rating <= 10:
            SQL_insert = "INSERT INTO service_ratings (rating, message) VALUES (%s, %s)"
            mycursor.execute(SQL_insert, (rating, message))
            conn.commit()
            print("Thank you for your rating and feedback!")
        else:
            print("Please enter a rating between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a numeric rating.")

# MAIN PROGRAM LOOP
while True:
    print("\n1. CREATE YOUR ACCOUNT")
    print("2. LOG IN")
    print("3. EXIT")
    try:
        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            create_account()
        elif choice == 2:
            log_in()
        elif choice == 3:
            print("Thank you for visiting!")
            break
        else:
            print("Invalid Choice, Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

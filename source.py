import mysql.connector as sql
from mysql.connector import Error

# DATABASE CONNECTION, DO NOT MODIFY
try:
    conn = sql.connect(host="localhost", user="root", passwd="2115200511", database="electricity_data1")
    mycursor = conn.cursor()
    if conn.is_connected():
        print("Connection With Database Established Successfully")
except Error as e:
    print(f"Error connecting to database: {e}")
    exit()

print("Welcome to USTP OmniCharge CDO")

#########################################################################################################################
while True:
    #CREATE ACCOUNT
    def create_account():
        cust_name = input("Enter the consumer name: ")

        while True:
            try:
                account_no = int(input("Enter your User ID given by the company: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for User ID.")
        
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

        try:
            SQL_insert = "INSERT INTO Log_in (cust_name, account_no, password, phone_no) VALUES (%s, %s, %s, %s)"
            mycursor.execute(SQL_insert, (cust_name, account_no, password, phone_no))
            conn.commit()
            print("Account Created Successfully")
        except Error as e:
            print(f"Error creating account: {e}")

    #LOGIN
    def log_in():
        print("\nEnter your Credentials")
        cust_name = input("Enter your name: ")

        while True:
            try:
                account_no = int(input("Enter your User ID given by company: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for User ID.")

        while True:
            try:
                password = int(input("Enter your Passkey: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for Passkey.")
        
        try:
            mycursor.execute("SELECT * FROM Log_in WHERE cust_name = %s AND account_no = %s AND password = %s", (cust_name, account_no, password))
            user_data = mycursor.fetchone()
            
            if user_data:
                print("\nWELCOME TO USTP OMNICHARGE CDO\n")
                user_dashboard(user_data)
            else:
                print("Invalid Credentials, please try again.")
        except Error as e:
            print(f"Error logging in: {e}")

    #DASHBOARD
    def user_dashboard(user_data):
        while True:
            print("""
            TO SEE your details, press              : 1
            TO PAY the bill, press                   : 2
            TO EXIT, press                           : 3
            TO RATE US, press                        : 4
            """)
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    show_consumer_details(user_data)
                elif choice == 2:
                    pay_bill(user_data)
                elif choice == 3:
                    print("Thank you for visiting.")
                    break
                elif choice == 4:
                    rate_service()
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

    def show_consumer_details(user_data):
        try:
            # Display personal information
            print("\n--- Consumer Details ---")
            print(f"Name: {user_data[0]}")
            print(f"Customer ID: {user_data[1]}")
            print(f"Phone Number: {user_data[3]}")  # user_data[3] should contain phone number
            
            # Fetch payment history
            mycursor.execute("SELECT * FROM consumer_details WHERE account_no = %s", (user_data[1],))
            payment_history = mycursor.fetchall()

            if payment_history:
                print("\n--- Payment History ---")
                for payment in payment_history:
                    print(f"Units Consumed: {payment[1]}, Bill Amount: {payment[3]:.2f}, Date: {payment[4]}")
            else:
                print("No payment history found.")
                
            print("\nVisit again!")
        except Error as e:
            print(f"Error fetching consumer details: {e}")

    def pay_bill(user_data):
        billrate = 11.42  # Cost per unit in the electricity bill
        
        try:
            # Get user details
            f_name = input("Enter your name (this will be your Consumer Name): ")
            units = int(input("Enter the units consumed: "))  # Number of units consumed by the consumer
            
            # Calculate the total bill based on units consumed
            total_bill = units * billrate
            
            # Display the bill amount to be paid
            print(f"\n--- Bill Calculation ---")
            print(f"Name: {f_name}")
            print(f"Units Consumed: {units} units")
            print(f"Bill Rate: {billrate} per unit")
            print(f"Total Bill: {total_bill:.2f}")
            
            # Ask the user to confirm payment
            while True:
                payment = input("Do you wish to proceed with the payment? (yes/no): ").lower()
                if payment == 'yes':
                    # Insert the bill data into the database, assuming `account_no` is part of the user data
                    SQL_insert = "INSERT INTO consumer_details (account_no, f_name, units, bill, phone_no) VALUES (%s, %s, %s, %s, %s)"
                    mycursor.execute(SQL_insert, (user_data[1], f_name, units, total_bill, user_data[3]))
                    conn.commit()
                    
                    # Display receipt after payment
                    print(f"\n--- Payment Receipt ---")
                    print(f"Consumer Name: {f_name}")
                    print(f"Units Consumed: {units} units")
                    print(f"Bill Rate: {billrate} per unit")
                    print(f"Total Amount Due: {total_bill:.2f}")
                    print("Payment Successful! Thank you for using our service.\n")
                    break
                elif payment == 'no':
                    print("Payment canceled. Returning to the main menu.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values for units, bill, and phone number.")
        except Error as e:
            print(f"Error recording bill: {e}")

    def rate_service():
        try:
            rating = int(input("On a scale of 1 to 10, how would you rate us: "))
            if 1 <= rating <= 10:
                print("Thank you for your rating!")
            else:
                print("Please enter a rating between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric rating.")

    # Main Program Loop

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
        else:
            print("Invalid Choice, Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

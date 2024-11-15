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
        
        try:
            SQL_insert = "INSERT INTO Log_in (cust_name, account_no, password) VALUES (%s, %s, %s)"
            mycursor.execute(SQL_insert, (cust_name, account_no, password))
            conn.commit()
            print("Account Created Successfully")
        except Error as e:
            print(f"Error creating account: {e}")

    def log_in():
        print("\nEnter your Credentials")
        cust_name = input("Enter your name: ")

        while True:
            try:
                account_no = int(input("Enter your User ID given by the electricity board: "))
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
                user_dashboard()
            else:
                print("Invalid Credentials, please try again.")
        except Error as e:
            print(f"Error logging in: {e}")

    def user_dashboard():
        while True:
            print("""
            TO SEE employee list, press              : 1
            TO UPDATE DETAILS of employee, press     : 2
            TO SEE consumer details, press           : 3
            TO PAY the bill, press                   : 4
            TO EXIT, press                           : 5
            TO RATE US, press                        : 6
            """)
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    show_employees()
                elif choice == 2:
                    update_employee()
                elif choice == 3:
                    show_consumer_details()
                elif choice == 4:
                    pay_bill()
                elif choice == 5:
                    print("Thank you for visiting.")
                    break
                elif choice == 6:
                    rate_service()
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

    def show_employees():
        try:
            mycursor.execute("SELECT * FROM Log_in")
            employees = mycursor.fetchall()
            print(f"Total number of employees: {len(employees)}")
            print("Details of all employees are arranged as User Name / ID / Passkey")
            for employee in employees:
                print(employee)
            print("Visit again!")
        except Error as e:
            print(f"Error fetching employee details: {e}")

    def update_employee():
        try:
            emp_name = input("Enter current name: ")
            new_name = input("Enter new name: ")
            update_query = "UPDATE Log_in SET cust_name = %s WHERE cust_name = %s"
            mycursor.execute(update_query, (new_name, emp_name))
            conn.commit()
            print("Your details are successfully updated.")
        except Error as e:
            print(f"Error updating employee details: {e}")

    def show_consumer_details():
        try:
            mycursor.execute("SELECT * FROM consumer_details")
            consumer_data = mycursor.fetchall()
            print(f"Total number of records: {len(consumer_data)}")
            for row in consumer_data:
                print(row)
            print("Visit again!")
        except Error as e:
            print(f"Error fetching consumer details: {e}")

    def pay_bill():
        try:
            f_name = input("Enter your name: ")
            units = int(input("Enter the units consumed by the consumer: "))
            bill = int(input("Enter the bill cost: "))
            cust_name = input("Enter Consumer Name: ")
            phone_no = int(input("Enter Consumer phone number: "))

            SQL_insert = "INSERT INTO consumer_details (f_name, units, bill, cust_name, phone_no) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(SQL_insert, (f_name, units, bill, cust_name, phone_no))
            conn.commit()
            print("Bill recorded successfully.")
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

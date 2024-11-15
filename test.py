print("Welcome to USTP OmniCharge CDO")

#CREATE ACCOUNT FUNCTION
def create_account():
    while True:
        cust_name = input("Enter the consumer name: ")
    

#MAIN
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

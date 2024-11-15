import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="2115200511", database="electricity_data1")
mycursor=conn.cursor()
if conn.is_connected():
    print("Conection With Database Establised Successfully")
else:
    print("Conection With Database Failed XXX")

print("Welcome to ZARONE ELECTRICITY BOARD")

c1=conn.cursor()
choice = 0
while choice != 3:
    print("1.CREATE YOUR ACCOUNT")
    print("2.LOG IN")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice ==1:
     cust_name=input("Enter the consumer name :")
     account_no=int(input("enter your User ID given by electricity board:"))
     password=int(input("Enter your Passkey :"))
     SQL_insert="insert into Log_in values('"+cust_name+"',"+str(account_no)+","+str (password)+")"
     c1.execute(SQL_insert)
     conn.commit()
     print("ACCOUNT CREATED")

    if choice==2:
     print('')
     print('Enter your Credentials')
     cust_name=input('Enter your name : ')
     print('')
     account_no=int(input('Enter your User ID given by electricity board: '))
     print(' ')
     password=int(input('Enter your Passkey : '))
     print(' ')
     c1=conn.cursor()
     c1.execute('select * from Log_in')
     data=c1.fetchall()
     count=c1.rowcount
     for row in data:
        if (cust_name in row) and (account_no in row) and (password in row):
            print(' ')
            print(' ')
            print("WELCOME TO ZARONE ELECTRICITY BOARD")
            print(' ')
            print(' ')
            print('TO SEE employee list,press                    :1')
            print(' ')
            print('TO UPDATE DETAILS of employee,press           :2')
            print(' ')
            print('TO SEE consumer details                       :3')
            print(' ')
            print('TO pay the bill,press                         :4')
            print(' ')
            print('TO EXIT,press                                 :5')
            print(' ')
            print('WANT TO RATE US,press                         :6')
            print(' ')
            c2=int(input('enter your choice : '))

            if (c2==1):
                c1=conn.cursor()
                c1.execute('select * from Log_in')
                data=c1.fetchall()
                count=c1.rowcount
                print('Details of all employees is',count)
                print("Details of all employees are arranged as User Name/ID/Passkey")
                for row in data:
                    print(row)
                print("VISIT AGAIN")

            elif (c2==2):
                print('')
                print('TO UPDATE FILL THIS')
                print('')
                empName = input("Enter name : ")
                update = input("Enter new name : ")
                sqlFormula = "UPDATE Log_in SET cust_name=%s WHERE cust_name = %s"
                c1.execute(sqlFormula,(update,empName))
                conn.commit()

                print('YOUR DETAILS ARE SUCESSFULLY UPDATED')

            elif(c2==4):
                 f_name=input("Enter the your name : ")
                 units=int(input("Enter the units consumed by the consumer : "))
                 bill=int(input("Enter the bill cost :"))
                 cust_name=input("Enter Consumer Name:")
                 phone_no=int(input("Enter Consumer phone no:"))
                 SQL_insert="insert into consumer_details values("+"'"+f_name+"'"+","+"'"+str(units)+"'"+","+"'"+str(bill)+"'"+","+"'"+cust_name+"'"+","+str(phone_no)+")"
                 c1.execute(SQL_insert)
                 conn.commit()
                 print("Bill Recorded")

            elif(c2==3):
                  c1=conn.cursor()
                  c1.execute('select * from consumer_details ')
                  data=c1.fetchall()
                  count=c1.rowcount
                  print('total bill of this month  is',count)
                  for row in data:
                     print(row)
                  print("VISIT AGAIN")

            elif (c2==5):
                print('THANK YOU FOR VISITING')
            

            elif (c2==6):
                print('RATE US FOR SERVICE')
                rating=int(input("On the Scale of 10 how would you like to rate us:"))
                print('THANK FOR RATING')
            else:
                print("Oops, something went wrong, try again...........")

     if choice==3:
      print("THANK YOU FOR VISITING")
      
     else :
       print("Invalid Choice, Please try again")
               
                 
            
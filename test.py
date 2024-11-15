import random
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


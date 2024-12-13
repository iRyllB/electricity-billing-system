# Group 2 
# Members-------------------------------------------------------        
# Villacorta - Leader       |  Computer Programming 1.
# Ello                      |  
# Bologa                    |  Final PIT for 1st semester.
# Recopelacion              |  Instructor: Kim Serenuela Pagal
# Gomez                     |  Section: CS1B
# Moneva                    |
# Tangarocan                |   
#----------------------------------------------------------------
#---------------------Electrical Bill----------------------------

# Overview: 
# This program takes the total bill by taking the current records of your electricity bill
# and subtracting it to the previous record to get the base consumption (if you have already set the record otherwise it is set 
# to 0 by default) and then calculates the total bill to be payed by multiplying the base consumption with the predetermined rates (generation, transmission, system loss, etc.). 

# If the base consumption goes over the threshold for a residential base consumption (e.g. in this case 1500), the exceeded amount will be taken and calculated with the commercial rate and then added to the residential base consumption calculated with the residential rate to get total amount of the bill. The program stores all data inside 2 .csv files, one is for the general information of the user, and the other one is for their records (which will be named after their IDs).

# If the first name and the last name matches some data stored during input, it will automatically retrieve the data such as their previous reading to subract with the current reading and get the base consumption.  

# Additional Notes:
# All the variable declaration are right below the functions.
# You can run the run.bat file to run this program, '.\run'

import csv
import os
import tkinter as tk
import uuid
import time
from datetime import datetime
from datetime import timedelta
from tkinter import messagebox
from PIL import Image, ImageTk
import base64

# save user info
def save_user_info(first_name, last_name, address, curr_read, prev_read = 0):
    try:
        first_name_stringed = str(first_name)
        last_name_stringed = str(last_name)
        address_stringed = str(address)
        curr_read_float = float(curr_read)

        rows = []
        user_found = False
        user_id = ""

        try:
            with open(user_data_file_path, mode="r", newline="") as file:
                reader = csv.reader(file)
                rows = list(reader)
        except FileNotFoundError:
            pass 

        # look for prev read
        for i, row in enumerate(rows):
            if row[1] == first_name_stringed and row[2] == last_name_stringed:
                prev_read = float(row[5])  # Correct index for the previous reading
                rows[i] = [row[0], first_name_stringed, last_name_stringed, 
                           address_stringed, prev_read, curr_read_float]
                user_found = True
                user_id = row[0]
                break

        # if not found add entry w/ prev 0
        if not user_found:
            unique_id = base64.urlsafe_b64encode((uuid.uuid4()).bytes).rstrip(b'=').decode('utf-8')
            rows.append([unique_id, first_name_stringed, last_name_stringed, 
                         address_stringed, prev_read, curr_read_float])

        with open(user_data_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)


        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not user_id:
            rows2 = []
            with open(user_data_file_path, mode="r", newline="") as file:
                reader = csv.reader(file)
                rows2 = list(reader)

            for i, row in enumerate(rows2):
                if row[1] == first_name_stringed and row[2] == last_name_stringed:
                    user_id = row[0]
                    break

        file_name = f"{user_id}.csv"
        file_path = os.path.join(script_dir, f"../data/records/{file_name}")

        try:
            with open(file_path, mode="a", newline="") as file:
                    
                writer = csv.writer(file)
                
                if file.tell() == 0:
                    writer.writerow(['Current Reading', 'Timestamp'])
                writer.writerow([curr_read_float, current_time])

        except Exception as e:
            messagebox.showerror("Error", f"Error while creating records")
    except Exception as e:
        messagebox.showerror("Error", f"An error occured while saving the user info: {e}")

def calculate_bill():
    try:
        # residential rates 
        residential_generation_rate = 3.6273
        residential_transmission_rate = 1.1423
        residential_system_loss_rate = 0.5621
        residential_distribution_rate = 1.3426
        residential_subsidies_rate = 0.0145
        residential_government_tax_rate = 0.1250
        residential_universal_charges_rate = 0.0426
        residential_fit_all_renewable_rate = 0.1682

        # commercial rates 
        commercial_generation_rate = 4.5474
        commercial_transmission_rate = 1.2456
        commercial_system_loss_rate = 0.8921
        commercial_distribution_rate = 1.6393
        commercial_subsidies_rate = 0.0200
        commercial_government_tax_rate = 0.1250
        commercial_universal_charges_rate = 0.0513
        commercial_fit_all_renewable_rate = 0.2226

        # vars
        total = 0
        prev_record = 0
        curr_record = float(entry_usage.get())
        customer_type = ""
        threshold = 1800
        residential_base_consumption = 0
        commercial_base_consumption = 0
        total_residential = 0
        total_commercial = 0
        residential_rate = 0
        commercial_rate = 0

        # rate lists
        residential_rate_list = [round(residential_generation_rate, 2), round(residential_transmission_rate, 2), round(residential_system_loss_rate, 2), round(residential_distribution_rate, 2), round(residential_subsidies_rate, 2), round(residential_government_tax_rate, 2), round(residential_universal_charges_rate, 2), round(residential_fit_all_renewable_rate, 2)]

        commercial_rate_list = [round(commercial_generation_rate, 2), round(commercial_transmission_rate, 2), round(commercial_system_loss_rate, 2), round(commercial_distribution_rate, 2), round(commercial_subsidies_rate, 2), round(commercial_government_tax_rate, 2), round(commercial_universal_charges_rate, 2), round(commercial_fit_all_renewable_rate, 2)]

        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        address = entry_address.get()
        


        # bill due dates logic
        curr_date = datetime.now()
        billing_start_date = None
        billing_end_date = None

        if user_exist(first_name, last_name):    
            prev_record = float(get_last_record(first_name, last_name)['Current Reading'])

        billing_start_date = datetime(curr_date.year, curr_date.month, 1)
        billing_trans_date = curr_date
        billing_end_date = add_one_month(billing_start_date)


        if curr_record <= prev_record:
            messagebox.showerror("Error", "Current record should be higher and doesn't equal to the previous one")
            return
        
        # gets the base consumption
        base_consumption = curr_record - prev_record

        # takes the residential and commercial 
        if base_consumption > threshold:
            commercial_base_consumption = base_consumption - threshold
            residential_base_consumption = threshold
     
            # calculate base consumption to residential rates
            for i in range(len(residential_rate_list)):
                total_residential += base_consumption * residential_rate_list[i]
            
            # calculate base consumption to commercial rates
            for i in range(len(commercial_rate_list)):
                total_commercial += base_consumption * commercial_rate_list[i]

            residential_rate = total_residential / residential_base_consumption
            commercial_rate = total_commercial / commercial_base_consumption
            total = total_commercial + total_residential
        else:
            residential_base_consumption = base_consumption
            # calculate base consumption to residential rates
            for i in range(len(residential_rate_list)):
                total_residential += residential_base_consumption * residential_rate_list[i]
            
            residential_rate = total_residential / residential_base_consumption
            total = total_residential

        save_user_info(first_name, last_name, address, curr_record)

        if not first_name or not last_name or not address or not base_consumption:
            messagebox.showerror("Input Error", "Please fill in all customer or usage details.")
            return

        global bill_text
        bill_text = (
                f"Electricity Bill\n\n"
                f"Transaction Date: {str(billing_start_date)[0:10]}\n"
                f"Billing Period Date: {str(billing_start_date)[0:10]} to {str(billing_end_date)[0:10]}\n\n"
                f"Customer Details:\n"
                f" Customer Name: {first_name} {last_name}\n"
                f" Address: {address}\n"
                f"Usage Details:\n"
                f" Residential Threshold (kWh): {threshold} \n"
                f" Current Record (kWh): {curr_record} \n"
                f" Previous Record (kWh): {prev_record} \n"
                f" Base Consumption (kWh): {base_consumption} \n"
                f" Residential Base Consumption (kWh): {residential_base_consumption} \n"
                f" Commercial Base Consumption (kWh): {commercial_base_consumption} \n"
                f"Bill Computation Summary:\n"
                f"{'-'*60}\n"
                f"{'':<34}{'Residential':<15}{'Commercial':<15}\n"
                f"{'-'*60}\n"
                f"Generation Rate (PHP/kWh):{'':<11}{residential_generation_rate:<15.2f}{commercial_generation_rate:<5.2f}\n"
                f"Transmission Rate (PHP/kWh):{'':<9}{residential_transmission_rate:<15.2f}{commercial_transmission_rate:<5.2f}\n"
                f"System Loss Rate (PHP/kWh):{'':<10}{residential_system_loss_rate:<15.2f}{commercial_system_loss_rate:<5.2f}\n"
                f"Distribution Rate (PHP/kWh):{'':<9}{residential_distribution_rate:<15.2f}{commercial_distribution_rate:<5.2f}\n"
                f"Subsidies Rate (PHP/kWh):{'':<12}{residential_subsidies_rate:<15.2f}{commercial_subsidies_rate:<5.2f}\n"
                f"Government Tax Rate (PHP/kWh):{'':<7}{residential_government_tax_rate:<15.2f}{commercial_government_tax_rate:<5.2f}\n"
                f"Universal Charges Rate (PHP/kWh):{'':<4}{residential_universal_charges_rate:<15.2f}{commercial_universal_charges_rate:<5.2f}\n"
                f"Fit All Renewable Rate (PHP/kWh):{'':<4}{residential_fit_all_renewable_rate:<15.2f}{commercial_fit_all_renewable_rate:<5.2f}\n"
                f"{'-'*60}\n"
                f"Residential Blended Rate: (PHP/kWh) {residential_rate:.5f}\n"
                f"Commercial Blended Rate: (PHP/kWh) {commercial_rate:.5f}\n"
                f"Residential Bill: (PHP) {total_residential:.2f}\n"
                f"Commercial Bill: (PHP) {total_commercial:.2f}\n"
                f"Total Bill: (PHP) {total:.2f}\n"
                f"{'-'*60}"
        )
        label_bill.config(
            text=bill_text,
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for usage and rate.")

# this one is tricky, cause i dont want to use dateutil module for calculating the next month. 
# i dont want to hustle the next person to be running this to install a dependency.
# so what i did is i calculated it manually, leap years and common years stuff like that.
def add_one_month(date):
    
    month = date.month + 1
    year = date.year
    if month > 12:  
        month = 1
        year += 1
    
    if month == 12: 
        next_month_start = datetime(year + 1, 1, 1)  
    else:
        next_month_start = datetime(year, month + 1, 1)  

    last_day_of_month = next_month_start - timedelta(days=1)

    day = min(date.day, last_day_of_month.day)
    
    return datetime(year, month, day)

def user_exist(first_name, last_name):
    if(first_name and last_name):
        with open(user_data_file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["First Name"] == first_name and row["Last Name"] == last_name:
                    return True    
    return False


def get_last_record(first_name, last_name):
    user_records_file_path = os.path.join(script_dir, "../data/records")
    target_file_name = None
    latest_row = None
    latest_timestamp = None

     # open & read data.csv
    if(first_name and last_name):
        with open(user_data_file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["First Name"] == first_name and row["Last Name"] == last_name:
                    target_file_name = row['ID']
    
        # loop through dir 
        for root, dirs, files in os.walk(user_records_file_path):
            target_file_name += ".csv"
            if target_file_name in files:
                file_path = os.path.join(root, target_file_name)
                
                # read .csv find latest row
                with open(file_path, mode="r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # timestamp to datetime obj
                        row_timestamp = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S")
                        if not latest_timestamp or row_timestamp > latest_timestamp:
                            latest_timestamp = row_timestamp
                            latest_row = row
                
                break  # stops when found

    return latest_row

def clear_fields():
    try:
        entry_first_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_usage.delete(0, tk.END)
        label_bill.config(text="Electricity Bill\n\n[Fill out details to calculate]")
    except Exception as e:
        messagebox.showerror("Error", f"An error occured while clearing the fields: {e}")

# abs path
script_dir = os.path.dirname(os.path.abspath(__file__))
user_data_file_path = os.path.join(script_dir, "data.csv")

# ui part
root = tk.Tk()
root.title("Electrical Bill Profile")

# conf. column weights allow flex. resizing
root.grid_columnconfigure(0, weight=1)  
root.grid_columnconfigure(1, weight=1) 
root.grid_columnconfigure(2, weight=1)  

# load logo
try:
    icon_path = os.path.join(script_dir, "../assets/logo.png")
    ico = Image.open(icon_path)
    photo = ImageTk.PhotoImage(ico)

    # set icon
    root.wm_iconphoto(False, photo)
except FileNotFoundError:
    messagebox.showerror("Error", "File not found error, make sure the icon's path is correct (tkinter section)")
except Exception as e:
    messagebox.showerror("Error", f"An error occured while loading the image: {e}")

frame_customer = tk.LabelFrame(root, text="Customer Details", padx=10, pady=10)
frame_customer.grid(row=0, column=0, padx=10, pady=5)


tk.Label(frame_customer, text="First Name:").grid(row=0, column=0, sticky="e")
entry_first_name = tk.Entry(frame_customer, width=30)  
entry_first_name.grid(row=0, column=1)

tk.Label(frame_customer, text="Last Name:").grid(row=1, column=0, sticky="e")
entry_last_name = tk.Entry(frame_customer, width=30)  
entry_last_name.grid(row=1, column=1)

tk.Label(frame_customer, text="Address:").grid(row=2, column=0, sticky="e")
entry_address = tk.Entry(frame_customer, width=30)
entry_address.grid(row=2, column=1)

frame_usage = tk.LabelFrame(root, text="Usage Details", padx=10, pady=10)
frame_usage.grid(row=0, column=2, padx=10, pady=5)

tk.Label(frame_usage, text="Current Usage (kWh):").grid(row=0, column=0, sticky="e")
entry_usage = tk.Entry(frame_usage, width=10)
entry_usage.grid(row=0, column=1)

# buttons for action
frame_buttons = tk.Frame(root, padx=10, pady=10)
frame_buttons.grid(row=1, column=2)

button_calculate = tk.Button(frame_buttons, text="Generate Bill", command=calculate_bill)
button_calculate.grid(row=0, column=0, padx=5)

button_clear = tk.Button(frame_buttons, text="Clear", command=clear_fields)
button_clear.grid(row=0, column=1, padx=5)

# display bill
frame_bill = tk.LabelFrame(root, text="Generated Bill", padx=10, pady=10)
frame_bill.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=10)  # spans 3 col.

bill_text = ""
label_bill = tk.Label(frame_bill, text="Electricity Bill\n\n[Fill out details to calculate]", justify="left", font=("Courier", 9), anchor="w")
label_bill.grid(row=0, column=0, sticky="w")


# start loop
root.mainloop()
# Define required libraries.
import datetime
import csv
import os
import pandas as pd

# Read defaults file
def read_defaults():
    with open("Defaults.dat", "r") as file:
        line = file.readline().strip()
        parts = line.split(",")
        return {
            "NextTransaction": int(parts[0]),
            "NextDriverID": int(parts[1]),
            "MonthlyStandFee": float(parts[2]),
            "DailyRentalFee": float(parts[3]),
            "WeeklyRentalFee": float(parts[4]),
            "HSTRate": float(parts[5])
        }

def write_defaults(defaults):
    with open("Defaults.dat", "w") as file:
        line = f'{defaults["NextTransaction"]},{defaults["NextDriverID"]},{defaults["MonthlyStandFee"]},{defaults["DailyRentalFee"]},{defaults["WeeklyRentalFee"]},{defaults["HSTRate"]}\n'
        file.write(line)

# Employee input 
def new_employee_input(defaults):
    driver_number = int(defaults["NextDriverID"])
    
    employee_name = input("Employee name: ").title()
    address = input("Address: ").title()
    
    phone_num = input("Phone number (10 digits): ")
    while len(phone_num) != 10:
        print("Please enter a valid 10-digit phone number.")
        phone_num = input("Phone number (10 digits): ")

    license_num = input("Driver's license number: ")
    license_exp_date = input("Enter license expiration date (YYYY-MM-DD): ")
    insurance_company = input("Insurance company: ").title()
    insurance_policy_num = input("Policy number: ")

    car_ownership = input("Do they own their car? (Y/N): ").upper()
    while car_ownership not in ["Y", "N"]:
        print("Invalid input, please enter Y for Yes, or N for No.")
        car_ownership = input("Do they own their car? (Y/N): ").upper()

    balance_due = 0.00

    return (driver_number, employee_name, address, phone_num, license_num,
            license_exp_date, insurance_company, insurance_policy_num,
            car_ownership, balance_due)

# Update employee record
def employee_record(defaults, driver_number, employee_name, address, phone_num, license_num, license_exp_date, insurance_company, insurance_policy_num, car_ownership, balance_due):

    file_path = "employees.csv"

    new_data = pd.DataFrame([{
        "EmployeeNumber": driver_number,
        "Name": employee_name,
        "Address": address,
        "Phone": phone_num,
        "LicenseNumber": license_num,
        "LicenseExpiry": license_exp_date,
        "InsuranceCompany": insurance_company,
        "PolicyNumber": insurance_policy_num,
        "OwnCar": car_ownership,
        "BalanceDue": round(balance_due, 2)
    }])

    if os.path.isfile(file_path):
        new_data.to_csv(file_path, mode='a', index=False, header=False)
    else:
        new_data.to_csv(file_path, mode='w', index=False, header=True)
    
    # Update NextDriverID
    defaults["NextDriverID"] += 1
    write_defaults(defaults)

# Main function
def __main__():
    defaults = read_defaults()
    employee_data = new_employee_input(defaults)
    employee_record(defaults, *employee_data)

__main__()

# Define required libraries.
import os
from datetime import date
from random import randint
import pandas as pd

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

def employee_payment():
    defaults = read_defaults()
    payment_id = randint(100000,999999)
    
    driver_number = input("Driver number: ")
    payment_date = str(date.today())
    total_amount = float(input("Amount of payment: $"))
    reason = input("Reason for payment: ")
    payment_method = input("Payment Method (Cash/Debit/Credit): ").title()

    # Write to payments.csv (create if doesn't exist)
    payment_record = pd.DataFrame([{
        "PaymentID": payment_id,
        "EmployeeID": driver_number,
        "PaymentDate": payment_date,
        "TotalPayment": total_amount,
        "ReasonForPayment": reason,
        "PaymentMethod": payment_method,
    }])

    file_path = "payment_record.csv"

    # If the file exists, append without duplicating the header
    if os.path.isfile(file_path):
        payment_record.to_csv(file_path, mode='a', index=False, header=False)
    else:
        # File does not exist, write it with header
        payment_record.to_csv(file_path, mode='w', index=False, header=True)

    print(f"\nPayment of ${total_amount:.2f} recorded for Driver #{driver_number} (Payment ID: {payment_id})")

def update_employee_balance(defaults, driver_number, total_amount):

    file_path = "employees.csv"

    if not os.path.exists(file_path):
        print("Employees.csv file not found.")
        return

    df = pd.read_csv(file_path)

    # Check if driver exists
    if int(driver_number) not in df["EmployeeNumber"].values:
        print(f"Driver #{driver_number} not found.")
        return

    # Update balance in employees.csv df
    df.loc[df["EmployeeNumber"] == int(driver_number), "BalanceDue"] += total_amount

    # Write df change to filepath
    df.to_csv(file_path, index=False)

def __main__():
    read_defaults()
    employee_payment()
    update_employee_balance()

__main__()
    


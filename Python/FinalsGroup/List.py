# Description: Robot Group 3 Python Code

import sys

import datetime as datetime
import FormatValues as FV
import os
from datetime import datetime, timedelta, date
import time
from random import randint
import pandas as pd

# Functions

# Leah
def AddEmployee():
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
    defaults = read_defaults()
    employee_data = new_employee_input(defaults)
    employee_record(defaults, *employee_data)

# Kassaundra
# Function to check if a car is occupied for the given rental period
def CarRent():
    def IsCarOccupied(CarNum, StartDate=None, NumDays=None):
        CarFile = f"Car{CarNum}.dat"
        if not os.path.exists(CarFile):
            return False

        if StartDate is None or NumDays is None:
            with open(CarFile, "r") as file:
                for line in file:
                    return True
            return False

        # Calculate the rental period
        RentalDates = set(
            (StartDate + timedelta(days=i)).strftime("%Y-%m-%d")
            for i in range(NumDays)
        )

        # Check for conflicts in the car's file
        with open(CarFile, "r") as f:
            for XRecord in f:
                _, ExistingStartDate, _, ExistingNumDays, *_ = XRecord.strip().split(", ")
                ExistingStartDate = datetime.strptime(ExistingStartDate, "%Y-%m-%d").date()
                ExistingNumDays = int(ExistingNumDays)

                ExistingRentalDates = set(
                    (ExistingStartDate + timedelta(days=i)).strftime("%Y-%m-%d")
                    for i in range(ExistingNumDays)
                )
                
                if RentalDates & ExistingRentalDates:
                    return True
        return False

    # Open the Defaults.dat file and read the values
    with open("Defaults.dat", "r") as f:
        for XRecord in f:
            XLst = XRecord.split(",")
            TransNum = int(XLst[0].strip())
            EmpNum = int(XLst[1].strip())
            MonthStandFee = float(XLst[2].strip())
            DayRentFee = float(XLst[3].strip())
            WeekRentFee = float(XLst[4].strip())
            HST = float(XLst[5].strip())

    # Check if today is the first day of the month for monthly stand fees
    today = datetime.date.today()
    if today.day == 1:
        with open("Revenue.dat", "a") as f:
            StandFeeTransNum = TransNum
            TransNum += 1

            StandFeeHSTAmt = MonthStandFee * HST
            StandFeeTotal = MonthStandFee + StandFeeHSTAmt

            f.write(
                f"{StandFeeTransNum}, {today}, Monthly Stand Fees, {EmpNum}, {MonthStandFee:.2f}, {StandFeeHSTAmt:.2f}, {StandFeeTotal:.2f}\n"
            )

    # Main program starts here

    while True:
        RentalID = TransNum  # Assign the Rental ID from the transaction number

        while True:
            print()
            StartDate = input("Enter the start date of the rental (YYYY-MM-DD):  ")
            if StartDate == "":
                print()
                print("   Data Entry Error - Start date cannot be blank.")
                print()
            else:
                try:
                    StartDate = datetime.strptime(StartDate, "%Y-%m-%d").date()
                    if StartDate > datetime.date.today():
                        print()
                        print("   Data Entry Error - Start date cannot be in the future.")
                        print()
                    else:
                        break
                except ValueError:
                    print()
                    print("   Data Entry Error - Start date must be in YYYY-MM-DD format.")
                    print()

        while True:
            RentalDur = input("Enter if the rental is for a day or a week (D/W): ").upper()
            if RentalDur == "":
                print()
                print("   Data Entry Error - Rental duration cannot be blank.")
                print()
            elif RentalDur != "D" and RentalDur != "W":
                print()
                print("   Data Entry Error - Rental duration must be D or W.")
                print()
            elif RentalDur == "W":
                RentalDur = "Week"
                NumDays = 7
                RentCost = WeekRentFee
                break
            elif RentalDur == "D":
                RentalDur = "Day"
                while True:
                    NumDays = input("Enter the number of days the car is rented for:   ")
                    if NumDays == "":
                        print()
                        print("   Data Entry Error - Number of days cannot be blank.")
                        print()
                    elif not NumDays.isdigit():
                        print()
                        print("   Data Entry Error - Number of days must be a number.")
                        print()
                    else:
                        NumDays = int(NumDays)
                        RentCost = DayRentFee * NumDays
                        break
                break

        while True:
            CarNum = input("Enter the car number (1, 2, 3, or 4):             ")
            if CarNum == "":
                print()
                print("   Data Entry Error - Car number cannot be blank.")
                print()
            elif CarNum != "1" and CarNum != "2" and CarNum != "3" and CarNum != "4":
                print()
                print("   Data Entry Error - Car number must be 1, 2, 3, or 4.")
                print()
            elif IsCarOccupied(CarNum, StartDate, NumDays):
                print()
                print(f"   Car {CarNum} is currently occupied for the selected dates. Please choose another car.")
                print()
            else:
                break

        # Calculate HST and Total
        HSTRate = RentCost * HST
        Total = RentCost + HSTRate

        # Save the rental information to the specific car file
        CarFile = f"Car{CarNum}.dat"
        with open(CarFile, "a") as file:
            file.write(f"{RentalID}, {StartDate}, {RentalDur}, {NumDays}, {RentCost:.2f}, {HSTRate:.2f}, {Total:.2f}\n")

        # Progress bar for saving the rental information
        print()
        print("Saving rental information...")
        ProgressBarLength = 50
        for i in range(ProgressBarLength + 1):
            percent = (i / ProgressBarLength) * 100
            bar = "█" * i + "░" * (ProgressBarLength - i)
            print(f"\r{bar} {percent:.0f}%", end="")
            time.sleep(0.05)
        print()
        print(f"Rental information saved successfully!")
        print()
        print(f"Start Date: {StartDate}, Car Number: {CarNum}, Rental Duration: {RentalDur}, Number of Days: {NumDays}, Rental Cost: {FV.FDollar2(RentCost)}, HST: {FV.FDollar2(HSTRate)}, Total: {FV.FDollar2(Total)}")

        # Increment the transaction number for the next rental
        TransNum += 1

        # Ask if the user wants to input another transaction
        print()
        Continue = input("Would you like to input another transaction? (Y/N): ").upper()
        if Continue != "Y":
            print()
            print(f"   Thank you for using the Car Rental System. Goodbye!")
            print()
            break
        elif Continue != "N" and Continue != "Y":
            print()
            print("   Data Entry Error - Please enter Y or N.")
            print()

    # Save updated defaults to Defaults.dat
    with open("Defaults.dat", "w") as f:
        f.write(f"{TransNum}, {EmpNum}, {MonthStandFee}, {DayRentFee}, {WeekRentFee}, {HST}\n")

# Leah
def EmployeePayment():
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

    def employee_payment():
        defaults = read_defaults()
        payment_id = randint(100000,999999)
        
        driver_number = input("Driver number: ")
        payment_date = str(datetime.today().date())
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

        return driver_number, total_amount

    def update_employee_balance(defaults, driver_number, total_amount):

        file_path = "employees.csv"

        if not os.path.exists(file_path):
            print("employees.csv file not found.")
            return

        df = pd.read_csv(file_path)

        # Check if driver exists
        if int(driver_number) not in df["EmployeeNumber"].values:
            print(f"Driver #{driver_number} not found.")
            return

        # Update balance in employees.csv df
        if total_amount > (df.loc[df["EmployeeNumber"] == int(driver_number), "BalanceDue"]):
            df.loc[df["EmployeeNumber"] == int(driver_number), "BalanceDue"] -= total_amount

        # Write df change to filepath
        df.to_csv(file_path, index=False)

    defaults = read_defaults()
    driver_number, total_amount = employee_payment()
    update_employee_balance(defaults, driver_number, total_amount)

# Stephen
def RevenueTable():

    # Constants
    CUR_DATE = datetime.now()
        # Format date here real quick
    CUR_DATE = CUR_DATE.strftime("%B %d, %Y")

    # Validation sets
    AllowedPrice = set("1234567890.,$")
    AllowedCharDate = set("1234567890-")

    # Initializing list
    Records = []

    # Main program
    while True:
        # Gathering inputs
        while True:
            StartDate = input("Enter the start date of revenue report (YYYY-MM-DD): ")
            if StartDate == "":
                print()
                print("Please enter a date.")
                print()
            elif set(StartDate).issubset(AllowedCharDate) == False:
                print()
                print("Please enter a valid date.")
                print()
            else:
                try:
                    # Converts to string object and verifies date format
                    StartDateObj = datetime.strptime(StartDate, "%Y-%m-%d")
                    break
                except ValueError:
                    print()
                    print("Invalid date format or non-existent date. Please use YYYY-MM-DD.")
                    print()
        
        while True:
            EndDate = input("Enter the end date of revenue report (YYYY-MM-DD): ")
            if EndDate == "":
                print()
                print("Please enter a date.")
                print()
            elif set(EndDate).issubset(AllowedCharDate) == False:
                print()
                print("Please enter a valid date.")
                print()
            else:
                try:
                    # Converts to string object and verifies date format
                    EndDateObj = datetime.strptime(EndDate, "%Y-%m-%d")
                    break
                except ValueError:
                    print()
                    print("Invalid date format or non-existent date. Please use YYYY-MM-DD.")
                    print()
            
        while True:
            Revenue = input("Enter the revenue for report period: ")
            if Revenue == "":
                print()
                print("Please enter a revenue amount for the report period.")
                print()
            elif set(Revenue).issubset(AllowedPrice) == False:
                print()
                print("Please enter a valid revenue amount (numbers, commas, or $ only).")
                print()
            else:
                try:
                    Revenue = float(Revenue.replace(",", "").replace("$", ""))
                    if Revenue < 0:
                        print()
                        print("Cannot enter negative revenue, please input a valid number.")
                        print()
                    break
                except ValueError:
                    print()
                    print("Please enter a valid numeric revenue amount.")
                    print()
        
        while True:
            Expenses = (input("Enter the expenses for report period: "))    
            if Expenses == "":
                print()
                print("Please enter an expenses amount for the report period.")
                print()
            elif set(Expenses).issubset(AllowedPrice) == False:
                print()
                print("Please enter a valid expenses amount.")
                print()
            else:
                try:
                    Expenses = float(Expenses.replace(",", "").replace("$", ""))
                    if Expenses < 0:
                        print()
                        print("Cannot enter negative expenses, please input a valid number.")
                        print()
                    break
                except ValueError:
                    print()
                    print("Please enter a valid numeric expenses amount.")
                    print()

        # Create list
        Record = {
            "StartDate": StartDateObj.strftime("%Y-%m-%d"),
            "EndDate": EndDateObj.strftime("%Y-%m-%d"),
            "Revenue": Revenue,
            "Expenses": Expenses,
        }
    
        Records.append(Record)

        # Allow user to add another report
        Continue = input("Do you want to add another report? (Y/N): ").upper()
        if Continue == "N":
            break
    
    # Calculate totals
    TotRevenue = sum(record["Revenue"] for record in Records)
    TotExpenses = sum(record["Expenses"] for record in Records)
    # sum(record["Revenue"] for record in Records) loops over each record and adds the values together
    ProfLoss = TotRevenue - TotExpenses

    # Format values
    TotRevenueDsp = FV.FComma2(TotRevenue)
    TotExpensesDsp = FV.FComma2(TotExpenses)
    ProfLossDSP = FV.FComma2(ProfLoss)

    # Display the report
    print()
    print(f"HAB Taxi Services       Current Date: {CUR_DATE}")
    print(f"-" * 52)
    print(f"Start Date      End Date        Revenue     Expenses")
    print(f"-" * 52)
    for Record in Records:
        StartDate = Record["StartDate"]
        EndDate = Record["EndDate"]
        Revenue = Record["Revenue"]
        Expenses = Record["Expenses"]
        
        RevenueDSP = FV.FComma2(Revenue)
        ExpensesDSP = FV.FComma2(Expenses)

        print(f"{StartDate:<10s}     {EndDate:<10s}  {RevenueDSP:>12s} {ExpensesDSP:>12s}")
    print(f"-" * 52)
    print(f"Total Revenue:                  {TotRevenueDsp:>20s}")
    print(f"Total Expenses:                 {TotExpensesDsp:>20s}")
    print(f"Profit/Loss:                    {ProfLossDSP:>20s}")

    # Write values to file
    with open("RevenueReport.txt", "w") as file:
        file.write(f"Revenue Summary Report - {CUR_DATE}\n")
        file.write(f"Start Date:    {StartDateObj.strftime('%Y-%m-%d')}\n")
        file.write(f"End Date:      {EndDateObj.strftime('%Y-%m-%d')}\n")
        file.write(f"Total Revenue:  {TotRevenueDsp}\n")
        file.write(f"Total Expenses: {TotExpensesDsp}\n")
        file.write(f"Profit/Loss:    {ProfLossDSP}\n")

    print("Revenue summary written to 'RevenueReport.txt'")

# Kassaundra
def FinancialReport():
    # Open the data file.
    f = open("Defaults.dat", "r")

    # Initialize variables to store default values
    NextTransNum = 0
    TransID = 0
    EmpNum = 0
    HST = 0.0


    # Define data storage lists.
    TransNumLst = []
    TransDateLst = []
    DescLst = []
    SubtotalLst = []
    HSTAmtLst = []
    TotalLst = []

    # Open the data file.
    f = open("Defaults.dat", "r")

    # Process each line (record) in the file in a loop.
    for XRecord in f:

        # The following line reads the first record in the file and creates a list.
        XLst = XRecord.split(",")

        # Grab the values from the list and assign to variables.
        TransNum = int(XLst[0].strip())
        EmpNum = int(XLst[1].strip())
        MonthStandFee = float(XLst[2].strip())
        DayRentFee = float(XLst[3].strip())
        WeekRentFee = float(XLst[4].strip())
        HST = float(XLst[5].strip())

    # Check if today is the first day of the month for monthly stand fees
    today = date.today()
    if today.day == 1:
        with open("Revenue.dat", "a") as f:
            StandFeeTransNum = TransNum
            TransNum += 1

            StandFeeHSTAmt = MonthStandFee * HST
            StandFeeTotal = MonthStandFee + StandFeeHSTAmt

            f.write(
                f"{StandFeeTransNum}, {today}, Monthly Stand Fees, {EmpNum}, {MonthStandFee:.2f}, {StandFeeHSTAmt:.2f}, {StandFeeTotal:.2f}\n"
            )

    # Main program starts here.
    while True:
        # Gather user inputs for employee details and report dates.

        while True:
            print()
            EmpName = input("Enter the employee name:                                          ").title()
            if EmpName == "":
                print()
                print("   Data Entry Error - Employee Name cannot be blank.")
                print()
            else:
                break

        while True:
            StartDate = input("Enter the start date (YYYY-MM-DD):                                ")
            if StartDate == "":
                print()
                print("   Data Entry Error - Start date cannot be blank.")
                print()
            else:
                try:
                    StartDate = datetime.strptime(StartDate, "%Y-%m-%d").date()
                    if StartDate > date.today():
                        print()
                        print("   Data Entry Error - Start date cannot be in the future.")
                        print()
                    else:
                        break
                except ValueError:
                    print()
                    print("   Data Entry Error - Start date must be in YYYY-MM-DD format.")
                    print()

        while True:
            EndDate = input("Enter the end date (YYYY-MM-DD):                                  ")
            if EndDate == "":
                print()
                print("   Data Entry Error - End date cannot be blank.")
                print()
            else:
                try:
                    EndDate = datetime.strptime(EndDate, "%Y-%m-%d").date()
                    if EndDate < StartDate:
                        print()
                        print("   Data Entry Error - End date cannot be earlier than start date.")
                        print()
                    else:
                        break
                except ValueError:
                    print()
                    print("   Data Entry Error - End date must be in YYYY-MM-DD format.")
                    print()

        # Loop for transaction details
        while True:
            print()
            
            TransNumLst.append(TransNum)
            TransNum += 1

            # Transaction Date
            while True:
                TransDate = input("Enter the transaction date (YYYY-MM-DD):                          ")
                try:
                    TransDate = datetime.strptime(TransDate, "%Y-%m-%d").date()
                    if StartDate <= TransDate <= EndDate:
                        TransDateLst.append(TransDate)
                        break
                    else:
                        print()
                        print("   Data Entry Error - Transaction date must be on or between the start and end dates.")
                        print()
                except ValueError:
                    print()
                    print("   Data Entry Error - Please enter the date as YYYY-MM-DD.")
                    print()

            # Description
            while True:
                Desc = input("Enter a brief description of the transaction (max 25 characters): ")
                if Desc == "":
                    print()
                    print("   Data Entry Error - Description cannot be blank.")
                    print()
                elif len(Desc) > 25:
                    print()
                    print("   Data Entry Error - Description must be 25 characters or less.")
                    print()
                else:
                    DescLst.append(Desc)
                    break

            # Subtotal
            while True:
                Subtotal = input("Enter the transaction amount:                                     ")
                try:
                    Subtotal = float(Subtotal)
                    SubtotalLst.append(Subtotal)
                    break
                except ValueError:
                    print()
                    print("   Data Entry Error - Amount must be numeric.")
                    print()

            # Perform required calculations.
            HSTAmt = Subtotal * HST
            Total = Subtotal + HSTAmt
            HSTAmtLst.append(HSTAmt)
            TotalLst.append(Total)

            # Save the transaction details to FinancialReport.dat
            with open("FinancialReport.dat", "a") as f:
                f.write(
                    f"{TransNum}, {TransDate}, {Desc}, {Subtotal:.2f}, {HSTAmt:.2f}, {Total:.2f}\n"
                )

            # Ask if the user wants to input another transaction
            print()
            Continue = input("Would you like to input another transaction? (Y/N):               ").upper()
            if Continue != "Y":
                break
            elif Continue != "N" and Continue != "Y":
                print()
                print("   Data Entry Error - Please enter Y or N.")
                print()

        # Display results
        
        print()
        print(f"                    HAB Taxi Services - Driver Financial Listing Report")
        print()
        print(f"Start Date: {StartDate}                                   Employee Name: {EmpName:>25s}")
        print(f"End Date:   {EndDate}                                   Employee Number:                    {EmpNum:>4d}")
        print()
        print(f"Transaction ID   Transaction Date         Description              Subtotal       HST       Total")
        print(f"==================================================================================================")

        # Display all transactions
        for i in range(len(TransNumLst)):
            print(f"      {TransNumLst[i]:3d}           {TransDateLst[i]}     {DescLst[i]:<25s}      {FV.FDollar2(SubtotalLst[i]):>8s}    {FV.FDollar2(HSTAmtLst[i]):>8s}    {FV.FDollar2(TotalLst[i]):>8s}")
        
        print(f"==================================================================================================")
        print(f"                                                                              Subtotal: {FV.FDollar2(sum(SubtotalLst)):>10s}")
        print(f"                                                                              HST:      {FV.FDollar2(sum(HSTAmtLst)):>10s}")
        print(f"                                                                              Total:    {FV.FDollar2(sum(TotalLst)):>10s}")
        print()


        break

    # Any housekeeping duties at the end of the program

    # Save updated defaults to Defaults.dat
    f = open("Defaults.dat", "w")
    f.write(f"{TransNum}, {EmpNum}, {MonthStandFee}, {DayRentFee}, {WeekRentFee}, {HST}\n")
    f.close()

# Stephen
# List choices
while True:
    print()
    print(f"    HAB Taxi Services")
    print(f" Company Services System")
    print()

    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Quit")
    print()

    Choice = int(input("Enter choice (1-8): "))

    if Choice == 1:
        AddEmployee()
    elif Choice == 2:
        pass
    elif Choice == 3:
        pass
    elif Choice == 4:
        CarRent()
    elif Choice == 5:
        EmployeePayment()
    elif Choice == 6:
        RevenueTable()
    elif Choice == 7:
        FinancialReport()
    elif Choice == 8:
        print("Thank you for using the program. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice")

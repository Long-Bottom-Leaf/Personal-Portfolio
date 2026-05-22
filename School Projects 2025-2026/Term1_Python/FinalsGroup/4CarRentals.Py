# Define required libraries.
import datetime as DT
import FormatValues as FV
import os
from datetime import datetime, timedelta
import time

# Define program constants.

#Define program functions.

# Function to check if a car is occupied for the given rental period
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
today = DT.date.today()
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
                StartDate = DT.datetime.strptime(StartDate, "%Y-%m-%d").date()
                if StartDate > DT.date.today():
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
# Define required libraries.
import datetime as DT
import FormatValues as FV

# Define program constants.

#Define program functions.

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
        EndDate = input("Enter the end date (YYYY-MM-DD):                                  ")
        if EndDate == "":
            print()
            print("   Data Entry Error - End date cannot be blank.")
            print()
        else:
            try:
                EndDate = DT.datetime.strptime(EndDate, "%Y-%m-%d").date()
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
                TransDate = DT.datetime.strptime(TransDate, "%Y-%m-%d").date()
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
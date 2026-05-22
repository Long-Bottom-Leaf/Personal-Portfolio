# Description: Python Assignment 4 - The One Stop Insurance Company
# Author: Stephen Fennelly
# Dates: March 17, 2025 - March 23, 2025


# Define required libraries
import datetime
import Assignment4FormatValues as A4FV


# Define constants

CUR_DATE = datetime.datetime.now()

POLICY_NUMB = 1944               # Policy Number

BASE_PREM_RATE = 869.00         # Basic Premium Rate
DISCNT_ADD_CAR = 0.75           # 25% Discount for additional car

EXT_LIABL_RATE = 130.00         # Extra Liability Rate
GLASS_COVRG_RATE = 86.00        # Glass Coverage Rate

LOAN_CAR_RATE = 58.00           # Loaner Car Rate
HST_RATE = 0.15                 # HST Rate

PROCESS_FEE = 39.99             # Monthly Payments Processing Fee

# Define program functions

def InsurPremium(NumbCars, BASE_PREM_RATE, DISCNT_ADD_CAR):
    if NumbCars <= 0:
        raise ValueError("Number of cars must be at least 1.")

    CarPrem = BASE_PREM_RATE                        # First car at full price
    for i in range(1, NumbCars):  
        CarPrem += BASE_PREM_RATE * DISCNT_ADD_CAR  # Discount applies to extra cars

    return CarPrem

def LiableLoan(NumbCars, ExtraLiabl, GlassCoverg, LoanCar, EXT_LIABL_RATE, GLASS_COVRG_RATE, LOAN_CAR_RATE):
    ExtraLiablCost = (EXT_LIABL_RATE * NumbCars) if ExtraLiabl == "Y" else 0
    GlassCovergCost = (GLASS_COVRG_RATE * NumbCars) if GlassCoverg == "Y" else 0
    LoanCarCost = (LOAN_CAR_RATE * NumbCars) if LoanCar == "Y" else 0

            # Cap extra liability at 1 million
    if ExtraLiablCost > 1000000:
        ExtraLiablCost = 1000000

    TotalExtraCost = ExtraLiablCost + GlassCovergCost + LoanCarCost
    return ExtraLiablCost, GlassCovergCost, LoanCarCost, TotalExtraCost

def GetPayDue(FirstPayDate):
    # Determine dates
    Pay20Date = FirstPayDate + datetime.timedelta(days=20)
    PurYear = FirstPayDate.year
    PurMonth = FirstPayDate.month
    PurDay = FirstPayDate.day
 
    PayYear = PurYear
    PayMonth = PurMonth + 1
    if PayMonth == 13:
        PayMonth -= 12
        PayYear += 1
    PayDay = 1
    PayFirst = datetime.datetime(PayYear, PayMonth, PayDay)
 
    if Pay20Date > PayFirst:
        PayDate = Pay20Date
    else:
        PayDate = PayFirst
 
    return PayDate

# Main program starts here
while True:

    # Gather user inputs

        # Validation lists
    AllowedUpperCharNum = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    AllowedUpperChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    AllowedNum = set("0123456789-")
    ProvSet = set(["ON", "QC", "BC", "AB", "MB", "NS", "NB", "NL", "PE", "SK"])

        # Customer details
    CustName = input("Enter the customer's full name: ").title()
    Addrs = input("Enter the customer's address: ")
    City = input("Enter the customer's city: ").title()

    while True:
        Prov = input("Enter the customer's province: ").upper()
        if Prov == "":
            print()
            print("User Entry Error - Province cannot be blank.")
            print()
        elif Prov not in ProvSet:
            print()
            print("User Entry Error - Province must be entered correctly.")
            print()
        elif len(Prov) != 2:
            print()
            print("User Entry Error - Province must be 2 characters")
            print()
        else:
            break

    while True:
        PostalCode = input("Enter the customer's postal code (X0X0X0): ").upper()
        if PostalCode == "":
            print()
            print("User Entry Error - Postal code cannot be blank.")
            print()
        elif not set(PostalCode).issubset(AllowedUpperCharNum):
            print()
            print("User Entry Error - Postal code must be entered correctly.")
            print()
        elif len(PostalCode) != 6 or not PostalCode[0].isalpha() or not PostalCode[1].isdigit() or not PostalCode[2].isalpha() or not PostalCode[3].isdigit() or not PostalCode[4].isalpha() or not PostalCode[5].isdigit():
            print()
            print("User Entry Error - Postal code must follow the format X0X0X0.")
            print()
        else:
            break
    
    while True:
        Phone = input("Enter the customer's phone number (XXX-XXX-XXXX): ")
        if Phone == "":
            print()
            print("User Entry Error - Phone number cannot be blank.")
            print()
        elif not set(Phone).issubset(AllowedNum):
            print()
            print("User Entry Error - Phone number must be entered correctly.")
            print()
        else:
            break

        # Number cars
    NumbCars = int(input("Enter the number of cars being insured: "))
    
        # Extra liability/glass/loaner
    ExtraLiabl = input("Would you like to purchase extra liability coverage? (Y/N): ").upper()    
    GlassCoverg = input("Does the customer want glass coverage? (Y/N): ").upper()
    LoanCar = input("Does the customer want loaner car coverage? (Y/N): ").upper()

        # Payment options
    PayOptLst = ["Full", "Monthly", "Downpay"]
    while True:
        PayOpt = input("Would the customer like to pay in full (enter: Full), pay monthly (enter: Monthly), or place a down payment (enter: Downpay) : ").title()

        if PayOpt not in PayOptLst:
            print("User Entry Error - Payment option is invalid.")
        elif PayOpt == "Downpay":
            while True:
                try:
                    DownPay = float(input("Enter the down payment amount: "))
                    if DownPay <= 0:
                        print()
                        print("Error: Down payment cannot be 0.")
                        print()
                    else:
                        break
                except ValueError:
                    print()
                    print("Error: Please enter a valid numeric down payment amount.")
                    print()
            break
        else:
            break

    PayMethLst = ["Cash", "Debit", "Visa", "Mastercard"]
    while True:
        PayMethod = input("Enter the payment method (Cash, Debit, Visa, Mastercard): ").title()
 
        if PayMethod not in PayMethLst:
            print()
            print("User Entry Error - Payment method is invalid.")
            print()
        else:
            break

    # Claim Details

        # Store 3 previous claims
    Claims = [
        {"Claim Number": 1, "Date": "2024-11-05", "Amount": 2498.38},
        {"Claim Number": 2, "Date": "2024-12-10", "Amount": 999.35},
        {"Claim Number": 3, "Date": "2025-01-15", "Amount": 1200.50}
    ]

        # Set the starting claim number to continue from last claim
    ClaimNumb = len(Claims) + 1

        # Loop to input multiple claim amounts
    while True:
        AnoClaim = input("Do you want to enter another claim? (Y/N): ").upper()
        if AnoClaim != "Y":
            break

        ClaimDate = input("Enter the claim date (YYYY-MM-DD): ")
        ClaimAmt = float(input("Enter the claim amount: "))

        # Store the claim details
        ClaimDetails = {
            "Claim Number": ClaimNumb,
            "Date": ClaimDate,
            "Amount": ClaimAmt
        }

        Claims.append(ClaimDetails)

        # Increment claim number for the next claim
        ClaimNumb += 1

    # Perfrom required calculations

        # Had a lot of trouble with this calculation, I'll admit I had to get chatGPT to help cause every day the code would just.. stop working
    CarPrem = InsurPremium(NumbCars, BASE_PREM_RATE, DISCNT_ADD_CAR)        # Initializing CarPrem

    ExtraLiablCost, GlassCovergCost, LoanCarCost, TotalExtraCost = LiableLoan(
    NumbCars, ExtraLiabl, GlassCoverg, LoanCar, EXT_LIABL_RATE, GLASS_COVRG_RATE, LOAN_CAR_RATE)

    TotInsurance = CarPrem + TotalExtraCost
    
    HST = TotInsurance * HST_RATE
    TotCost = TotInsurance + HST

        # Calculate total payment
    if PayOpt == "Downpay":
        InsurPay = TotCost - DownPay
    else:
        InsurPay = TotCost

    if PayOpt == "Monthly":
        MonthlyPay = (TotCost / 8) + PROCESS_FEE
    elif PayOpt == "Downpay":
        MonthlyPay = ((TotCost - DownPay) / 8) + PROCESS_FEE
    else:
        MonthlyPay = 0

    InvoiceDate = CUR_DATE
    FirstPayDate = GetPayDue(InvoiceDate)

        # Formating for prints
    InvoiceDateDsp = InvoiceDate.strftime("%Y-%m-%d")
    FirstPayDateDsp = FirstPayDate.strftime("%Y-%m-%d")
    
    Phone = "".join(filter(str.isdigit, Phone))         # Removes all non-numeric characters
    PhoneDsp = f"{Phone[:3]}-{Phone[3:6]}-{Phone[6:]}"

        # Append additional claims
    if AnoClaim == "Y":
        NewClaimDetails = {
            "Claim Number": ClaimNumb,
            "Date": ClaimDate,
            "Amount": ClaimAmt
        }
        Claims.append(NewClaimDetails)  # Append the new claim

        # Append inputs to claim list
    InitialClaim = {
        "Claim Number": ClaimNumb,
        "Date": InvoiceDateDsp,
        "Amount": TotCost
    }
    Claims.append(InitialClaim)
    
    # Display results

    # Header

    print()
    print(f"                   ONE STOP INSURANCE COMPANY")
    print(f"-------------------------------------------------------------")
    print(f"Invoice for:                              Policy Number: {POLICY_NUMB}")
    print(f"Customer Name: {CustName:<20s}  Invoice Date: {InvoiceDateDsp:<10s}")
    print(f"Address: {Addrs}")
    print(f"         {City:<20s}      Phone Number: {PhoneDsp}")
    print(f"         {Prov:<2s}, {PostalCode:<6s}")
    print(f"-------------------------------------------------------------")

    print("Policy Information:")
    print(f"Number of Cars Insured: {NumbCars:<3d}            Loaner Car Coverage: {LoanCar}")
    print(f"Extra Liability Coverage: {ExtraLiabl}                 Glass Coverage: {GlassCoverg}")
    print(f"Payment Option: {PayOpt}")
    if PayOpt == "Downpay":
        print(f"Down Payment: {A4FV.FDollar2(DownPay)}")
    print(f"-------------------------------------------------------------")
    print(f"Payment Information:")
    print(f"Total Insurance Premium: {A4FV.FDollar2(TotInsurance)}")
    print(f"HST (15%): {A4FV.FDollar2(HST)}                 Payment Method: {PayMethod:>10s}")
    print(f"Total Cost: {A4FV.FDollar2(TotCost)}                 Payment Due: {FirstPayDateDsp:>10s}")
    if PayOpt in ["Monthly", "Downpay"]:
        print(f"Monthly Payment: {A4FV.FDollar2(MonthlyPay)} for 8 months")
    else:
        print(f"Payment in Full: {A4FV.FDollar2(TotCost)}")
    print(f"-------------------------------------------------------------")
    print(f"  Claim Number #          Claim Date            Total Claim")
    for claim in Claims:
        print(f"       {claim['Claim Number']:<15d}    {claim['Date']:<10s}   {A4FV.FDollar2(claim['Amount']):>20s}")
    print(f"-------------------------------------------------------------")

    # Write the values to a data file for starage

    # Any housekeeping duties at the end of the program
    Continue = input("Do you want to continue (Y/N): ").upper()
    if Continue == "N":
        print("Have a great day!")
        break
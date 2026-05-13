# Description: Python Assignment 3
# Author: Stephen Fennelly
# Dates: 2025-02-12 - 2025-02-14


# Define required libraries
import datetime

# Define constants

InvDate = datetime.datetime.now()                       # current date for invoice
FirstPayDate = InvDate + datetime.timedelta(days=30)    # first payment date

FINANCING_RATE = 39.99                                  # rate per year
MAX_SELL_PRICE = 50000.00                               # max sell price

HST_RATE = 0.15                                         # 15% HST tax

LICENSE_FEE_THRESHOLD = 15000.00                        # threshold to trigger high license fee
HIGH_LICENSE_FEE = 165.00
LOW_LICENSE_FEE = 75.00

TRANSFER_FEE_RATE = 0.01                                # 1% transfer fee

LUXURY_TAX_THRESHOLD = 20000.00                         # threshold to trigger luxury tax
LUXURY_TAX_RATE = 0.016                                 # 1.6% luxury tax

# Define program functions

financing_options = []

# Main program starts here

while True:

    # Allowed character sets

    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'")
    AllowedUpperChar = set ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    AllowedNum = set("0123456789") 
    AllowedUpperCharNum = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    AllowedPriceVari = set("0123456789 $,.")
    AllowedCarVari = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 abcdefghijklmnopqrstuvwxyz.-'")

    # User inputs
    
    exit_program = False  # Initialize exit_program

    while not exit_program:

        CustFirstName = input("Enter your first name: ").title()
        if CustFirstName == "":
            print()
            print("     Error - First name cannot be blank.")
            print()
        elif not set(CustFirstName).issubset(allowed_char):
            print()
            print("     Error - First name contains invalid characters.")
            print()
        elif CustFirstName.upper() == "END":
            exit_program = True
            break
        else:
            break

    if exit_program:                    # exiting program
        break

    while True:
        CustLastName = input("Enter your last name: ").title()
        if CustLastName == "":
            print()
            print("     Error - Customer name cannot be blank.")
            print()
        elif set(CustLastName).issubset(allowed_char) == False:
            print()
            print("     Error - Customer name contains invalid characters.")
            print()
        else:
            break

    while True:
        PhnNumb = input("Enter your phone number (XXXXXXXXXX): ")
        if PhnNumb == "":
            print()
            print("     Error - Customer Phone Number cannot be blank.")
            print()
        elif len(PhnNumb) != 10:
            print()
            print("     Error - Phone number must be 10 digits.")
            print()
        elif set(PhnNumb).issubset(AllowedNum) == False:
            print()
            print("     Error - Customer name contains invalid characters.")
            print()
        else:
            break
    
    # I was looking up why the code wasn't performing the len check when I happened to find this way to format the plate numb and it seems to have fixed the len check issue.
    while True:
        PlateNumb = input("Enter the car's plate number (AAA999): ").upper()
        if PlateNumb == "":
            print()
            print("     Error - Plate number cannot be blank.")
            print()
        elif len(PlateNumb) != 6:
            print()
            print("     Error - Plate Number must be 6 characters.")
            print()
        elif not (PlateNumb[:3].isalpha() and PlateNumb[3:].isdigit()):
            print()
            print("     Error - Plate Number must be in the format AAA999.")
            print()       
        else:
            break

    while True:
        # car details
        CarMake = input("Enter the manufacturer of the vehicle: ").title()
        if CarMake == "":
            print()
            print("     Error - Vehicle manufacturer cannot be blank.")
            print()
        elif set(CarMake).issubset(allowed_char) == False:
            print()
            print("     Error - Vehicle manufacturer contains invalid characters.")
            print()
        else:
            break

    while True:
        CarModel = input("Enter the model of the Vehicle: ").title()
        if CarModel == "":
            print()
            print("     Error - Vehicle model cannot be blank.")
            print()
        elif set(CarModel).issubset(AllowedCarVari) == False:
            print()
            print("     Error - Vehicle model contains invalid characters.")
            print()
        else:
            break
    
    while True:
        CarYear = input("Enter the year of the car: ")
        if CarYear == "":
            print()
            print("     Error - Vehicle year cannot be blank.")
            print()
        elif set(CarYear).issubset(AllowedNum) == False:
            print()
            print("     Error - Vehicle year contains invalid characters.")
            print()
        elif len(CarYear) != 4:
            print()
            print("     Error - Year must be 4 characters.")
            print()
        else:
            break
    

    # Sell price checks
    while True:
        SellPrice = input("Enter the sell price of the car (Cannot exceed $50,000): ").strip()
        # when trying to get these checks to work which took AN HOUR I discovered .strip() function which removes extra blank spaces to make it easier for conversion/checks later

        if SellPrice == "":
            print()
            print("     Error - Sell Price cannot be blank.")
            print()
            continue   
        if set(SellPrice).issubset(AllowedPriceVari) == False:
            print()
            print("     Error - Price contains invalid characters.")
            print()
            continue
        
        # Removing extra variables for conversion
        SellPrice = SellPrice.replace(',', '').replace('$', '')       
        try:
            # Converting to float to handle checks
            SellPrice = float(SellPrice)

            if SellPrice > MAX_SELL_PRICE:
                print()
                print("     Error - Price exceeding $50,000 entered.")
                print()
                continue
            if SellPrice <= 0:
                print()
                print("     Error - Price must be greater than 0.")
                print()
                continue
            break       
        except ValueError:
            print()
            print("     Error - Price contains invalid numerical format.")
            print()
        
    while True:
        TradIn = input("Enter the trade-in price (Cannot exceed sell price, $XX,XXXX): ").strip()

        if TradIn == "":
            print()
            print("     Error - Sell Price cannot be blank.")
            print()
            continue   
        if set(TradIn).issubset(AllowedPriceVari) == False:
            print()
            print("     Error - Price contains invalid characters.")
            print()
            continue
        
        # Removing extra variables for conversion
        TradIn = TradIn.replace(',', '').replace('$', '')       
        try:
            # Convert to float to handle checks
            TradIn = float(TradIn)

            if TradIn >= SellPrice:
                print()
                print("     Error - Trade-in price cannot exceed the Sell price.")
                print()
                continue
            if TradIn <= 0:
                print()
                print("     Error - Price must be greater than 0.")
                print()
                continue
            break       
        except ValueError:
            print()
            print("     Error - Price contains invalid numerical format.")
            print()
        
    while True:
        SalePerName = input("Enter the salespersons name: ").title()
        if SalePerName == "":
            print()
            print("     Error - First name cannot be blank.")
            print()
        elif set(SalePerName).issubset(allowed_char) == False:
            print()
            print("     Error - First name contains invalid characters.")
            print()
        else:
            break


    # Perfrom required calculations
    PriceAfterTrade = SellPrice - TradIn

    # License Fee based on the selling price
    if SellPrice <= LICENSE_FEE_THRESHOLD:
        LicenseFee = LOW_LICENSE_FEE
    else:
        LicenseFee = HIGH_LICENSE_FEE

    TransFee = SellPrice * TRANSFER_FEE_RATE

    if SellPrice > LUXURY_TAX_THRESHOLD:
        TransFee += SellPrice * LUXURY_TAX_RATE              # luxury tax if applicable, += will calculate the SellPrice * RATE and add it to the TransFee
    
    Subtotal = PriceAfterTrade + LicenseFee + TransFee

    HST = Subtotal * HST_RATE
    TotalSalesPrice = Subtotal + HST
    
    # calculating payment table
    for Years in range(1, 5):
        Months = Years * 12
        FinancingFee = Years * FINANCING_RATE
        TotPrice = SellPrice + FinancingFee
        MonthPay = TotPrice / Months

        FinancingFeeDsp = "${:,.2f}".format(FinancingFee)
        MonthPayDsp = "${:,.2f}".format(MonthPay)
        TotPriceDsp = "${:,.2f}".format(TotPrice)

        financing_options.append({                              # I couldn't remember how to format for a table and while searching online I learned about the .append() which alters
        'Years': Years,                                         # a list to add an item at the end, and since it's wrapped in an if with a range of 1-5 it creates a list for 4 years
        'MonthPayments': Months,
        'FinanceFee': FinancingFeeDsp,
        'TotPrice': TotPriceDsp,
        'MontFee': MonthPayDsp
        })
    
    # Formating

    # formating times
    InvDate1Dsp = InvDate.strftime("%B %d, %Y")
    InvDate2Dsp = InvDate.strftime("%d-%B-%y")
    FirstPayDateDsp = FirstPayDate.strftime("%d-%B-%y")

    # formating reciept number and name
    RecpNum = CustFirstName[0] + CustLastName[0] + "-" + PlateNumb[3:6] + "-" + PhnNumb[6:10]
    CustNam = CustFirstName[0] + "." + " " + CustLastName
    PhnNumbDsp = "(" + PhnNumb[0:3] + ")" + " " + PhnNumb[3:6] + "-" + PhnNumb[6:10]

    # formating car display
    CarDetails = CarYear + " " + CarMake + " " + CarModel

    # formating price details for invoice
    SellPriceDsp = "${:,.2f}".format(SellPrice)
    PriceAfterTradeDsp = "${:,.2f}".format(PriceAfterTrade)

    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    TransFeeDsp = "${:,.2f}".format(TransFee)

    SubtotalDsp = "${:,.2f}".format(Subtotal)
    HSTDsp = "${:,.2f}".format(HST)

    TotalSalesPriceDsp = "${:,.2f}".format(TotalSalesPrice)
    
    # Display results
    print()
    print(f"Honest Harry Car Sales                  Invoice Date: {InvDate1Dsp:<20s}")
    print(f"Used Car Sale and Receipt               Recipt No:          {RecpNum:<20s}")
    print()
    print(f"                                    Sale Price:              {SellPriceDsp:>10}")
    print(f"Sold to:                            Trade Allowance: ")
    print(f"                                    -----------------------------------")
    print(f"    {CustNam:<20s}            Price after Trade:       {PriceAfterTradeDsp:>10}")
    print(f"    {PhnNumbDsp:<14s}                  Liscence Fee:            {LicenseFeeDsp:>10}")
    print(f"                                    Transfer Fee:            {TransFeeDsp:>10}")
    print(f"                                    -----------------------------------")                           # put in calculations and fix alignment again
    print(f"Car Details:                        Subtotal:                {SubtotalDsp:>10}")
    print(f"                                    HST:                     {HSTDsp:>10}")
    print(f"    {CarDetails:<30s}  -----------------------------------")
    print(f"                                    Total sales price: ")
    print()
    print(f"-----------------------------------------------------------------------")
    print()
    print(f"                           Financing       Total         Monthly")
    print(f"   # Years   # Payments      Fee           Price         Payment")
    print(f"----------------------------------------------------------------")
    for option in financing_options:
        print(f"      {option['Years']:<8}  {option['MonthPayments']:<10}  {option['FinanceFee']:>7}     {option['TotPrice']:>10}     {option['MontFee']:>10}")
    print(f"----------------------------------------------------------------")
    print(f"Invoice Date: {InvDate2Dsp:<20s}   First Payment Date: {FirstPayDateDsp:<20s}")
    print(f"-----------------------------------------------------------------------")
    print(f"                 Best used cars for the best prices!")
    
    print()
    print(f"If you would like to end the program, type END when prompted to enter a first name.")

    # Write the values to a data file for starage



    # Any housekeeping duties at the end of the program

print()
print(f"Have a great day!")
print()
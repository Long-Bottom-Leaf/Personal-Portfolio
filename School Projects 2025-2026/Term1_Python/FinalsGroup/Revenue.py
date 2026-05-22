def RevenueTable():
    # Function for Revenue Table

    import datetime
    import FormatValues as FV

    # Constants
    CUR_DATE = datetime.datetime.now()
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
                    StartDateObj = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
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
                    EndDateObj = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
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
    print(f"HAB Taxi Services           Current Date: {CUR_DATE.strftime('%Y-%m-%d')}")
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
    
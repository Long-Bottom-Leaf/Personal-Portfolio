# Description: Determin total bill for Car Rental from Edsel
# Author: Stephen Fennelly
# Date: January 11, 2025

# Define program constants
Day_Rate = 75.00 # 75 dollars per day
Mlg_Rate = .26 # 26 cents per km
Insur_Rate = 19.00 # 19 dollars per day
Rnt_Discnt_Rate = .1 # 10% discount rate on rental
Mlg_Discnt_Rate = .25 # 25% discount rate on mileage
Hst_Rate = .15 # 15% current rate to calculate HST

# Gather User Input
CustName = input("Enter the customer name: ")
CustPhone = input("Enter the customer phone number: ")
NumbDays = int(input("Enter the number of days the car was rented: "))
if NumbDays <= 0:
    print("The number of days must be greater than 0. Please re-enter.")
    NumbDays = int(input("Enter the number of days the car was rented: "))

print()

OdomRent = int(input("Enter the odometer reading at the start of the rental: "))
OdomRetrn = int(input("Enter the odometer reading at the end of the rental: "))
if OdomRetrn <= OdomRent:
    print("The end of rental odometer reading must be greater than the starting odometer reading.")
    print("Please re-enter the odometer readings.")
    OdomRent = int(input("Enter the odometer reading at the start of the rental: "))
    OdomRetrn = int(input("Enter the odometer reading at the end of the rental: "))

print()

# Calculate Costs
KmTrvl = OdomRetrn - OdomRent
print()
RentCost = NumbDays * Day_Rate
MlgCost = KmTrvl * Mlg_Rate
Insur = NumbDays * Insur_Rate
print()
DiscntRnt = RentCost * Rnt_Discnt_Rate
DiscntMlg = MlgCost * Mlg_Discnt_Rate
TotDiscnt = DiscntRnt + DiscntMlg
print()
TotRent = RentCost + MlgCost + Insur - TotDiscnt
print()
HST = RentCost * Hst_Rate
InvoTot = TotRent + HST

print()

# Display Results
print("Customer Name:                               ", CustName)
print("Customer Phone Number:                       ", CustPhone)
print("Number of Days Rented:                       ", NumbDays)
print("Odometer Reading at Start of Rental:         ", OdomRent)
print("Odometer Reading at End of Rental:           ", OdomRetrn)
print()
print("Kilometers Traveled:                         ", KmTrvl)
print("Rental Cost:                                 ", RentCost)
print("Mileage Cost:                                ", MlgCost)
print()
print("Insurance Cost:                              ", Insur)
print("Total Discount:                              ", TotDiscnt)
print()
print("Total Rental Cost:                           ", TotRent)
print()
print("HST:                                         ", HST)
print("Invoice Total:                               ", InvoTot)
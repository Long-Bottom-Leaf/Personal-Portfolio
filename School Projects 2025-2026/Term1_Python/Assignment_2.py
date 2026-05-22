# Description: Python Assignment 2
# Author: Stephen Fennelly
# Dates: 2025-01-28 - 2025-2-01

# Constants

EVN_SITE_RATE = 80.00           # Even numbered sites rate
ODD_SITE_RATE = 120.00          # Odd numbered sites rate

ALT_MEM_RATE = 5.00             # Additional member rate

SITE_CLN_RATE = 50.00           # Weekly cleaning monthly charge
VID_RATE = 35.00                # Video surveillance charge

HST_RATE = .15

STN_DUE_RATE = 75.00            # Standard dues
EXEC_DUE_RATE = 150.00          # Executive dues

PROSS_RATE = 59.99 / 12         # Processing fee
CNCL_RATE = .60                 # Cancellation fee

# User inputs

Date = input("Enter current date (YYYY-MM-DD): ")
SitNum = int(input("Enter the site number (1-100): "))
MemName = input("Enter the member name: ")

StrAdd = input("Enter the member streen address: ")
City = input("Enter the city name: ")
Prov = input("Enter the province: ").upper()
Post = input("Enter the postal code: ").upper()

PhonNumb = input("Enter the member phone number (XXXXXXXXX): ")
CellNumb = input("Enter the member cell number (XXXXXXXXX): ").upper()

MembType = input("Enter the member type (S for Standard, E for Executive): ").upper()

AltMem = int(input("Enter the number of alternate members: "))
SiteCln = (input("Would the member like weekly site cleaning? (Y, N): ")).upper()
VidSurv = (input("Would the member like video surveillance? (Y, N): ")).upper()

# Define program functions

# Member type
if MembType == "S":
	MembTypeDsp = "Standard"
else:
	MembTypeDsp = "Executive"

# Site cost caclulation
if SitNum % 2 == 0:
    SitCost = EVN_SITE_RATE
else:
	SitCost = ODD_SITE_RATE

# Site cleaning caclulation         
if SiteCln == "Y":
	SitClnChrg = SITE_CLN_RATE
else:
	SitClnChrg = 0

# Video surveillance caclulation
if VidSurv == "Y":
	VidSurvChrg = VID_RATE
else:
	VidSurvChrg = 0

# Standard/Executive dues
if MembType == "S":
	MontDue = STN_DUE_RATE
else:
	MontDue = EXEC_DUE_RATE
	

# Perform required calculations

AltMemCost = AltMem * ALT_MEM_RATE

SitChrg = SitCost + AltMemCost

ExtChrg = SitClnChrg + VidSurvChrg

SubTot = SitChrg + ExtChrg

HST = HST_RATE * SubTot

TotMonChrg = SubTot + HST

TotMonFee = TotMonChrg + MontDue

TotYearFee = (TotMonFee * 12)

TotMonPay = (TotYearFee + PROSS_RATE) / 12

CnclFee = (SitChrg * 12) * CNCL_RATE

# Display formating -- I just tried sorting it this way and it was easy for me to make adjustments

SitChrgDsp = "${:,.2f}".format(SitChrg)
ExtChrgDsp = "${:,.2f}".format(ExtChrg)
SubTotDsp = "${:,.2f}".format(SubTot)
HSTDsp = "${:,.2f}".format(HST)
TotMonChrgDsp = "${:,.2f}".format(TotMonChrg)
TotYearFeeDsp = "${:,.2f}".format(TotYearFee)
TotMonFeeDsp = "${:,.2f}".format(TotMonFee)
MontDueDsp = "${:,.2f}".format(MontDue)
TotMonPayDsp = "${:,.2f}".format(TotMonPay)
CnclFeeDsp = "${:,.2f}".format(CnclFee)

# Display results

print()
print(f"     St. John's Marina & Yacht Club")
print(f"          Yearly Member Receipt")
print()
print('─' * 38)									# I know we were supposed to use just hyphens but I found a way online to make the solid line
print()
print(f"Client Name and Address: ")
print()
print(f"{MemName:<24s}")
print(f"{StrAdd:<24s}")
print(f"{City:<15s},             {Prov:<2s} {Post:<6s}")
print()
print(f"Phone: {PhonNumb:<10s} (H)")
print(f"       {CellNumb:<10s} (C)")
print()
print(f"Site #: {SitNum:<3d}    Member type: {MembTypeDsp:<9s}")
print()
print(f"Alternate members:		    {AltMem:>2d}")
print(f"Weekly site cleaning:              {SiteCln:>3s}")
print(f"Video surveillance:                {VidSurv:>3s}")
print()
print(f"Site charges:               {SitChrgDsp:>10s}")
print(f"Extra charges:              {ExtChrgDsp:>10s}")
print(f"                             ---------")
print(f"Subtotal:                   {SubTotDsp:>10s}")
print(f"Sales tax (HST):            {HSTDsp:>10s}")
print(f"                             ---------")
print(f"Total monthly charges:      {TotMonChrgDsp:>10s}")
print(f"Total monthly dues:         {MontDueDsp:>10s}")
print(f"                             ---------")
print(f"Total monthly fees:         {TotMonFeeDsp:>10s}")
print(f"Total yearly fees:          {TotYearFeeDsp:>10s}")
print()
print(f"Monthly payment:            {TotMonPayDsp:>10s}")
print()
print('─' * 38)
print()
print(f"Issued: {Date:<10s}")
print(f"HST Reg No: 549-33-589-4720-9885")
print()
print(f"Cancellation fee:           {CnclFeeDsp:>10s}")
print()


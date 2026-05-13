// Description: Web Assignment 4
// Author: SD-14
// DatesL: March 24, 2025 - March 27

// Set up the program constants

const EVEN_SITE_RATE = 80.00
const ODD_SITE_RATE = 120.00
const ALT_MEMB_RATE = 5.00
const HST_RATE = 0.15

const STAND_MEM_RATE = 75.00
const EXEC_MEM_RATE = 150.00

const SITE_CLEAN_RATE = 50.00
const VID_SURV_RATE = 35.00

const STAND_DUES_RATE = 75.00
const EXEC_DUES_RATE = 150.00

const PROCESS_FEE = 59.99
const CANCL_FEE = 0.60

// Constants used to format displayed variables
const cur2Format = new Intl.NumberFormat("en-CA",
    {
        style: "currency",
        currency: "CAD",
        minimumFractionDigits: "2",
        maximumFractionDigits: "2",
    })

const num0Format = new Intl.NumberFormat("en-CA",
    {
        style: "decimal",
        minimumFractionDigits: "0",
        maximumFractionDigits: "0",
    }
)

// Gather inputs

let CurrDate = prompt("Enter the current date (YYYY-MM-DD): ");
let SiteNumb = prompt("Enter the site number (1-100): ");
SiteNumb = parseInt(SiteNumb);

let MembName = prompt("Enter the member's name: ");
let StreetAddr = prompt("Enter the street address: ");
let City = prompt("Enter the city: ");
let Province = prompt("Enter the province: ");
let PostalCode = prompt("Enter the postal code: ");
let HomePhone = prompt("Enter the home phone number: ");
let CellPhone = prompt("Enter the cell phone number: ");

let MembType = prompt("Enter membership type (S for Standard, E for Executive): ").toUpperCase();
let NumbAltMemb = prompt("Enter the number of alternate members: ");
NumbAltMemb = parseInt(NumbAltMemb);

let SiteClean = prompt("Weekly site cleaning? (Y/N): ").toUpperCase();
let VidSurv = prompt("Video surveillance? (Y/N): ").toUpperCase();

// Perform calculations

    // Site Number Rate
let SiteFee;
    if (SiteNumb % 2 === 0)
    {
        SiteFee = EVEN_SITE_RATE
    } else
    {
        SiteFee = ODD_SITE_RATE
    }

let AltMembCost = NumbAltMemb * ALT_MEMB_RATE;
let SiteCharge = SiteFee + AltMembCost;

    // Site Clean
let SiteCleanCharge;
    if (SiteClean === "Y")
    {
        SiteCleanCharge = SITE_CLEAN_RATE;
    } else
    {
        SiteCleanCharge = 0;
    }
        
if (SiteClean === 'Y')
{
    SitePrint = "Yes";
} else
{
    SitePrint = "No";
}
        
    // Vid Surveillance
if (VidSurv === "Y")
{
    VidCharge = VID_SURV_RATE;
} else
{
    VidCharge = 0;
}
        
if (VidSurv === 'Y')
{
    VidPrint = "Yes";
} else
{
    VidPrint = "No";
}

    // Extra Charge Total
let ExtraCharge = SiteCleanCharge + VidCharge;

    // Subtotal and HST and Monthly Charges
let SubTot = ExtraCharge + SiteCharge;
let HST = SubTot * HST_RATE;
let TotMonthCharge = SubTot + HST;

    // Member Type Rate
if (MembType === "E")
{
    MembDues = EXEC_DUES_RATE;
} else
{
    MembDues = STAND_DUES_RATE;
}

if (MembType === 'E')
{
    MembPrint = "Executive";
} else
{
    MembPrint = "Standard";
}

    // Monthly Fees
let TotMonthFee = TotMonthCharge + MembDues;

    // Yearly Fees
let TotYearFee = TotMonthFee * 12;

    // Monthly Payment Calculation
let MonthlyPay = (TotYearFee + PROCESS_FEE) / 12;

    // Cancellation Fee
let CancelFee = (SiteCharge * 12) * CANCL_FEE;

// Print out receipt for customer

document.writeln("<table class='receipttable'>");
document.writeln("<tr>"); 
document.writeln("<td class='mainhead' colspan='2'>St. John's Marina & Yacht Club<br />Yearly Member Receipt<br /><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Client Name and Address:<br /><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2'>" + MembName + "<br />" + StreetAddr + "<br />" + City + ", " + Province + " " + PostalCode + "<br /><br />Phone: " + HomePhone + "<br />Cell: &nbsp;&nbsp;&nbsp;&nbsp;" + CellPhone + "<br /><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><div style='flex: 1;'><span>Site #:</span><span class='righttext'>" + SiteNumb + "</span></div><div style='flex: 1; text-align: right;'><span>Member Type:</span><span class='righttext'>" + MembPrint + "</span></div></div><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><span>Alternate Members:</span><span class='righttext'>" + NumbAltMemb + "</span></div><br /><div class='flex-container'><span>Weekly Site Cleaning:</span><span class='righttext'>" + SitePrint + "</span></div><br /><div class='flex-container'><span>Video Surveillance:</span><span class='righttext'>" + VidPrint + "</span></div><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><span>Site Charges:</span><span class='righttext'>" + cur2Format.format(SiteCharge) + "</span></div><br /><div class='flex-container'><span>Extra Charges:</span><span class='righttext'>" + cur2Format.format(ExtraCharge) + "</span></div><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><span>SubTotal:</span><span class='righttext'>" + cur2Format.format(SubTot) + "</span></div><br /><div class='flex-container'><span>HST:</span><span class='righttext'>" + cur2Format.format(HST) + "</span></div><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><span>Total Monthly Charges:</span><span class='righttext'>" + cur2Format.format(TotMonthCharge) + "</span></div><br /><div class='flex-container'><span>Monthly Dues:</span><span class='righttext'>" + cur2Format.format(MembDues) + "</span></div><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><span>Total Monthly Fees:</span><span class='righttext'>" + cur2Format.format(TotMonthFee) + "</span></div><br /><div class='flex-container'><span>Total Yearly Fees:</span><span class='righttext'>" + cur2Format.format(TotYearFee) + "</span></div><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><span>Monthly Payment:</span><span class='righttext'>" + cur2Format.format(MonthlyPay) + "</span></div><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><div class='flex-container'><span>Issued:</span><span class='righttext'>" + CurrDate + "</span></div><br /><div class='flex-container'><span>HST Reg No:</span><span class='righttext'>549-33-5849-47</span></div><br /><div class='flex-container'><span>Cancellation Fee:</span><span class='righttext'>" + cur2Format.format(CancelFee) + "</span></div><br /></td>");
document.writeln("</tr>");

document.writeln("</table>");
document.writeln("<br />");

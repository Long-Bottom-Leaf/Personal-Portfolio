// Desc: Finals Assignment slideshow and recipt
// Author: Stephen Fennelly
// Dates: April 9, 2025 - April 13, 2025

// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Constants for Loan

const INT_RATE = 0.052;

CurDate = new Date();

// Start function definitions here.

  // Slide show function
let step = 0;
let Images = new Array();
Images[0] ="Images/Taxi 1.jpg";
Images[1] ="Images/Taxi 2.jpg";
Images[2] ="Images/Taxi 3.jpg";
Images[3] ="Images/Taxi 4.jpg";
Images[4] ="Images/Taxi 5.jpg";

window.onload = setInterval(gallery, 4000);

function gallery()
{
  const imgSlideElement = document.getElementById("ImgSlide");
  if (imgSlideElement) {
    imgSlideElement.src = Images[step];
  }

  if (step < Images.length - 1) {
    step++;
  } else {
    step = 0;
  }
}

// Loan Button

function LoanButton()
{
  document.getElementById("LoanButton").innerText = "Loan Analysis Statement";

  let LoanAmt = prompt("Enter the loan amount: ");
  LoanAmt = parseFloat(LoanAmt);
  let Reason = prompt("Enter the reason for the loan: ");
  Reason = Reason.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' '); // While searching for how to capitalize the first letter of multiple words I discovered the arrow function, makes it easier to handle arrays. Turns each word/letter to lower case first, then word => slices the first letter of each word to capitalize

  for (let Years = 1; Years <= 10; Years++)
  {
    let Interest = LoanAmt * INT_RATE * Years;
    let TotAmt = LoanAmt + Interest;
    let MonthPay = TotAmt / (Years * 12);
    console.log("Year: " + Years + " Loan Amount: " + LoanAmt + " Repayment Total: " + TotAmt + " Monthly Payment: " + MonthPay + ")"); // will remove, just for testing
  }

  let YearPay = prompt("Enter the number of years to pay off the loan: ");
  YearPay = parseInt(YearPay);

  // Build table as a string - this is t he only way I could figure out how to do it
  let output = "";

  output += "<table class='loantable'>";
  output += "<tr>";
  output += "<td class='mainhead' colspan='4'>Loan Analysis Statement</td>";
  output += "</tr>";
  
  output += "<tr>";
  output += "<td class='lefttext' colspan='4'>10 Year options for loan of: " + cur2Format.format(LoanAmt) + "</td>";
  output += "</tr>";
  
  output += "<tr>";
  output += "<td class='lefttext' colspan='4'>Loan Reason: " + Reason + "</td>";
  output += "</tr>";
  
  output += "<tr>";
  output += "<td class='lefttext' colspan='4'>Statement Date: " + CurDate.toLocaleDateString() + "</td>";
  output += "</tr>";
  
  output += "<tr>";
  output += "<td class='lefttext'>Years</td>";
  output += "<td class='righttext'>&nbsp&nbsp&nbsp&nbspInterest</td>";
  output += "<td class='righttext'>&nbsp&nbspTotal Amount</td>";
  output += "<td>Monthly Payment</td>";
  output += "</tr>";
  
  for (let Years = 1; Years <= 10; Years++) {
    let Interest = LoanAmt * INT_RATE * Years;
    let TotAmt = LoanAmt + Interest;
    let MonthPay = TotAmt / (Years * 12);
    output += "<tr>";
    output += "<td class='lefttext'>" + Years + "</td>";
    output += "<td class='righttext'>&nbsp&nbsp&nbsp&nbsp" + cur2Format.format(Interest) + "</td>";
    output += "<td class='righttext'>&nbsp&nbsp&nbsp&nbsp" + cur2Format.format(TotAmt) + "</td>";
    output += "<td class='righttext'>" + cur2Format.format(MonthPay) + "&nbsp</td>";
    output += "</tr>";
  }
  
  output += "<br><table class='loantable'>";
  output += "<tr><td class='mainhead' colspan='2'>Your Selected Option</td></tr>";
  output += "<tr><td class='lefttext'>Loan Payoff Period:</td><td class='righttext'>" + YearPay + " Years</td></tr>";
  output += "<tr><td class='lefttext'>Loan Amount:</td><td class='righttext'>" + cur2Format.format(LoanAmt) + "</td></tr>";
  output += "<tr><td class='lefttext'>Total Interest:</td><td class='righttext'>" + cur2Format.format(Interest) + "</td></tr>";
  output += "<tr><td class='lefttext'>Total Repayment:</td><td class='righttext'>" + cur2Format.format(TotAmt) + "</td></tr>";
  output += "<tr><td class='lefttext'>Monthly Payment:</td><td class='righttext'>" + cur2Format.format(MonthPay) + "</td></tr>";
  output += "</table>";

  output += "</table>";

  document.getElementById("LoanButton").innerHTML = output;
  // I was having trouble with the table overriding the page and not printing as a table, innerHTML and the table as a string updates the content of the page without having to reload or navigate away
}




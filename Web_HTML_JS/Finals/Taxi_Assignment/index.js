// Desc: Javascript for the HAB Taxi services
// Author: Kass, Stephen & Leah
// Dates: April 10/2025 - April 18/2025

var $ = function (id) {
  return document.getElementById(id);
};

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

// Start function definitions here.

// Function to create a progress bar for how far scrolled on page
window.addEventListener("scroll", function () {
  const progressBar = document.getElementById("progressBar");
  const scrollTop = window.scrollY;
  const docHeight =
    document.documentElement.scrollHeight -
    document.documentElement.clientHeight;
  const scrollPercentage = (scrollTop / docHeight) * 100;
  progressBar.style.width = scrollPercentage + "%";
});

//Function that creates an audio player for the page
// Identify audio player, collects tracks and sets up for listening.
document.addEventListener("DOMContentLoaded", function () {
  const audioPlayer = document.getElementById("audioPlayer");
  const playlist = document.getElementById("playlist");
  const tracks = playlist.getElementsByTagName("li");

  let currentTrackIndex = 0;

  // Load the first track
  audioPlayer.src = tracks[currentTrackIndex]?.getAttribute("data-src") || "";

  // Play the selected track when clicked
  for (let i = 0; i < tracks.length; i++) {
    tracks[i].addEventListener("click", function () {
      currentTrackIndex = i;
      audioPlayer.src = this.getAttribute("data-src");
      audioPlayer.play();
      document.getElementById(
        "nowPlaying"
      ).textContent = `Now Playing: ${this.textContent}`;
    });
  }
});

//Function for footer copyright year
// Update year element with the current year
document.addEventListener("DOMContentLoaded", function () {
  const yearElement = document.getElementById("year");
  const currentYear = new Date().getFullYear();
  yearElement.textContent = currentYear;
});

//Function for  footer back to top button
document.addEventListener("DOMContentLoaded", function () {
  const scrollToTopButton = document.getElementById("scrollToTop");

  scrollToTopButton.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});

// Constants for Loan

const INT_RATE = 0.052;

CurDate = new Date();

// Start function definitions here.

// Slide show function
let step = 0;
let Images = new Array();
Images[0] = "Images/Taxi 1.jpg";
Images[1] = "Images/Taxi 2.jpg";
Images[2] = "Images/Taxi 3.jpg";
Images[3] = "Images/Taxi 4.jpg";
Images[4] = "Images/Taxi 5.jpg";

window.onload = setInterval(gallery, 4000);

function gallery() {
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

function LoanButton() {
  document.getElementById("LoanButton").innerText = "Loan Analysis Statement";

  let LoanAmt = prompt("Enter the loan amount: ");
  LoanAmt = parseFloat(LoanAmt);
  let Reason = prompt("Enter the reason for the loan: ");
  Reason = Reason.toLowerCase()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" "); // While searching for how to capitalize the first letter of multiple words I discovered the arrow function, makes it easier to handle arrays. Turns each word/letter to lower case first, then word => slices the first letter of each word to capitalize

  for (let Years = 1; Years <= 10; Years++) {
    let Interest = LoanAmt * INT_RATE * Years;
    let TotAmt = LoanAmt + Interest;
    let MonthPay = TotAmt / (Years * 12);
    console.log(
      "Year: " +
        Years +
        " Loan Amount: " +
        LoanAmt +
        " Repayment Total: " +
        TotAmt +
        " Monthly Payment: " +
        MonthPay +
        ")"
    ); // will remove, just for testing
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
  output +=
    "<td class='lefttext' colspan='4'>10 Year options for loan of: " +
    cur2Format.format(LoanAmt) +
    "</td>";
  output += "</tr>";

  output += "<tr>";
  output += "<td class='lefttext' colspan='4'>Loan Reason: " + Reason + "</td>";
  output += "</tr>";

  output += "<tr>";
  output +=
    "<td class='lefttext' colspan='4'>Statement Date: " +
    CurDate.toLocaleDateString() +
    "</td>";
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
    output +=
      "<td class='righttext'>&nbsp&nbsp&nbsp&nbsp" +
      cur2Format.format(Interest) +
      "</td>";
    output +=
      "<td class='righttext'>&nbsp&nbsp&nbsp&nbsp" +
      cur2Format.format(TotAmt) +
      "</td>";
    output +=
      "<td class='righttext'>" + cur2Format.format(MonthPay) + "&nbsp</td>";
    output += "</tr>";
  }

  output += "</table>";

  document.getElementById("LoanButton").innerHTML = output;
  // I was having trouble with the table overriding the page and not printing as a table, innerHTML and the table as a string updates the content of the page without having to reload or navigate away
}

document.addEventListener("DOMContentLoaded", function () {
  const now = new Date();
  const hour = now.getHours();
 
  let greeting = "";
  if (hour >= 5 && hour < 12) {greeting = "Good Morning";}
  else if (hour >= 12 && hour < 16) {greeting = "Good Afternoon";}
  else if (hour >= 16 && hour < 20) {greeting = "Good Evening";}
  else {greeting = "Good Night";}
 
  const quotes = [
    "Road work ahead? Uh, yeah I sure hope it does.",
    "Life is a highway.",
    "Keep on truckin'!",
    "They see me rollin', they hatin'.",
    "The highway's callin', I gotta go."
  ];
 
  const randQuote = quotes[Math.floor(Math.random() * quotes.length)];
 
  const formattedDate = now.toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
 
  document.getElementById("greeting").textContent = greeting;
  document.getElementById("quote").textContent = `"${randQuote}"`;
  document.getElementById("date").textContent = formattedDate;
 });
 
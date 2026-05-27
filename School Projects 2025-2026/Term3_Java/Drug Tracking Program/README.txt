atient Database Management System
Overview

This application is a console-based Java program demonstrating patient database management using OOP concepts such as abstraction, inheritance, encapsulation, and aggregation. It includes an abstract Patient class and two subclasses (Inpatient and Outpatient). A PatientDatabaseManager class manages patients, while the Application class contains the main() method.

How to Compile and Run

Compile:
javac *.java
Run:
java Application

Class Hierarchy

Patient (abstract) → Inpatient, Outpatient
PatientDatabaseManager → manages Patient objects
Application → entry point

Features

➕ Add Patient
🔍 Search by ID
🔁 Update treatment cost
❌ Delete by ID
📃 Display all patients

Sample Data (Application.java)

Inpatient p1 = new Inpatient("P101", "John Doe", 5000.00, 5);
Outpatient p2 = new Outpatient("P102", "Sarah Lee", 350.00);

Example Output

---- Initial Patient List ----
Patient ID: P101, Name: John Doe, Cost: 5000.0, Type: Inpatient
Patient ID: P102, Name: Sarah Lee, Cost: 350.0, Type: Outpatient
Updating treatment cost for patient P101...
---- Updated Patient List ----
Patient ID: P101, Name: John Doe, Cost: 7500.0, Type: Inpatient
Deleting patient P102...
---- Final Patient List ----
Patient ID: P101, Name: John Doe, Cost: 7500.0, Type: Inpatient

OOP Concepts

Abstraction → Patient is abstract with abstract methods
Encapsulation → Private fields with getters/setters
Inheritance → Inpatient and Outpatient extend Patient
Aggregation → PatientDatabaseManager holds a list of patients

Notes

• Ensure all .java files are in one folder
• No extra libraries needed
• Console-based functionality

Testing Tips

• Add several patients
• Try search, update, delete
• Test incorrect IDs
• Display list before and after actions

Author

Developed by [Your Name Here]
For educational use demonstrating Java OOP

License

Free to modify for academic use only
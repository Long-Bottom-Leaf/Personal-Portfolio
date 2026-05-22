package MedicationTracking;

import java.time.LocalDate;
import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        MedicationTracking system = new MedicationTracking();
        boolean exit = false;
        loadSampleData(system);

        Scanner scanner = new Scanner(System.in);
        while (!exit) {
            System.out.println();
            System.out.println("=====Welcome To The Pharmacy Med Tracking System=====");
            System.out.println("What would you like to do? ");
            System.out.println("1: Add A New Patient");
            System.out.println("2: Add A New Doctor");
            System.out.println("3: Add A New Medication To The Pharmacy");
            System.out.println("4: Print System Report");
            System.out.println("5: Check If Meds Are Expired");
            System.out.println("6: Process A New Prescription");
            System.out.println("7: Print All Scripts For Specific Doctor");
            System.out.println("8: Restock the drugs in the pharmacy");
            System.out.println("9: Print all scripts for specific patient");
            System.out.println("10: Exit");
            
            int option = scanner.nextInt();
            scanner.nextLine(); // consume newline
            
            switch (option) {
                case 1:
                    addANewPatient(scanner, system);
                    break;
                case 2:
                    addANewDoctor(scanner, system);
                    break;
                case 3:
                    addNewMedicationToPharmacy(scanner, system);
                    break;
                case 4:
                    printPharmacyReport(system);
                    break;
                case 5:
                    checkExpiredMeds(system);
                    break;
                case 6:
                    processANewScript(scanner, system);
                    break;
                case 7:
                    printScriptsForSpecificDoctor(scanner, system);
                    break;
                case 8:
                    restockPharmacyDrugs(scanner, system);
                    break;
                case 9:
                    printAllScriptsForPatientByName(scanner, system);
                    break;
                case 10:
                    exit = true;
                    System.out.println("Exiting The System! Goodbye!");
                    break;
                default:
                    System.out.println("Invalid option");
            }
        }
        scanner.close();
    }

    private static void loadSampleData(MedicationTracking system) {
        // Doctors
        Doctor drSmith = new Doctor("Dr. John Smith", 45, "709-555-1111", "Cardiology");
        Doctor drLee = new Doctor("Dr. Emily Lee", 39, "709-555-2222", "Neurology");
        Doctor drPatel = new Doctor("Dr. Raj Patel", 50, "709-555-3333", "Family Medicine");
        system.createDoctor(drSmith);
        system.createDoctor(drLee);
        system.createDoctor(drPatel);

        // Patients
        Patient alice = new Patient("Alice Johnson", 30, "709-555-4444");
        Patient bob = new Patient("Bob Williams", 62, "709-555-5555");
        Patient charlie = new Patient("Charlie Brown", 48, "709-555-6666");
        system.createPatient(alice);
        system.createPatient(bob);
        system.createPatient(charlie);

        // Assign patients to doctors
        system.addPatientToDoc("Dr. John Smith", alice);
        system.addPatientToDoc("Dr. Emily Lee", bob);
        system.addPatientToDoc("Dr. Raj Patel", charlie);

        // Medications
        Medication aspirin = new Medication("Aspirin", "100mg", 120, LocalDate.now().plusMonths(8));
        Medication amoxicillin = new Medication("Amoxicillin", "500mg", 80, LocalDate.now().plusYears(1));
        Medication insulin = new Medication("Insulin", "10ml", 40, LocalDate.now().plusMonths(6));
        Medication vitaminD = new Medication("Vitamin D", "1000IU", 200, LocalDate.now().plusYears(2));
        system.createMedication(aspirin);
        system.createMedication(amoxicillin);
        system.createMedication(insulin);
        system.createMedication(vitaminD);

        // Sample prescriptions
        Prescription p1 = new Prescription(drSmith, alice, aspirin, LocalDate.now().plusYears(1));
        Prescription p2 = new Prescription(drLee, bob, amoxicillin, LocalDate.now().plusMonths(9));
        Prescription p3 = new Prescription(drPatel, charlie, vitaminD, LocalDate.now().plusYears(1));

        system.addScriptToPatient(p1);
        system.addScriptToPatient(p2);
        system.addScriptToPatient(p3);
    }

    private static void printAllScriptsForPatientByName(Scanner scanner, MedicationTracking system) {
        System.out.print("Enter patient name: ");
        String patientName = scanner.nextLine();
        Patient patient = system.searchPatientName(patientName);
        system.listAllScriptsForPatient(patient);
        System.out.println();
    }

    private static void restockPharmacyDrugs(Scanner scanner, MedicationTracking system) {
        System.out.print("Enter medication name: ");
        String medName = scanner.nextLine();
        Medication medication = system.searchMedName(medName);
        System.out.print("Enter order quantity: ");
        int orderQuant = scanner.nextInt();
        scanner.nextLine();
        
        system.restockMedication(medication, orderQuant);
        System.out.println();
    }

    private static void printScriptsForSpecificDoctor(Scanner scanner, MedicationTracking system) {
        System.out.print("Enter doctor name: ");
        String docName = scanner.nextLine();
        Doctor doctor = system.searchDoctorName(docName);
        system.listAllScriptsForDoctor(doctor);
    }

    private static void processANewScript(Scanner scanner, MedicationTracking system) {
        System.out.print("Enter patient name: ");
        String patientName = scanner.nextLine();
        Patient patient = system.searchPatientName(patientName);

        System.out.print("Enter doctor name: ");
        String doctorName = scanner.nextLine();
        Doctor doctor = system.searchDoctorName(doctorName);

        System.out.print("Enter medication name: ");
        String medName = scanner.nextLine();
        Medication med = system.searchMedName(medName);

        LocalDate expiry = LocalDate.now().plusYears(1);

        Prescription prescription = new Prescription(doctor, patient, med, expiry);

        system.addScriptToPatient(prescription);

        System.out.println("Prescription added successfully!");
        System.out.println();
    }


    private static void checkExpiredMeds(MedicationTracking system) {
        system.getExpiredMeds();
    }

    private static void printPharmacyReport(MedicationTracking system) {
        system.generateFullReport();
    }

    private static void addNewMedicationToPharmacy(Scanner scanner, MedicationTracking system) {
    System.out.print("Enter medication name: ");
    String name = scanner.nextLine();

    System.out.print("Enter medication dose (e.g., 500mg): ");
    String dose = scanner.nextLine();

    int quantity = 0;
    while (true) {
        System.out.print("Enter quantity available: ");
        if (scanner.hasNextInt()) {
            quantity = scanner.nextInt();
            scanner.nextLine();
            if (quantity >= 0) { 
            System.out.println(quantity + " units of " + name + " added successfully!");
            System.out.println();
            break;}
            else {System.out.println("Quantity must be zero or positive.");}
        } else {
            System.out.println("Please enter a valid integer.");
            scanner.nextLine();
        }
    System.out.println();}

    LocalDate expirationDate = null;
    while (true) {
        System.out.print("Enter expiration date (YYYY-MM-DD): ");
        String expStr = scanner.nextLine();
        try {
            expirationDate = LocalDate.parse(expStr);
            break;
        } catch (Exception e) {
            System.out.println("Invalid date format. Please enter in YYYY-MM-DD format.");
        }
    }

    Medication medication = new Medication(name, dose, quantity, expirationDate);
    system.createMedication(medication);

    System.out.println("Medication added successfully!");
    System.out.println();
}


    private static void addANewDoctor(Scanner scanner, MedicationTracking system) {
        System.out.print("Enter doctor name: ");
        String name = scanner.nextLine();
        System.out.print("Enter doctor age: ");
        int age = scanner.nextInt();
        scanner.nextLine(); // consume newline
        System.out.print("Enter phone number: ");
        String phone = scanner.nextLine();
        System.out.print("Enter doctor specializatoin: ");
        String specialization = scanner.nextLine();

        Doctor doctor = new Doctor(name, age, phone, specialization);

        system.createDoctor(doctor);
        System.out.println("Doctor " + name + " added successfully!");
        System.out.println();
    }

    private static void addANewPatient(Scanner scanner, MedicationTracking system) {
        System.out.print("Enter patient name: ");
        String name = scanner.nextLine();
        System.out.print("Enter patient age: ");
        int age = scanner.nextInt();
        scanner.nextLine(); // consume newline
        System.out.print("Enter phone number: ");
        String phone = scanner.nextLine();

        Patient patient = new Patient(name, age, phone);

        system.createPatient(patient);

        System.out.println("Patient " + name + " added. Please assign a doctor.");
        System.out.print("Enter doctor name: ");
        String docName = scanner.nextLine();
        system.addPatientToDoc(docName, patient);
        System.out.println();
    }
}

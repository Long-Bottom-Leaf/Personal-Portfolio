package MedicationTracking;

import java.time.LocalDate;

public class Test {
    public static void main(String[] args) {
        // Initialize system
        MedicationTracking system = new MedicationTracking();
        System.out.println("Starting Medication Tracking System Test...");

        // Create test doctors
        System.out.println("Creating test data...");
        
        Doctor doc1 = new Doctor("Dr. Alice Smith", 45, "555-1234", "Cardiology");
        Doctor doc2 = new Doctor("Dr. Bob Johnson", 50, "555-9876", "Neurology");

        // Create test patients
        Patient pat1 = new Patient("Jimmy John", 28, "555-0022");
        Patient pat2 = new Patient("Susan Monroe", 34, "555-2266");

        // Create test medications
        Medication med1 = new Medication("Amoxicillin", "500mg", 50, LocalDate.of(2026, 6, 1));
        Medication med2 = new Medication("Ibuprofen", "200mg", 200, LocalDate.of(2025, 1, 15));

        System.out.println("Test data created.");

        // Add to system
        System.out.println("Adding test data to system...");
        system.createDoctor(doc1);
        system.createDoctor(doc2);
        system.createPatient(pat1);
        system.createPatient(pat2);
        system.createMedication(med1);
        system.createMedication(med2);
        System.out.println("Test data added to system.");

        // Assign a patient to a doctor
        System.out.println("Assigning patients to doctors...");
        system.addPatientToDoc(doc1.getName(), pat1);
        system.addPatientToDoc(doc2.getName(), pat2);
        System.out.println("Patients assigned to doctors.");

        // Issue a prescription
        System.out.println("Issuing prescriptions...");
        Prescription presc1 = new Prescription(doc2, pat2, med2, LocalDate.now().plusMonths(6));
        system.addScriptToPatient(presc1);
        
        Prescription presc2 = new Prescription(doc1, pat1, med1, LocalDate.now().plusMonths(3));
        system.addScriptToPatient(presc2);
        System.out.println("Prescriptions issued.");

        // Search for a doctor
        System.out.println("Searching...");
        Doctor searchDoc = system.searchDoctorName("Dr. Alice Smith");
        system.searchDoctorName(searchDoc.getName());
        
        // Search for a patient
        Patient searchPat = system.searchPatientName("Jimmy John");
        system.searchPatientName(searchPat.getName());

        // Search for a medication
        Medication searchMed = system.searchMedName("Ibuprofen");
        system.searchMedName(searchMed.getName());
        System.out.println("Search completed.");

        // Edit doctor information
        System.out.println("Editing information...");
        system.editDoctor("Dr. Bob Johnson", "555-1111", "Pediatrics");
        System.out.println("Information edited.");

        // delete a patient
        System.out.println("Deleting a patient...");
        system.deletePatient("Susan Monroe");
        System.out.println("Patient deleted.");

        // Restock medication
        System.out.println("Restocking medication...");
        system.restockMedication(med2, 100);
        System.out.println("Medication restocked.");

        // Run reports
        System.out.println("Generating reports...");
        system.generateFullReport();
        system.getExpiredMeds();
        system.listAllScriptsForDoctor(doc1);
        system.listAllScriptsForPatient(pat1);
    }

}

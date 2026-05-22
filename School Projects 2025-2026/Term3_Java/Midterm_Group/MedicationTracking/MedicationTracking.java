package MedicationTracking;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Central management class for the pharmacy medication tracking system.
 * Maintains lists of doctors, patients, medications, and prescriptions,
 * and provides methods for searching, adding, and linking them.
 */
public class MedicationTracking {
    private List<Doctor> doctors;
    private List<Patient> patients;
    private List<Medication> medications;
    private List<Prescription> prescriptions;

    /** Constructs an empty MedicationTrackingSystem with no records. */
    public MedicationTracking() {
        doctors = new ArrayList<>();
        patients = new ArrayList<>();
        medications = new ArrayList<>();
        prescriptions = new ArrayList<>();
    }

    /** -------- Search ---------- */
    public Doctor searchDoctorName(String name) {
        for (Doctor d : doctors) {
            if (d.getName().equalsIgnoreCase(name)) {
                return d;
            }
        }
        return null;
    }

    public Patient searchPatientName(String name) {
        for (Patient p : patients) {
            if (p.getName().equalsIgnoreCase(name)) {
                return p;
            }
        }
        return null;
    }

    public Medication searchMedName(String name) {
        for (Medication m : medications) {
            if (m.getName().equalsIgnoreCase(name)) {
                return m;
            }
        }
        return null;
    }

    /** -------- Add -------- */
    public void createDoctor(Doctor doctor) {
        doctors.add(doctor);
    }

    public void createPatient(Patient patient) {
        patients.add(patient);
    }

    public void createMedication(Medication medication) {
        medications.add(medication);
    }

    /** -------- Edit -------- */
    public boolean editDoctor(String name, String newPhone, String newSpec) {
        Doctor d = searchDoctorName(name);
        if (d != null) {
            d.setPhoneNumber(newPhone);
            d.setSpecialization(newSpec);
            return true;
        }
        return false;
    }

    public boolean editPatient(String name, int newAge, String newPhone) {
        Patient p = searchPatientName(name);
        if (p != null) {
            p.setAge(newAge);
            p.setPhoneNumber(newPhone);
            return true;
        }
        return false;
    }

    public boolean editMedication(String name, String newDose, int newQuant, LocalDate newExpDate) {
        Medication m = searchMedName(name);
        if (m != null) {
            m.setDose(newDose);
            m.setQuantityInStock(newQuant);
            m.setNewExp(newExpDate);
            return true;
        }
        return false;
    }

    /** -------- Delete -------- */
    public boolean deleteDoctor(String name) {
        Doctor d = searchDoctorName(name);
        if (d != null) {
            doctors.remove(d);
            return true;
        }
        return false;
    }

    public boolean deletePatient(String name) {
        Patient p = searchPatientName(name);
        if (p != null) {
            patients.remove(p);
            return true;
        }
        return false;
    }

    public boolean deleteMedication(String name) {
        Medication m = searchMedName(name);
        if (m != null) {
            medications.remove(m);
            return true;
        }
        return false;
    }

    /** Adds a patient to a doctor's list */
    public void addPatientToDoc(String docName, Patient patient) {
        Doctor doctor = searchDoctorName(docName);
        if (doctor != null) {
            doctor.getPatients().add(patient);
            if (!patients.contains(patient)) {
                patients.add(patient);
                System.out.println("Patient " + patient.getName() + " assigned to Dr. " + doctor.getName() + ".");
            }
        } else {
            System.out.println("Error: Doctor not found.");
        }
    }

    /** Adds a prescription to a patient and the system */
        public void addScriptToPatient(Prescription prescription) {
        if (prescription == null) {
            System.out.println("Error creating prescription, please try again.");
            return;
        }

        prescriptions.add(prescription);
    }


    /** Generates a full report of the system */
    public void generateFullReport() {
        System.out.println("\n===== Full System Report =====");

        System.out.println("\n===== All Doctors =====");
        if (doctors.isEmpty()) {
            System.out.println("No doctors found.");
        } else {
            for (Doctor d : doctors) {
                System.out.println(d);
            }
        }

        System.out.println("\n===== All Patients =====");
        if (patients.isEmpty()) {
            System.out.println("No patients found.");
        } else {
            for (Patient p : patients) {
                System.out.println(p);
            }
        }

        System.out.println("\n===== All Medications =====");
        if (medications.isEmpty()) {
            System.out.println("No medications found.");
        } else {
            for (Medication m : medications) {
                System.out.println(m);
            }
        }

        System.out.println("\n===== All Prescriptions =====");
        if (prescriptions.isEmpty()) {
            System.out.println("No prescriptions found.");
        } else {
            for (Prescription pr : prescriptions) {
                System.out.println(pr);
            }
        }

        System.out.println("====================================\n");
        System.out.println();
    }

    /** Checks all medications for expiry */
    public void getExpiredMeds() {
        System.out.println("\n===== Medication Expiry Report =====");
        boolean foundExpired = false;
        LocalDate today = LocalDate.now();

        for (Medication med : medications) {
            if (med.getExpirationDate() != null && med.getExpirationDate().isBefore(today)) {
                System.out.println(med.getName() + " (Expired on: " + med.getExpirationDate() + ")");
                foundExpired = true;
            }
        }

        if (!foundExpired) {
            System.out.println("No expired medications found.");
        }
        System.out.println("====================================\n");
    }

    /** Lists all prescriptions for a specific doctor */
    public void listAllScriptsForDoctor(Doctor doctor) {
        if (doctor == null) {
            System.out.println("Error: Doctor not found.");
            return;
        }

        System.out.println("\n--- All prescriptions for Dr. " + doctor.getName() + " ---");

        boolean scriptFound = false;
        for (Prescription p : prescriptions) {
            if (p.getDoctor().equals(doctor)) {
                System.out.println(p);
                scriptFound = true;
            }
        }

        if (!scriptFound) {
            System.out.println("No prescriptions found.");
        }

        System.out.println("====================================\n");
        System.out.println();
    }

    public void listAllScriptsForPatient(Patient patient) {
        if (patient == null) {
            System.out.println("Error: Patient not found.");
            return;
        }

        System.out.println("\n--- All prescriptions for patient " + patient.getName() + " ---");

        boolean scriptFound = false;
        for (Prescription p : prescriptions) {
            if (p.getPatient().equals(patient)) {
                System.out.println(p);
                scriptFound = true;
            }
        }

        if (!scriptFound) {
            System.out.println("No prescriptions found.");
        }
        System.out.println("====================================\n");
        System.out.println();
    }

    /** Restocks a medication */
    public void restockMedication(Medication medication, int orderQuant) {
        if (medication == null) {
            System.out.println("Error: Medication not found.");
            return;
        }

        if (orderQuant <= 1) {
            System.out.println("Error: Order quantity cannot be negative or zero, please enter a positive integer.");
            return;
        }

        int newQuant = medication.getQuantityInStock() + orderQuant;
        medication.setQuantityInStock(newQuant);

        System.out.println("Successfully ordered " + orderQuant + " units of " + medication.getName() + ", Updated quantity: " + newQuant);
    }
}

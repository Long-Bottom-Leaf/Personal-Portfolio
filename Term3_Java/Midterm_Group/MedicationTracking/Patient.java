package MedicationTracking;

import java.util.ArrayList;
import java.util.List;

/**
 * Represents a patient in the pharmacy system.
 * Each patient maintains a list of medications and prescriptions.
 */
public class Patient extends Person {
    private List<Medication> medications;
    private List<Prescription> prescriptions;

    /**
     * Constructs a new Patient with basic personal details.
     *
     * @param name         the patient's name
     * @param age          the patient's age
     * @param phoneNumber  the patient's contact number
     */
    public Patient(String name, int age, String phoneNumber) {
        super(name, age, phoneNumber);
        this.medications = new ArrayList<>();
        this.prescriptions = new ArrayList<>();
    }

    /** @return the list of medications this patient is taking */
    public List<Medication> getMedications() {
        return medications;
    }

    /** @return the list of prescriptions issued to this patient */
    public List<Prescription> getPrescriptions() {
        return prescriptions;
    }

    /**
     * Adds a medication to the patient's list.
     *
     * @param medication the medication to add
     */
    public void addMedication(Medication medication) {
        this.medications.add(medication);
    }

    /**
     * Adds a prescription to the patient's record.
     *
     * @param prescription the prescription to add
     */
    public void addPrescription(Prescription prescription) {
        this.prescriptions.add(prescription);
    }
}

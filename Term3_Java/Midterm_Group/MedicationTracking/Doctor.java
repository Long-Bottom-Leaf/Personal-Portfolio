package MedicationTracking;

import java.util.ArrayList;
import java.util.List;

/**
 * Represents a doctor in the pharmacy system.
 * Each doctor has a specialization and manages a list of patients.
 */
public class Doctor extends Person {
    private String specialization;
    private List<Patient> patients;

    /**
     * Constructs a new Doctor with the given information.
     *
     * @param name          the doctor's full name
     * @param age           the doctor's age
     * @param phoneNumber   the doctor's contact phone number
     * @param specialization the doctor's area of expertise
     */
    public Doctor(String name, int age, String phoneNumber, String specialization) {
        super(name, age, phoneNumber);
        this.specialization = specialization;
        this.patients = new ArrayList<>();
    }

    /** @return the doctor's medical specialization */
    public String getSpecialization() {
        return specialization;
    }

    /** @return the list of patients assigned to this doctor */
    public List<Patient> getPatients() {
        return patients;
    }

    /**
     * Updates the doctor's specialization.
     *
     * @param specialization the new specialization
     */
    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }

    /**
     * Adds a new patient to this doctor's managed list.
     *
     * @param patient the patient to be added
     */
    public void addANewPatient(Patient patient) {
        this.patients.add(patient);
    }

    @Override
    public String toString() {
        return String.format("Doctor ID:%d Name:%s Specialization:%s Patients:%d", getId(), getName(), specialization, patients.size());
    }
}

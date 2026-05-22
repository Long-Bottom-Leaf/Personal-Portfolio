package MedicationTracking;

import java.util.concurrent.atomic.AtomicInteger;
import java.time.LocalDate;

/**
 * Represents a prescription issued by a doctor to a patient.
 * Links a doctor, patient, and medication, and includes an expiration date.
 */
public class Prescription {
    private static final AtomicInteger ID_GEN = new AtomicInteger(0);
    private final int id;
    private Doctor doctor;
    private Patient patient;
    private Medication medication;
    private LocalDate expirationDate;

    /**
     * Constructs a new Prescription object.
     * The expiration date defaults to one year from the current date.
     *
     * @param doctor      the prescribing doctor
     * @param patient     the patient receiving the medication
     * @param medication  the prescribed medication
     * @param expirationDate (optional) a custom expiry date, ignored in this constructor
     */
    public Prescription(Doctor doctor, Patient patient, Medication medication, LocalDate expirationDate) {
        this.id = ID_GEN.getAndIncrement();
        this.doctor = doctor;
        this.patient = patient;
        this.medication = medication;
        this.expirationDate = LocalDate.now().plusYears(1);
    }

    /** @return the unique prescription ID */
    public int getId() {
        return id;
    }

    /** @return the doctor who issued the prescription */
    public Doctor getDoctor() {
        return doctor;
    }

    /** @return the patient assigned this prescription */
    public Patient getPatient() {
        return patient;
    }

    /** @return the prescribed medication */
    public Medication getMedication() {
        return medication;
    }

    /** @return the expiration date of the prescription */
    public LocalDate getExpirationDate() {
        return expirationDate;
    }

    @Override
    public String toString() {
        return String.format("ID:%d Doctor:%s Patient:%s Medication:%s Expiry:%s", id, doctor.getName(), patient.getName(), medication.getName(), expirationDate);
    }
}

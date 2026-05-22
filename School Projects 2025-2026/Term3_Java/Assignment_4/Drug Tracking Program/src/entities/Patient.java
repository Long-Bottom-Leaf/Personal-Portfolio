package entities;

public class Patient {
    // Patient properties
    private int patientId;
    private String patientFirstName;
    private String patientLastName;
    private String patientDOB;

    // Constructor
    public Patient(int patientId, String patientFirstName, String patientLastName, String patientDOB) {
        this.patientId = patientId;
        this.patientFirstName = patientFirstName;
        this.patientLastName = patientLastName;
        this.patientDOB = patientDOB;
    };

    // Getters
    public int getPatientId() { return patientId; }
    public String getPatientFirstName() { return patientFirstName; }
    public String getPatientLastName() { return patientLastName; }
    public String getPatientDOB() { return patientDOB; }

    // Output
    @Override
    public String toString() {
        return patientId + ", " + patientFirstName + ", " + patientLastName + ", " + patientDOB;
    }

    public static Patient fromString(String line) {
        String[] parts = line.split(", ");
        
        return new Patient(
            Integer.parseInt(parts[0]),
            parts[1],
            parts[2],
            parts[3]
        );
    };
}
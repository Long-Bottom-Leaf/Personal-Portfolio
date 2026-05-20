package patient_manager;

import entities.Patient;
import java.sql.*;
import java.util.ArrayList;

public class PatientDatabaseManager {
    // database connection parameters
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/Term3_Java_QAP4";
    private static final String USER = "postgres";
    private static final String PASSWORD = "StudentLogin1234";

    // Add patient to database
    public static void addPatient(Patient patient) {
        String insertSQL = "INSERT INTO patients (patientid, firstname, lastname, dob) VALUES (?, ?, ?, ?)";

        // Establish connection and execute insert
        try (Connection connection = DriverManager.getConnection(DB_URL, USER, PASSWORD);
            PreparedStatement prepStmt = connection.prepareStatement(insertSQL))
        {
            prepStmt.setInt(1, patient.getPatientId());
            prepStmt.setString(2, patient.getPatientFirstName());
            prepStmt.setString(3, patient.getPatientLastName());
            prepStmt.setString(4, patient.getPatientDOB());

            prepStmt.executeUpdate();
            System.out.println("Patient added successfully!");

        } catch (SQLException error) {
            error.printStackTrace();
        };
    };

    // Get all patients from database
    public static ArrayList<Patient> getAllPatients() {
        // Initialize patient list
        ArrayList<Patient> patients = new ArrayList<>();

        String selectSQL = "SELECT * FROM patients";

        // Establish connection and execute query
        try (Connection connection = DriverManager.getConnection(DB_URL, USER, PASSWORD);
            Statement stmt = connection.createStatement();
            ResultSet results = stmt.executeQuery(selectSQL))
        {
            while (results.next()) {
                patients.add(new Patient(
                    results.getInt("patientid"),
                    results.getString("firstname"),
                    results.getString("lastname"),
                    results.getString("dob")
                ));
            }

        } catch (SQLException error) {
            error.printStackTrace();
        };

        return patients;
    };

}

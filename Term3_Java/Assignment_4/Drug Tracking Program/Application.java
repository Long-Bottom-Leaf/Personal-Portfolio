import java.util.InputMismatchException;
import java.util.Scanner;
import entities.Drug;
import entities.Patient;
import patient_manager.DrugFileManager;
import patient_manager.PatientDatabaseManager;

public class Application {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int choice = 0;

        System.out.println("Welcome to the Drug & Patient Tracking Program!");

        // Menu loop
        do {
            System.out.println("\n=== MENU ===");
            System.out.println("1. Save Drug to File");
            System.out.println("2. Read Drugs From File");
            System.out.println("3. Save Patient to Database");
            System.out.println("4. Read Patients From Database");
            System.out.println("0. Exit");
            System.out.print("Choose an option: ");

            // Prevent crash on invalid menu input
            try {
                choice = scan.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid choice! Please enter a number 0-4.");
                scan.nextLine();
                continue;
            }

            scan.nextLine();

            switch (choice) {
                case 1:
                    try {
                        System.out.print("Drug ID: ");
                        int id = scan.nextInt();
                        scan.nextLine();
                        System.out.print("Drug Name: ");
                        String name = scan.nextLine();
                        System.out.print("Drug Cost: ");
                        double cost = scan.nextDouble();
                        scan.nextLine();
                        System.out.print("Dosage: ");
                        String dosage = scan.nextLine();

                        DrugFileManager.addDrug(new Drug(id, name, cost, dosage));
                    } catch (Exception e) {
                        System.out.println("Invalid input! Please try again.");
                        scan.nextLine();
                    }
                    break;

                case 2:
                    System.out.println("\n--- Drugs From File ---");
                    DrugFileManager.loadDrugs().forEach(System.out::println);
                    System.out.println("Drugs successfully loaded.");
                    break;

                case 3:
                    try {
                        System.out.print("Patient ID: ");
                        int patientId = scan.nextInt();
                        scan.nextLine();
                        System.out.print("Patient First Name: ");
                        String patientFirstName = scan.nextLine();
                        System.out.print("Patient Last Name: ");
                        String patientLastName = scan.nextLine();
                        System.out.print("Patient DOB: ");
                        String patientDOB = scan.nextLine();

                        PatientDatabaseManager.addPatient(new Patient(patientId, patientFirstName, patientLastName, patientDOB));
                    } catch (Exception e) {
                        System.out.println("Invalid input! Please try again.");
                        scan.nextLine();
                    }
                    break;

                case 4:
                    System.out.println("\n--- Patients From Database ---");
                    PatientDatabaseManager.getAllPatients().forEach(System.out::println);
                    System.out.println("Patients successfully loaded.");
                    break;

                case 0:
                    System.out.println("Exiting... Thank you for using the program!");
                    break;

                default:
                    System.out.println("Invalid option! Please choose 0-4.");
            }

        } while (choice != 0);

        scan.close();
    }
}

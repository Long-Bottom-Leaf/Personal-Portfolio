package com.gymapp.menu;

import com.gymapp.model.Trainer;
import com.gymapp.util.AppLogger;
import com.gymapp.workout.WorkoutClassService;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class TrainerMenu extends BaseMenu {

    private final WorkoutClassService workoutClassService = new WorkoutClassService();

    private static final DateTimeFormatter FORMATTER =
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

    public TrainerMenu(Trainer trainer) {
        super(trainer);
    }

    @Override
    public void display() {
        showHeader("Trainer Menu");
        System.out.println("1. Create workout class");
        System.out.println("2. Update workout class");
        System.out.println("3. Delete workout class");
        System.out.println("4. View my classes");
        System.out.println("5. Logout");
        System.out.print("Choose an option: ");
    }

    @Override
    public void handleInput() {
        boolean running = true;

        while (running) {
            display();

            String input = scanner.nextLine();

            switch (input) {
                case "1" -> createWorkoutClass();
                case "2" -> updateWorkoutClass();
                case "3" -> deleteWorkoutClass();
                case "4" -> viewMyClasses();
                case "5" -> {
                    System.out.println("Logging out...");
                    running = false;
                }
                default -> System.out.println("Invalid option. Try again.");
            }
        }
    }

    // Menu Actions
    private void createWorkoutClass() {
        try {
            System.out.print("Class name: ");
            String name = scanner.nextLine();

            System.out.print("Description: ");
            String description = scanner.nextLine();

            System.out.print("Schedule (yyyy-MM-dd HH:mm): ");
            LocalDateTime schedule =
                    LocalDateTime.parse(scanner.nextLine(), FORMATTER);

            workoutClassService.createWorkoutClass(
                    user, name, description, schedule
            );

            System.out.println("Workout class created successfully.");

        } catch (Exception error) {
            System.out.println("Failed to create class: " + error.getMessage());
            AppLogger.logErrorTrace("Create class error", error);
        }
    }

    private void updateWorkoutClass() {
        try {
            System.out.print("Class ID: ");
            int classId = Integer.parseInt(scanner.nextLine());

            System.out.print("New name: ");
            String name = scanner.nextLine();

            System.out.print("New description: ");
            String description = scanner.nextLine();

            System.out.print("New schedule (yyyy-MM-dd HH:mm): ");
            LocalDateTime schedule =
                    LocalDateTime.parse(scanner.nextLine(), FORMATTER);

            workoutClassService.updateWorkoutClass(
                    user, classId, name, description, schedule
            );

            System.out.println("Workout class updated successfully.");

        } catch (Exception error) {
            System.out.println("Failed to update class: " + error.getMessage());
            AppLogger.logErrorTrace("Update class error", error);
        }
    }

    private void deleteWorkoutClass() {
        try {
            System.out.print("Class ID to delete: ");
            int classId = Integer.parseInt(scanner.nextLine());

            workoutClassService.deleteWorkoutClass(user, classId);

            System.out.println("Workout class deleted.");

        } catch (Exception error) {
            System.out.println("Failed to delete class: " + error.getMessage());
            AppLogger.logErrorTrace("Delete class error", error);
        }
    }

    private void viewMyClasses() {
        workoutClassService
                .getTrainerWorkoutClasses(user)
                .forEach(System.out::println);
    }
}

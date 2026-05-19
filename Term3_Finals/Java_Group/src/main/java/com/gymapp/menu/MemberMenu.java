package com.gymapp.menu;

import com.gymapp.model.Member;
import com.gymapp.model.WorkoutClass;
import com.gymapp.classenrollment.ClassEnrollmentService;
import com.gymapp.member.MemberService;
import com.gymapp.util.AppLogger;
import com.gymapp.workout.WorkoutClassService;
// import com.gymapp.merchandise.MerchandiseService; // handle later

import java.util.List;

public class MemberMenu extends BaseMenu {

    private final MemberService memberService = new MemberService();
    private final WorkoutClassService workoutClassService = new WorkoutClassService();
    private final ClassEnrollmentService enrollmentService = new ClassEnrollmentService();
    // private final MerchandiseService merchandiseService = new MerchandiseService();

    public MemberMenu(Member member) {
        super(member);
    }

    @Override
    public void display() {
        showHeader("Member Menu");
        System.out.println("1. View available classes");
        System.out.println("2. Enroll in a class");
        System.out.println("3. View my classes");
        System.out.println("4. Purchase Membership / View Expenses");
        System.out.println("5. Store");
        System.out.println("6. Logout");
        System.out.print("Choose an option: ");
    }

    @Override
    public void handleInput() {
        boolean running = true;

        while (running) {
            display();
            String input = scanner.nextLine();

            switch (input) {
                case "1" -> viewAvailableClasses();
                case "2" -> enrollInClass();
                case "3" -> viewMyClasses();
                case "4" -> manageMembership();
                case "5" -> viewStore();
                case "6" -> {
                    System.out.println("Logging out...");
                    running = false;  // Exit loop
                }
                default -> System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    // --- Menu Actions ---

    private void viewAvailableClasses() {
        List<WorkoutClass> classes = workoutClassService.getMemberWorkoutClasses(user);

        if (classes.isEmpty()) {
            System.out.println("No workout classes available.");
            return;
        }

        classes.forEach(System.out::println);
    }

    private void enrollInClass() {
        try {
            viewAvailableClasses();
            System.out.print("Enter Class ID to enroll: ");
            int classId = Integer.parseInt(scanner.nextLine());

            enrollmentService.enrollMember(user, classId);
            System.out.println("Successfully enrolled in class.");

        } catch (Exception error) {
            System.out.println("Enrollment failed: " + error.getMessage());
            AppLogger.logErrorTrace("Enrollment error", error);
        }
    }

    private void viewMyClasses() {
        List<com.gymapp.model.ClassEnrollment> enrollments = enrollmentService.getMemberEnrollments(user);

        if (enrollments.isEmpty()) {
            System.out.println("You are not enrolled in any classes.");
            return;
        }

        enrollments.forEach(System.out::println);
    }

    private void manageMembership() {
        System.out.println("\n--- Membership ---");
        System.out.println("1. Purchase Membership");
        System.out.println("2. View Total Expenses");
        System.out.print("Choose an option: ");

        String option = scanner.nextLine();

        switch (option) {
            case "1" -> {
                try {
                    memberService.purchaseMembership(user);
                    System.out.println("Membership purchased successfully!");
                } catch (Exception e) {
                    System.out.println("Failed to purchase membership: " + e.getMessage());
                }
            }
            case "2" -> {
                double total = memberService.viewTotalExpenses(user);
                System.out.printf("Total membership expenses: $%.2f%n", total);
            }
            default -> System.out.println("Invalid choice.");
        }
    }

    private void viewStore() {
        // merchandiseService.getAllMerchandise().forEach(System.out::println);
        System.out.println("Store menu coming soon...");
    }
}

package com.gymapp.menu;

import com.gymapp.model.Admin;

public class AdminMenu extends BaseMenu {
    public AdminMenu(Admin admin) {
        super(admin);
    }

    @Override
    public void display() {
        System.out.println("Admin Menu");
        System.out.println("1. Manage All Members");
        System.out.println("2. Manage All Trainers");
        System.out.println("3. Manage All Classes");
        System.out.println("4. Manage Store Items");
        System.out.println("5. View Financial Reports");
        System.out.println("6. Logout");
    }

    @Override
    public void handleInput() {
        int choice = scanner.nextInt();

        switch (choice) {
            case 1 -> System.out.println("Manage All Members selected.");
            case 2 -> System.out.println("Manage All Trainers selected.");
            case 3 -> System.out.println("Manage All Classes selected.");
            case 4 -> System.out.println("Manage Store Items selected.");
            case 5 -> System.out.println("View Financial Reports selected.");
            case 6 -> System.out.println("Logout selected.");
            default -> System.out.println("Invalid choice. Please try again.");
        }
    }
}

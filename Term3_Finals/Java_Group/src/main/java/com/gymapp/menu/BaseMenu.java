package com.gymapp.menu;

import java.util.Scanner;

import com.gymapp.model.User;
import com.gymapp.workout.WorkoutClassService;
import com.gymapp.merchandise.MerchandiseService;
import com.gymapp.user.UserService;

public abstract class BaseMenu implements Menu {
    // Menu structure
    protected final User user;
    protected final Scanner scanner = new Scanner(System.in);

    // Services
    protected final WorkoutClassService workoutClassService = new WorkoutClassService();
    protected final MerchandiseService merchandiseService = new MerchandiseService();
    protected final UserService userService = new UserService();

    public BaseMenu(User user) {
        this.user = user;
    }

    protected void showHeader(String title) {
        System.out.println("=== " + title + " ===");
        System.out.println("Logged in as: " + user.getUsername());
    }
}

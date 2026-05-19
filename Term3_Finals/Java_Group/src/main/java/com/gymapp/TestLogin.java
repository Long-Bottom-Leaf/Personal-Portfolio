package com.gymapp;
import com.gymapp.user.UserService;
import com.gymapp.model.User;

public class TestLogin {
    public static void main(String[] args) {
        UserService userService = new UserService();

        User user = userService.login("admin1", "password1");

        if (user != null) {
            System.out.println("Login successful! Welcome " + user.getFirstName());
        } else {
            System.out.println("Login failed!");
        }
    }
}

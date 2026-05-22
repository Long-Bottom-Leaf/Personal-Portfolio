package com.gymapp.user;

import java.sql.SQLException;
import org.mindrot.jbcrypt.BCrypt;
import com.gymapp.model.User;

public class UserService {

    private UserDAO userDAO = new UserDAO();

    public User login(String username, String password) {
        try {
            User user = userDAO.getUserByUsername(username); // Fetch user by username
            if (user == null) {
                System.out.println("User not found.");
                return null; 
            }
            
            if (BCrypt.checkpw(password, user.getPasswordHash())) {
                System.out.println("Login successful!");
                return user;
            } else {
                System.out.println("Invalid password.");
                return null;
            }

        } catch (SQLException e) { // Handle SQL exceptions
            e.printStackTrace();
            return null; 
        }
    }
}

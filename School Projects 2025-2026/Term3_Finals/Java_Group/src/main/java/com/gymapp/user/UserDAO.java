package com.gymapp.user;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import com.gymapp.config.DatabaseConnect;
import com.gymapp.model.User;

public class UserDAO {

    public User getUserByUsername(String username) throws SQLException {
        String sql = "SELECT * FROM users WHERE username = ?";

        try (Connection conn = DatabaseConnect.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, username);

            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    String role = rs.getString("role");
                    int userId = rs.getInt("user_id");
                    String firstName = rs.getString("first_name");
                    String lastName = rs.getString("last_name");
                    String email = rs.getString("email");
                    String passwordHash = rs.getString("password_hash");
                    String phoneNumber = rs.getString("phone_number");
                    String address = rs.getString("address");

                    switch (role) {
                        case "ADMIN":
                            String adminSql = "SELECT * FROM admins WHERE user_id = ?";
                            try (PreparedStatement adminStmt = conn.prepareStatement(adminSql)) {
                                adminStmt.setInt(1, userId);
                                try (ResultSet adminRs = adminStmt.executeQuery()) {
                                    if (adminRs.next()) {
                                        int adminId = adminRs.getInt("admin_id");
                            return new com.gymapp.model.Admin(
                                    adminId, userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, 1
                            );
                                    }
                                }
                            }
                            break;

                        case "TRAINER":
                            String trainerSql = "SELECT * FROM trainers WHERE user_id = ?";
                            try (PreparedStatement trainerStmt = conn.prepareStatement(trainerSql)) {
                                trainerStmt.setInt(1, userId);
                                try (ResultSet trainerRs = trainerStmt.executeQuery()) {
                                    if (trainerRs.next()) {
                                        int trainerId = trainerRs.getInt("trainer_id");
                                        String specialty = trainerRs.getString("specialty");
                                        int experienceYears = trainerRs.getInt("experience_years");
                                        String membershipStatus = trainerRs.getString("membership_status");

                                        return new com.gymapp.model.Trainer(
                                                trainerId, userId, firstName, lastName, username, email,
                                                passwordHash, phoneNumber, address, specialty, experienceYears, membershipStatus, null, null, experienceYears, null
                                        );
                                    }
                                }
                            }
                            break;

                        case "MEMBER":
                            return new com.gymapp.model.Member(
                                    userId, firstName, lastName, username, email, passwordHash, phoneNumber, address
                            );

                        default:
                            throw new SQLException("Unknown user role: " + role);
                    }
                }
            }
        }

        return null;
    }
}

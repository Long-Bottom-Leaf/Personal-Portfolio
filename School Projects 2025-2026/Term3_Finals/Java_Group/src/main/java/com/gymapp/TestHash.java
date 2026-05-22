package com.gymapp;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import com.gymapp.config.DatabaseConnect;

public class TestHash {
    public static void main(String[] args) {
        try (Connection conn = DatabaseConnect.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT username, password_hash FROM users")) {

            while (rs.next()) {
                String username = rs.getString("username");
                String hash = rs.getString("password_hash");
                System.out.println("User: " + username);
                System.out.println("Hash: [" + hash + "]");
                System.out.println("Length: " + hash.length());
                System.out.println("---");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

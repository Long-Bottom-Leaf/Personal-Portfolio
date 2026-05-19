package com.gymapp.config;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnect {
    private static final String URL = "jdbc:postgresql://localhost:5432/gymappdb";
    private static final String USER = "gymappuser";
    private static final String PASSWORD = "password";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public static void main(String[] args) {
        try {
            DatabaseConnect.getConnection();
            System.out.println("Connection successful");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

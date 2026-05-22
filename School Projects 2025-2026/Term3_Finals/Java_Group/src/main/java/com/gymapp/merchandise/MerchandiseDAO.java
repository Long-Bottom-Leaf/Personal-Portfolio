package com.gymapp.merchandise;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import com.gymapp.config.DatabaseConnect;
import com.gymapp.model.User;

public class MerchandiseDAO {
    public User getProductByName(String name) throws SQLException {
        String sql = "SELECT * FROM merchandise WHERE name = ?";

        try (Connection conn = DatabaseConnect.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, name);

            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    }
                }
            }

        return null;
    }
    
}
//CREATE TABLE merchandise (
//    merchandise_id SERIAL PRIMARY KEY,
//    item_name VARCHAR(100) NOT NULL,
//    description TEXT,
//    price DECIMAL(10, 2) NOT NULL,
//    quantity INT NOT NULL
//);  

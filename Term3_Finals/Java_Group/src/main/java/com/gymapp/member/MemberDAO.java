package com.gymapp.member;

import com.gymapp.config.DatabaseConnect;
import com.gymapp.model.Member;
import com.gymapp.util.AppLogger;

import java.sql.*;
import java.time.LocalDate;

public class MemberDAO {

    // READ by user_id (used at login)
    public Member findByUserId(int userId) {
        String sql = """
            SELECT m.member_id,
                   m.membership_status,
                   m.membership_start_date,
                   m.membership_end_date,
                   m.membership_total_revenue,
                   u.user_id,
                   u.first_name,
                   u.last_name,
                   u.username,
                   u.email,
                   u.password_hash,
                   u.phone_number,
                   u.address
            FROM members m
            JOIN users u ON m.user_id = u.user_id
            WHERE u.user_id = ?
            """;

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setInt(1, userId);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    return new Member(
                        resultSet.getInt("member_id"),
                        resultSet.getInt("user_id"),
                        resultSet.getString("first_name"),
                        resultSet.getString("last_name"),
                        resultSet.getString("username"),
                        resultSet.getString("email"),
                        resultSet.getString("password_hash"),
                        resultSet.getString("phone_number"),
                        resultSet.getString("address"),
                        resultSet.getString("membership_status"),
                        resultSet.getDate("membership_start_date").toLocalDate(),
                        resultSet.getDate("membership_end_date") != null
                            ? resultSet.getDate("membership_end_date").toLocalDate()
                            : null,
                        resultSet.getDouble("membership_total_revenue")
                    );
                }
            }

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Failed to load member by user ID", error);
        }

        return null;
    }

    // UPDATE membership info
    public void updateMembership(
            int memberId,
            String status,
            LocalDate start,
            LocalDate end,
            double amount
    ) {
        String sql = """
            UPDATE members
            SET membership_status = ?,
                membership_start_date = ?,
                membership_end_date = ?,
                membership_total_revenue =
                    membership_total_revenue + ?
            WHERE member_id = ?
            """;

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setString(1, status);
            preparedStatement.setDate(2, Date.valueOf(start));
            preparedStatement.setDate(3, end != null ? Date.valueOf(end) : null);
            preparedStatement.setDouble(4, amount);
            preparedStatement.setInt(5, memberId);

            preparedStatement.executeUpdate();

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Failed to update membership", error);
            throw new RuntimeException("Membership update failed");
        }
    }

    // READ member total spent
    public double getTotalRevenue(int memberId) {
        String sql = """
            SELECT membership_total_revenue
            FROM members
            WHERE member_id = ?
            """;

        try (Connection connection = DatabaseConnect.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {

            preparedStatement.setInt(1, memberId);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    return resultSet.getDouble(1);
                }
            }

        } catch (SQLException error) {
            AppLogger.logErrorTrace("Failed to read member revenue", error);
        }

        return 0.0;
    }
}

package com.gymapp.classenrollment;

import com.gymapp.config.DatabaseConnect;
import com.gymapp.model.ClassEnrollment;
import com.gymapp.util.AppLogger;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ClassEnrollmentDAO {

    // Add a new class enrollment
    public void addEnrollment(int memberId, int classId) throws SQLException {
        String sql = "INSERT INTO enrollments (member_id, class_id) VALUES (?, ?)";

        try (Connection conn = DatabaseConnect.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, memberId);
            stmt.setInt(2, classId);
            stmt.executeUpdate();
        }
    }


    // Get all classes a member is enrolled in
    public List<ClassEnrollment> getEnrollmentsByMemberId(int memberId) {
        List<ClassEnrollment> enrollments = new ArrayList<>();
        String sql = "SELECT enrollment_id, member_id, class_id, enrollment_date FROM enrollments WHERE member_id = ?";

        try (Connection conn = DatabaseConnect.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, memberId);
            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    enrollments.add(new ClassEnrollment(
                            rs.getInt("enrollment_id"),
                            rs.getInt("member_id"),
                            rs.getInt("class_id"),
                            rs.getTimestamp("enrollment_date").toLocalDateTime()
                    ));
                }
            }

        } catch (SQLException e) {
            AppLogger.logErrorTrace("Failed to fetch enrollments for member ID: " + memberId, e);
        }

        return enrollments;
    }

    // Check if a member is already enrolled in a class
    public boolean isMemberEnrolled(int memberId, int classId) {
        String sql = "SELECT 1 FROM enrollments WHERE member_id = ? AND class_id = ?";

        try (Connection conn = DatabaseConnect.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, memberId);
            stmt.setInt(2, classId);

            try (ResultSet rs = stmt.executeQuery()) {
                return rs.next(); // true if a row exists
            }

        } catch (SQLException e) {
            AppLogger.logErrorTrace("Failed to check enrollment for member ID: " + memberId + ", class ID: " + classId, e);
            return false;
        }
    }
}

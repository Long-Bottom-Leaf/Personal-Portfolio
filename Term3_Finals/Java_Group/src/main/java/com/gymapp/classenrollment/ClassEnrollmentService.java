package com.gymapp.classenrollment;

import com.gymapp.model.User;
import com.gymapp.util.AppLogger;

import java.util.List;

public class ClassEnrollmentService {

    private final ClassEnrollmentDAO enrollmentDAO = new ClassEnrollmentDAO();

    // Enroll a member in a class
    public void enrollMember(User memberUser, int classId) {
        enforceRole(memberUser, "MEMBER", "enroll in class");

        int memberId = memberUser.getRoleSpecificId();

        if (enrollmentDAO.isMemberEnrolled(memberId, classId)) {
            throw new RuntimeException("Member is already enrolled in this class");
        }

        try {
            enrollmentDAO.addEnrollment(memberId, classId);
            AppLogger.logInfo("Member " + memberUser.getUsername() + " enrolled in class ID " + classId);
        } catch (Exception e) {
            AppLogger.logErrorTrace("Enrollment failed for member " + memberUser.getUsername(), e);
            throw new RuntimeException("Enrollment failed: " + e.getMessage());
        }
    }

    // Get all enrollments for a member
    public List<com.gymapp.model.ClassEnrollment> getMemberEnrollments(User memberUser) {
        enforceRole(memberUser, "MEMBER", "view enrolled classes");
        return enrollmentDAO.getEnrollmentsByMemberId(memberUser.getRoleSpecificId());
    }

    private void enforceRole(User user, String requiredRole, String action) {
        if (!requiredRole.equals(user.getRole())) {
            AppLogger.logWarning("Unauthorized " + action + " attempt by " + user.getUsername() + " (role=" + user.getRole() + ")");
            throw new SecurityException("Access denied");
        }
    }
}

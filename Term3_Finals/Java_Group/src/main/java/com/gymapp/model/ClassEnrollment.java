package com.gymapp.model;

import java.time.LocalDateTime;

public class ClassEnrollment {

    private int enrollmentId;
    private int memberId;
    private int classId;
    private LocalDateTime enrollmentDate;

    public ClassEnrollment() {}

    public ClassEnrollment(int enrollmentId, int memberId,
                           int classId, LocalDateTime enrollmentDate) {
        this.enrollmentId = enrollmentId;
        this.memberId = memberId;
        this.classId = classId;
        this.enrollmentDate = enrollmentDate;
    }

    // Accessors
    public int getEnrollmentId() {
        return enrollmentId;
    }

    public int getMemberId() {
        return memberId;
    }

    public int getClassId() {
        return classId;
    }

    public LocalDateTime getEnrollmentDate() {
        return enrollmentDate;
    }

    // Mutators
    public void setEnrollmentId(int enrollmentId) {
        this.enrollmentId = enrollmentId;
    }

    public void setMemberId(int memberId) {
        this.memberId = memberId;
    }

    public void setClassId(int classId) {
        this.classId = classId;
    }

    public void setEnrollmentDate(LocalDateTime enrollmentDate) {
        this.enrollmentDate = enrollmentDate;
    }

    // toString method
    @Override
    public String toString() {
        return "Class Enrollment -- Enrollment ID: " + enrollmentId +
               ", Member ID: " + memberId +
               ", Class ID: " + classId +
               ", Enrollment Date: " + enrollmentDate;
    }
}
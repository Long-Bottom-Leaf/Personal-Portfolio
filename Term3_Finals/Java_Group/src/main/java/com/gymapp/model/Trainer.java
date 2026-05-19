package com.gymapp.model;

import java.time.LocalDateTime;

public class Trainer extends User {
    // Trainer-specific fields
    private int trainerId;
    private String specialty;
    private int experienceYears;
    private String membershipStatus;
    private LocalDateTime membershipStartDate;
    private LocalDateTime membershipEndDate;
    private double membershipTotalRevenue;

    // Constructor for User fields only
    public Trainer(int userId, String firstName, String lastName, String username, String email,
                   String passwordHash, String phoneNumber, String address, LocalDateTime createdAt) {
        super(userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, "TRAINER", createdAt);
    }

    // Full constructor including trainer-specific fields
    public Trainer(int trainerId, int userId, String firstName, String lastName, String username, String email,
                   String passwordHash, String phoneNumber, String address,
                   String specialty, int experienceYears, String membershipStatus,
                   LocalDateTime membershipStartDate, LocalDateTime membershipEndDate,
                   double membershipTotalRevenue, LocalDateTime createdAt) {
        super(userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, "TRAINER", createdAt);
        this.trainerId = trainerId;
        this.specialty = specialty;
        this.experienceYears = experienceYears;
        this.membershipStatus = membershipStatus;
        this.membershipStartDate = membershipStartDate;
        this.membershipEndDate = membershipEndDate;
        this.membershipTotalRevenue = membershipTotalRevenue;
    }

    // Allow class creation
    @Override
    public boolean canCreateWorkoutClass() {
        return true;
    }

    // Accessors
    public int getTrainerId() { return trainerId; }
    public String getSpecialty() { return specialty; }
    public int getExperienceYears() { return experienceYears; }
    public String getMembershipStatus() { return membershipStatus; }
    public LocalDateTime getMembershipStartDate() { return membershipStartDate; }
    public LocalDateTime getMembershipEndDate() { return membershipEndDate; }
    public double getMembershipTotalRevenue() { return membershipTotalRevenue; }

    // Mutators
    public void setTrainerId(int trainerId) { this.trainerId = trainerId; }
    public void setSpecialty(String specialty) { this.specialty = specialty; }
    public void setExperienceYears(int experienceYears) { this.experienceYears = experienceYears; }
    public void setMembershipStatus(String membershipStatus) { this.membershipStatus = membershipStatus; }
    public void setMembershipStartDate(LocalDateTime membershipStartDate) { this.membershipStartDate = membershipStartDate; }
    public void setMembershipEndDate(LocalDateTime membershipEndDate) { this.membershipEndDate = membershipEndDate; }
    public void setMembershipTotalRevenue(double membershipTotalRevenue) { this.membershipTotalRevenue = membershipTotalRevenue; }

    // toString method
    @Override
    public String toString() {
        return super.toString() + ", Trainer ID: " + trainerId +
               ", Specialty: " + specialty + ", Experience: " + experienceYears +
               " years, Membership Status: " + membershipStatus +
               ", Membership Start: " + membershipStartDate +
               ", Membership End: " + membershipEndDate +
               ", Total Revenue: $" + membershipTotalRevenue;
    }
    @Override
    public int getRoleSpecificId() {
        return trainerId;
    }
}

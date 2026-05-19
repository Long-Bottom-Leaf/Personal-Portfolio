package com.gymapp.model;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class Member extends User {

    // Member-specific fields
    private int memberId;
    private String membershipStatus;
    private LocalDate membershipStartDate;
    private LocalDate membershipEndDate;
    private double membershipTotalRevenue;

    // Default constructor
    public Member() {
        super(0, "", "", "", "", "", "", "", "MEMBER", LocalDateTime.now());
    }

    // Constructor for User fields only
    public Member(int userId, String firstName, String lastName, String username, String email,
                  String passwordHash, String phoneNumber, String address) {
        super(userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, "MEMBER", LocalDateTime.now());
    }

    // Full constructor including member-specific fields
    public Member(int memberId, int userId, String firstName, String lastName, String username, String email,
                  String passwordHash, String phoneNumber, String address,
                  String membershipStatus, LocalDate membershipStartDate,
                  LocalDate membershipEndDate, double membershipTotalRevenue) {

        super(userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, "MEMBER", LocalDateTime.now());
        this.memberId = memberId;
        this.membershipStatus = membershipStatus;
        this.membershipStartDate = membershipStartDate;
        this.membershipEndDate = membershipEndDate;
        this.membershipTotalRevenue = membershipTotalRevenue;
    }

    // Accessors
    public int getMemberId() {
        return memberId;
    }

    public String getMembershipStatus() {
        return membershipStatus;
    }

    public LocalDate getMembershipStartDate() {
        return membershipStartDate;
    }

    public LocalDate getMembershipEndDate() {
        return membershipEndDate;
    }

    public double getMembershipTotalRevenue() {
        return membershipTotalRevenue;
    }

    // Mutators
    public void setMemberId(int memberId) {
        this.memberId = memberId;
    }

    public void setMembershipStatus(String membershipStatus) {
        this.membershipStatus = membershipStatus;
    }

    public void setMembershipStartDate(LocalDate membershipStartDate) {
        this.membershipStartDate = membershipStartDate;
    }

    public void setMembershipEndDate(LocalDate membershipEndDate) {
        this.membershipEndDate = membershipEndDate;
    }

    public void setMembershipTotalRevenue(double membershipTotalRevenue) {
        this.membershipTotalRevenue = membershipTotalRevenue;
    }

    // toString method
    @Override
    public String toString() {
        return super.toString() +
               ", Member ID: " + memberId +
               ", Membership Status: " + membershipStatus +
               ", Membership Start: " + membershipStartDate +
               ", Membership End: " + membershipEndDate +
               ", Total Revenue: $" + membershipTotalRevenue;
    }
    @Override
    public int getRoleSpecificId() {
        return memberId;    
    }
}

package com.gymapp.model;

import java.time.LocalDateTime;

public abstract class User {
    // User constants
    protected int userId;
    protected String firstName;
    protected String lastName;
    protected String username;
    protected String email;
    protected String passwordHash;
    protected String phoneNumber;
    protected String address;
    protected String role;
    protected LocalDateTime createdAt;

    // Default constructor
    public User(int userId, String firstName, String lastName, String username, String email,
                String passwordHash, String phoneNumber, String address, String role, LocalDateTime createdAt) {
        this.userId = userId;
        this.firstName = firstName;
        this.lastName = lastName;
        this.username = username;
        this.email = email;
        this.passwordHash = passwordHash;
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.role = role;
        this.createdAt = createdAt != null ? createdAt : LocalDateTime.now();
    }

    // Simpler constructor that auto-sets createdAt
    public User(int userId, String firstName, String lastName, String username, String email,
                String passwordHash, String phoneNumber, String address, String role) {
        this(userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, role, LocalDateTime.now());
    }

    // Create workout class access
    public boolean canCreateWorkoutClass() {
        return false;
    }

    // Accessors
    public int getUserId() {
        return userId;
    }

    public abstract int getRoleSpecificId();

    public String getUsername() {
        return username;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getPasswordHash() {
        System.out.println("Retrieving password from hash: " + passwordHash);
        return passwordHash;
    }

    public String getEmail() {
        return email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getAddress() {
        return address;
    }

    public String getRole() {
        return role;
    }

    // Mutators
    public void setUserId(int userId) {
        this.userId = userId;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setRole(String role) {
        this.role = role;
    }

    // toString method
    @Override
    public String toString() {
    return "User ID: " + userId + ", Name: " + firstName + " " + lastName + ", Username: " + username + ", Email: " + email +
           ", Phone: " + phoneNumber + ", Address: " + address +
           ", Role: " + role;
    }
}
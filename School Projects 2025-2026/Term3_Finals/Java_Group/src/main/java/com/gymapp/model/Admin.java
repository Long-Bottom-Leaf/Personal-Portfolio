package com.gymapp.model;

import java.time.LocalDateTime;

public class Admin extends User {
    private int adminId;
    private int accessLevel;

    // Default constructor
    public Admin(int adminId, int userId, String firstName, String lastName, String username,
                 String passwordHash, String email, String phoneNumber, String address,
                 LocalDateTime createdAt, int accessLevel) {
        super(userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, "ADMIN", createdAt);
        this.adminId = adminId;
        this.accessLevel = accessLevel;
    }

    // Minimal constructor without createdAt (auto-set to now)
    public Admin(int adminId, int userId, String firstName, String lastName, String username,
                  String email, String passwordHash, String phoneNumber, String address,
                 int accessLevel) {
        super(userId, firstName, lastName, username, email, passwordHash, phoneNumber, address, "ADMIN");
        this.adminId = adminId;
        this.accessLevel = accessLevel;
    }

    // Accessors
    public int getAdminId() {
        return adminId;
    }

    public int getAccessLevel() {
        return accessLevel;
    }

    // Mutators
    public void setAdminId(int adminId) {
        this.adminId = adminId;
    }

    public void setAccessLevel(int accessLevel) {
        this.accessLevel = accessLevel;
    }

    // toString
    @Override
    public String toString() {
        return "Admin -- Admin ID: " + adminId + ", Access Level: " + accessLevel + ", " + super.toString();
    }
    @Override
    public int getRoleSpecificId() {
        return adminId;
    }
}

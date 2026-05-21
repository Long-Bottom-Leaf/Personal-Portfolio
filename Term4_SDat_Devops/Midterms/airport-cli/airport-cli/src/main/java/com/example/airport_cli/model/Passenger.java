package com.example.airport_cli.model;

public class Passenger {

    private Long id;
    private String firstName;
    private String lastName;
    private int phoneNumber;

    // empty constructure for json objects
    public Passenger() {}

    public Passenger(Long id, String firstName, String lastName, int phoneNumber) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
    }

    // getters and setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    @Override
    public String toString() {
        return "Passenger ID: " + getId() +
                "\nName: " + getFirstName() + getLastName() +
                "\nPhone Number: " + getPhoneNumber();
    }
}
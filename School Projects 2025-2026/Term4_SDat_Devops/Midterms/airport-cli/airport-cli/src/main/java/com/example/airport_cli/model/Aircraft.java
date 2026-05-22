package com.example.airport_cli.model;

import java.util.List;

public class Aircraft {

    private Long id;
    private String type;
    private String airlineName;
    private int numberOfPassengers;
    private List<Passenger> passengers;
    private List<Airport> airports;

    public Aircraft() {}

    /* Getters and Setters */
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getAirlineName() {
        return airlineName;
    }

    public void setAirlineName(String airlineName) {
        this.airlineName = airlineName;
    }

    public int getNumberOfPassengers() {
        return numberOfPassengers;
    }

    public void setNumberOfPassengers(int numberOfPassengers) {
        this.numberOfPassengers = numberOfPassengers;
    }

    public List<Passenger> getPassengers() {
        return passengers;
    }

    public void setPassengers(List<Passenger> passengers) {
        this.passengers = passengers;
    }

    public List<Airport> getAirports() {
        return airports;
    }

    public void setAirports(List<Airport> airports) {
        this.airports = airports;
    }

    @Override
    public String toString() {
        return "Aircraft ID: " + getId() +
                "\nAircraft Type: " + getType() +
                "\nAirline Name: " + getAirlineName() +
                "\nNumber of Passengers: " + getNumberOfPassengers() +
                "\nAirports visited: " + getAirports();
    }
}

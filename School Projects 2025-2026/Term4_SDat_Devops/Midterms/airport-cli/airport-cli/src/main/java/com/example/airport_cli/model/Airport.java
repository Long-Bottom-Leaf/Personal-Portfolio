package com.example.airport_cli.model;

import com.example.airport_cli.model.City;

import java.util.List;

public class Airport {

    private Long id;
    private String name;
    private String code;
    private City city;
    private List<Aircraft> aircraft;

    public Airport() {}

    public Airport(Long id, String name, String code, City city) {
        this.id = id;
        this.name = name;
        this.code = code;
        this.city = city;
    }

    /* Getters and Setters */
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public City getCity() {
        return city;
    }

    public void setCity(City city) {
        this.city = city;
    }

    public List<Aircraft> getAircraft() {
        return aircraft;
    }

    public void setAircraft(List<Aircraft> aircraft) {
        this.aircraft = aircraft;
    }

    @Override
    public String toString() {
        return "Airport ID: " + getId() +
                "\nAirport Name: " + getName() +
                "\nAirport Code: " + getCode() +
                "\nLocation City: " + getCity() +
                "\nStationed Aircraft: " + getAircraft();
    }
}

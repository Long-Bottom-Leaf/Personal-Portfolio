package com.example.airport_cli.model;

import java.util.List;

public class City {

    private Long id;
    private String name;
    private String province;
    private int population;

    private List<Airport> airports;

    // empty constructor for json objects
    public City() {}

    public City(Long id, String name, String province, int population) {
        this.id = id;
        this.name = name;
        this.province = province;
        this.population = population;
    }

    // getters and setters
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

    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }

    public int getPopulation() {
        return population;
    }

    public void setPopulation(int population) {
        this.population = population;
    }

    public List<Airport> getAirports() {
        return airports;
    }

    public void setAirports(List<Airport> airports) {
        this.airports = airports;
    }

    @Override
    public String toString() {
        return "City ID: " + getId() +
                "\nCity Name: " + getName() +
                "\nProvince: " + getProvince() +
                "\nPopulation: " + getPopulation() +
                "\nAirports: " + getAirports();
    }
}

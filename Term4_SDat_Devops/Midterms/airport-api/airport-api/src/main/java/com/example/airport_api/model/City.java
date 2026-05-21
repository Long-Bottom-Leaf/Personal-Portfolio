package com.example.airport_api.model;

import jakarta.persistence.*;
import java.util.List;

/*
 * City Entity
 *
  - id: Long (Primary Key, Auto-generated)
  - name: String (Not Null)
  - province: String
  - population: int
  - airports: List<Airport> (One-to-Many relationship with Airport)
 * 
 */

@Entity
@Table(name = "cities")
public class City {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    private String province;

    private int population;

    @OneToMany(mappedBy = "city", cascade = CascadeType.ALL)
    private List<Airport> airports;

    public City(String name, String province) {
        this.name = name;
        this.province = province;
        this.population = 0;
    }

    /*
     * Getters and Setters
     */

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
}
package com.example.airport_cli.service;

import com.example.airport_cli.client.ApiClient;
import com.example.airport_cli.model.Airport;
import com.example.airport_cli.model.City;

import java.io.IOException;
import java.util.Collections;
import java.util.List;

public class CityService {

    private final ApiClient apiClient;

    public CityService(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public List<City> getAllCities() {
        try {
            List<City> cities = apiClient.getAllCities();

            return cities != null ? cities : Collections.emptyList();

        } catch (IOException | InterruptedException error) {
            System.out.println("Error retrieving cities.");

            return Collections.emptyList();
        }
    }

    public List<Airport> getAirportsByCity(Long cityId) {
        if (cityId == null || cityId <= 0) {
            System.out.println("Invalid city ID.");

            return Collections.emptyList();
        }

        try {
            List<Airport> airports = apiClient.getAirportsByCity(cityId);

            return airports != null ? airports : Collections.emptyList();

        } catch (IOException | InterruptedException error) {
            System.out.println("Error retrieving airports.");

            return Collections.emptyList();
        }
    }
}

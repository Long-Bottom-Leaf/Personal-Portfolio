package com.example.airport_cli.service;

import com.example.airport_cli.client.ApiClient;
import com.example.airport_cli.model.Airport;

import java.io.IOException;
import java.util.Collections;
import java.util.List;

public class AircraftService {

    private final ApiClient apiClient;

    public AircraftService(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public List<Airport> getAirportsByAircraft(Long aircraftId) {
        if (aircraftId == null || aircraftId <= 0) {
            System.out.println("Invalid aircraft ID.");

            return Collections.emptyList();
        }

        try {
            List<Airport> airports = apiClient.getAirportsByAircraft(aircraftId);

            return airports != null ? airports : Collections.emptyList();

        } catch (IOException | InterruptedException error) {
            System.out.println("Error retrieving airports.");

            return Collections.emptyList();
        }
    }
}

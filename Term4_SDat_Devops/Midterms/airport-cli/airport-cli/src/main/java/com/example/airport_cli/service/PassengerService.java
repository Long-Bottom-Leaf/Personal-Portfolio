package com.example.airport_cli.service;

import com.example.airport_cli.client.ApiClient;
import com.example.airport_cli.model.Aircraft;
import com.example.airport_cli.model.Airport;
import com.example.airport_cli.model.Passenger;

import java.io.IOException;
import java.util.Collections;
import java.util.List;

public class PassengerService {

    private final ApiClient apiClient;

    public PassengerService(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public List<Passenger> getAllPassengers() {
        try {
            List<Passenger> passengers = apiClient.getAllPassengers();

            return passengers != null ? passengers : Collections.emptyList();

        } catch (IOException | InterruptedException error) {
            System.out.println("Error retrieving passengers.");

            return Collections.emptyList();
        }
    }

    public List<Aircraft> getAircraftByPassenger(Long passengerId) {
        if (passengerId == null || passengerId <= 0) {
            System.out.println("Invalid passenger ID.");

            return Collections.emptyList();
        }

        try {
            List<Aircraft> aircraft = apiClient.getAircraftByPassenger(passengerId);

            return aircraft != null ? aircraft : Collections.emptyList();

        } catch (IOException | InterruptedException error) {
            System.out.println("Error retrieving aircraft.");

            return Collections.emptyList();
        }
    }

    public List<Airport> getAirportsByPassenger(Long passengerId) {
        if (passengerId == null || passengerId <= 0) {
            System.out.println("Invalid passenger ID.");

            return Collections.emptyList();
        }

        try {
            List<Airport> airport = apiClient.getAirportsByPassenger(passengerId);

            return airport != null ? airport : Collections.emptyList();

        } catch (IOException | InterruptedException e) {
            System.out.println("Error retrieving airports.");

            return Collections.emptyList();
        }
    }
}
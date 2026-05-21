package com.example.airport_cli.client;

import com.example.airport_cli.model.Aircraft;
import com.example.airport_cli.model.Airport;
import com.example.airport_cli.model.City;
import com.example.airport_cli.model.Passenger;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.type.TypeReference;

import java.io.IOException;
import java.lang.reflect.Type;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.List;

public class ApiClient {

    private final String BASE_URL = "http://localhost:8080";
    private final HttpClient httpClient;
    private final ObjectMapper objectMapper;

    public ApiClient() {
        this.httpClient = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(5))
                .build();

        this.objectMapper = new ObjectMapper();
    }

    // generic get method to retrieve lists
    private <T> List<T> getList(String endpoint, TypeReference<List<T>> typeReference) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + endpoint))
                .timeout(Duration.ofSeconds(10))
                .header("Accept", "application/json")
                .GET()
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new IOException("Request failed: " + endpoint + " | Status Code: " + response.statusCode());
        }

        return objectMapper.readValue(response.body(), typeReference);
    }

    // cities
    public List<City> getAllCities() throws IOException, InterruptedException {
        return getList("/cities", new TypeReference<List<City>>() {});
    }

    public List<Airport> getAirportsByCity(long cityId) throws IOException, InterruptedException {
        return getList("/cities/" + cityId + "/airports", new TypeReference<List<Airport>>() {});
    }

    // passengers
    public List<Passenger> getAllPassengers() throws IOException, InterruptedException {
        return getList("/passengers", new TypeReference<List<Passenger>>() {});
    }

    public List<Aircraft> getAircraftByPassenger(Long passengerId) throws IOException, InterruptedException {
        return getList("/passengers/" + passengerId + "/aircraft", new TypeReference<List<Aircraft>>() {});
    }

    public List<Airport> getAirportsByPassenger(Long passengerId) throws IOException, InterruptedException {
        return getList("passengers/" + passengerId + "/airports", new TypeReference<List<Airport>>() {});
    }

    // aircraft
    public List<Airport> getAirportsByAircraft(Long aircraftId) throws IOException, InterruptedException {
        return getList("/aircraft/" + aircraftId + "/airports", new TypeReference<List<Airport>>() {});
    }
}
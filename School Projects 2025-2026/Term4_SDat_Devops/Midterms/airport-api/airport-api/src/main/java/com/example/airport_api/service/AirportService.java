package com.example.airport_api.service;

import com.example.airport_api.model.Airport;
import com.example.airport_api.repository.AirportRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AirportService {

    @Autowired
    private AirportRepository airportRepository;

    // Get all airports
    public List<Airport> getAllAirports() {
        return airportRepository.findAll();
    }

    // Get airport by ID
    public Airport getAirportById(Long id) {
        return airportRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Airport not found"));
    }

    // Save new airport
    public Airport saveAirport(Airport airport) {
        return airportRepository.save(airport);
    }

    // Update existing airport
    public Airport updateAirport(Long id, Airport airportDetails) {
        Airport airport = getAirportById(id);

        airport.setName(airportDetails.getName());
        airport.setCode(airportDetails.getCode());
        airport.setCity(airportDetails.getCity());

        return airportRepository.save(airport);
    }

    // Delete airport
    public void deleteAirport(Long id) {
        airportRepository.deleteById(id);
    }
}
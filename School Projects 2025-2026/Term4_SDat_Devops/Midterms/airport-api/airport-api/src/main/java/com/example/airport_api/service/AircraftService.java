package com.example.airport_api.service;

import com.example.airport_api.model.Aircraft;
import com.example.airport_api.repository.AircraftRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/*
 * Aircraftsserive
 *
  - id: Long (Primary Key, Auto-generated)
  - type: String
  - airlineName: String
  - numberOfPassengers: int
  - passengers: List<Passenger> (Many-to-Many relationship with Passenger)
  - airports: List<Airport> (Many-to-Many relationship with Airport)
 * 
 */


@Service
public class AircraftService {

    @Autowired
    private AircraftRepository aircraftRepository;

    // Get all aircraft
    public List<Aircraft> getAllAircraft() {
        return aircraftRepository.findAll();
    }

    // Get aircraft by ID
    public Aircraft getAircraftById(Long id) {
        return aircraftRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Aircraft not found"));
    }

    // Save new aircraft
    public Aircraft saveAircraft(Aircraft aircraft) {
        return aircraftRepository.save(aircraft);
    }

    // Update existing aircraft
    public Aircraft updateAircraft(Long id, Aircraft aircraftDetails) {
        Aircraft aircraft = getAircraftById(id);

        aircraft.setType(aircraftDetails.getType());
        aircraft.setAirlineName(aircraftDetails.getAirlineName());
        aircraft.setNumberOfPassengers(aircraftDetails.getNumberOfPassengers());
        aircraft.setAirports(null);
        aircraft.setPassengers(null);

        return aircraftRepository.save(aircraft);
    }

    // Delete aircraft
    public void deleteAircraft(Long id) {
        aircraftRepository.deleteById(id);
    }
}
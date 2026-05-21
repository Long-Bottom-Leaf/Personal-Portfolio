package com.example.airport_api.repository;

import com.example.airport_api.model.Aircraft;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AircraftRepository extends JpaRepository<Aircraft, Long> {

    List<Aircraft> findByType (String type);
    List<Aircraft> findByAirlineName (String airlineName);
    List<Aircraft> findByNumberOfPassengers (int numberOfPassengers);

}
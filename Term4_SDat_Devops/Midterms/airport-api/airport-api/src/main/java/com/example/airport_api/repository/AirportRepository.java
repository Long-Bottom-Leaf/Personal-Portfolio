package com.example.airport_api.repository;

import com.example.airport_api.model.Airport;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AirportRepository extends JpaRepository<Airport, Long> {

    List<Airport> findByName(String name);
    List<Airport> findByCode(String code);
    List<Airport> findByCityName(String cityName);

}
package com.example.airport_api.service;

import com.example.airport_api.model.City;
import com.example.airport_api.repository.CityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CityService {

    @Autowired
    private CityRepository cityRepository;

    public List<City> getAllCities() {
        return cityRepository.findAll();
    }

    public City getCityById(Long id) {
        return cityRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("City not found"));
    }

    public City saveCity(City city) {
        return cityRepository.save(city);
    }

    public City updateCity(Long id, City cityDetails) {
        City city = getCityById(id);

        city.setName(cityDetails.getName());
        city.setProvince(cityDetails.getProvince());
        city.setPopulation(cityDetails.getPopulation());
        city.setAirports(cityDetails.getAirports());

        return cityRepository.save(city);
    }

    public void deleteCity(Long id) {
        cityRepository.deleteById(id);
    }
}
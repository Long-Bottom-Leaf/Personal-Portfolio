package com.example.airport_api.repository;

import com.example.airport_api.model.City;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface CityRepository extends JpaRepository<City, Long> {

    List<City> findByName(String name);
    List<City> findByProvince(String province);
    List<City> findByPopulationGreaterThan(int population);
    List<City> findByPopulationLessThan(int population);

}
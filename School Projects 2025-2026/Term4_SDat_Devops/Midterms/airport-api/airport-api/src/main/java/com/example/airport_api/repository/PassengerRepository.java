package com.example.airport_api.repository;

import com.example.airport_api.model.Passenger;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PassengerRepository extends JpaRepository<Passenger, Long> {

    List<Passenger> findByFirstName(String firstName);
    List<Passenger> findByLastName(String lastName);
    List<Passenger> findByPhoneNumber(String phoneNumber);
    List<Passenger> findByFirstNameAndLastName(String firstName, String lastName);

}
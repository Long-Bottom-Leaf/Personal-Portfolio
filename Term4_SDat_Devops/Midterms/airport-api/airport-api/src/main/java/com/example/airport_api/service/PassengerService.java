package com.example.airport_api.service;

import com.example.airport_api.model.Passenger;
import com.example.airport_api.repository.PassengerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PassengerService {

    @Autowired
    private PassengerRepository passengerRepository;

    public List<Passenger> getAllPassengers() {
        return passengerRepository.findAll();
    }

    public Passenger getPassengerById(Long id) {
        return passengerRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Passenger not found"));
    }

    public Passenger savePassenger(Passenger passenger) {
        return passengerRepository.save(passenger);
    }

    public Passenger updatePassenger(Long id, Passenger passengerDetails) {
        Passenger passenger = getPassengerById(id);

        passenger.setFirstName(passengerDetails.getFirstName());
        passenger.setLastName(passengerDetails.getLastName());
        passenger.setPhoneNumber(passengerDetails.getPhoneNumber());

        return passengerRepository.save(passenger);
    }

    public void deletePassenger(Long id) {
        passengerRepository.deleteById(id);
    }
}
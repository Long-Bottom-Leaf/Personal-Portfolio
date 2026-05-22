package com.example.airport_cli.service;

import com.example.airport_cli.client.ApiClient;
import com.example.airport_cli.model.Airport;
import com.example.airport_cli.model.Passenger;
import com.example.airport_cli.model.Aircraft;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.List;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class PassengerServiceTest {

    @Mock
    private ApiClient apiClient;

    @InjectMocks
    private PassengerService passengerService;

    @Test
    public void testGetAllPassengers_success() throws Exception {

        Passenger passenger = new Passenger(1L, "Marcus", "Pierce", 7654321);

        when(apiClient.getAllPassengers()).thenReturn(List.of(passenger));

        List<Passenger> result = passengerService.getAllPassengers();

        assertNotNull(result);
        assertEquals(1, result.size());
        assertEquals("Marcus", result.get(0).getFirstName());

        verify(apiClient).getAllPassengers();
    }

    @Test
    public void testGetAllPassengers_nullResponse() throws Exception {

        when(apiClient.getAllPassengers()).thenReturn(null);

        List<Passenger> result = passengerService.getAllPassengers();

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAllPassengers();
    }

    @Test
    public void testGetAllPassengers_apiException() throws Exception {

        when(apiClient.getAllPassengers())
                .thenThrow(new IOException("API failure"));

        List<Passenger> result = passengerService.getAllPassengers();

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAllPassengers();
    }

    @Test
    public void testGetAircraftByPassenger_success() throws Exception {

        Aircraft aircraft = new Aircraft();
        aircraft.setType("Boeing 737");

        when(apiClient.getAircraftByPassenger(1L)).thenReturn(List.of(aircraft));

        List<Aircraft> result = passengerService.getAircraftByPassenger(1L);

        assertNotNull(result);
        assertEquals(1, result.size());
        assertEquals("Boeing 737", result.get(0).getType());

        verify(apiClient).getAircraftByPassenger(1L);
    }

    @Test
    public void testGetAircraftByPassenger_invalidId() {

        List<Aircraft> result = passengerService.getAircraftByPassenger(0L);

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verifyNoInteractions(apiClient);
    }

    @Test
    public void testGetAirportsByPassenger_success() throws Exception {

        Airport airport = new Airport();
        airport.setName("Super Cool Airport");

        when(apiClient.getAirportsByPassenger(1L)).thenReturn(List.of(airport));

        List<Airport> result = passengerService.getAirportsByPassenger(1L);

        assertNotNull(result);
        assertEquals(1, result.size());
        assertEquals("Super Cool Airport", result.get(0).getName());

        verify(apiClient).getAirportsByPassenger(1L);
    }

    @Test
    public void testGetAirportsByPassenger_apiException() throws Exception {

        when(apiClient.getAirportsByPassenger(1L))
                .thenThrow(new IOException("API failure"));

        List<Airport> result = passengerService.getAirportsByPassenger(1L);

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAirportsByPassenger(1L);
    }
}
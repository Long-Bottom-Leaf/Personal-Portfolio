package com.example.airport_cli.service;

import com.example.airport_cli.client.ApiClient;
import com.example.airport_cli.model.Airport;
import com.example.airport_cli.model.City;

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
public class AircraftServiceTest {

    @Mock
    private ApiClient apiClient;

    @InjectMocks
    private AircraftService aircraftService;

    @Test
    public void testGetAirportsByAircraft() throws Exception{

        City city = new City(1L, "St. John's", "Newfoundland", 110000);

        Airport airport = new Airport(
                2L,
                "St. John's International Airport",
                "YYT",
                city
        );

        when(apiClient.getAirportsByAircraft(1l)).thenReturn(List.of(airport));

        List<Airport> result = aircraftService.getAirportsByAircraft(1L);

        assertNotNull(result);
        assertEquals(1, result.size());
        assertEquals("St. John's International Airport", result.get(0).getName());
        assertEquals("St. John's", result.get(0).getCity().getName());

        verify(apiClient).getAirportsByAircraft(1L);
    }

    @Test
    public void testGetAirportsByAircraft_nullResponse() throws Exception {

        when(apiClient.getAirportsByAircraft(1L)).thenReturn(null);

        List<Airport> result = aircraftService.getAirportsByAircraft(1L);

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAirportsByAircraft(1L);
    }

    @Test
    public void testGetAirportsByAircraft_invalidId() {

        List<Airport> result = aircraftService.getAirportsByAircraft(0L);

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verifyNoInteractions(apiClient);
    }

    @Test
    public void testGetAirportsByAircraft_apiException() throws Exception {

        when(apiClient.getAirportsByAircraft(1L))
                .thenThrow(new IOException("API failure"));

        List<Airport> result = aircraftService.getAirportsByAircraft(1L);

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAirportsByAircraft(1L);
    }
}

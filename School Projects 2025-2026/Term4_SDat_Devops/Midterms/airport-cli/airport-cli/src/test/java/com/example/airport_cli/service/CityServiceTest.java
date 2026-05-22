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
public class CityServiceTest {

    @Mock
    private ApiClient apiClient;

    @InjectMocks
    private CityService cityService;

    @Test
    public void testAllCities() throws Exception {

        City city = new City(2L, "St. John's", "Newfoundland", 110000);
        when(apiClient.getAllCities()).thenReturn(List.of(city));

        List<City> result = cityService.getAllCities();

        assertNotNull(result);
        assertEquals(1, result.size());
        assertEquals("St. John's", result.get(0).getName());
        assertEquals(110000, result.get(0).getPopulation());

        verify(apiClient).getAllCities();
    }

    @Test
    public void testGetAllCities_nullResponse() throws Exception {

        when(apiClient.getAllCities()).thenReturn(null);

        List<City> result = cityService.getAllCities();

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAllCities();
    }

    @Test
    public void testGetAllCities_apiException() throws Exception {

        when(apiClient.getAllCities()).thenThrow(new IOException("Request failure"));

        List<City> result = cityService.getAllCities();

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAllCities();
    }

    @Test
    public void testGetAirportsByCity() throws Exception {

        City city = new City(1L, "Toronto", "Ontario", 3000000);
        Airport airport = new Airport(1L, "YYZ International", "YYZ", city);
        when(apiClient.getAirportsByCity(1L)).thenReturn(List.of(airport));

        List<Airport> result = cityService.getAirportsByCity(1L);

        assertNotNull(result);
        assertEquals(1, result.size());
        assertEquals("YYZ International", result.get(0).getName());
        assertEquals("Toronto", result.get(0).getCity().getName());

        verify(apiClient).getAirportsByCity(1L);
    }

    @Test
    public void testGetAirportsByCity_invalidId() {

        List<Airport> result = cityService.getAirportsByCity(0L);

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verifyNoInteractions(apiClient);
    }

    @Test
    public void testGetAirportsByCity_apiException() throws Exception {

        when(apiClient.getAirportsByCity(1L))
                .thenThrow(new IOException("API failure"));

        List<Airport> result = cityService.getAirportsByCity(1L);

        assertNotNull(result);
        assertTrue(result.isEmpty());

        verify(apiClient).getAirportsByCity(1L);
    }
}
package com.example.airport_cli.cli;

import com.example.airport_cli.client.ApiClient;
import com.example.airport_cli.model.*;
import com.example.airport_cli.service.AircraftService;
import com.example.airport_cli.service.CityService;
import com.example.airport_cli.service.PassengerService;

import java.util.List;
import java.util.Scanner;

public class Menu {

    private Scanner scanner;
    private AircraftService aircraftService;
    private CityService cityService;
    private PassengerService passengerService;

    public Menu() {
        scanner = new Scanner(System.in);

        ApiClient apiClient = new ApiClient();

        aircraftService = new AircraftService(apiClient);
        cityService = new CityService(apiClient);
        passengerService = new PassengerService(apiClient);
    }

    public void start() {
        boolean running = true;

        while (running) {
            printMenu();

            int choice;

            if (scanner.hasNextInt()) {
                choice = scanner.nextInt();

            } else {
                System.out.println("Invalid input. Please enter a number.");
                scanner.next();
                continue;
            }

            switch (choice) {

                case 1:
                    listCities();
                    break;

                case 2:
                    airportsByCity();
                    break;

                case 3:
                    aircraftByPassenger();
                    break;

                case 4:
                    airportsByPassenger();
                    break;

                case 5:
                    airportsByAircraft();
                    break;

                case 6:
                    running = false;
                    System.out.println("Goodbye!");
                    break;

                default:
                    System.out.println("Invalid option.");
            }
        }
    }

    private void printMenu() {

        System.out.println("======= Airport CLI =======");
        System.out.println("1. List Cities");
        System.out.println("2. Airports by City");
        System.out.println("3. Aircraft by Passenger");
        System.out.println("4. Airports by Passenger");
        System.out.println("5. Airports by Aircraft");
        System.out.println("6. Exit");

        System.out.print("Select option: ");
    }

    private Long readLong(String message) {

        while (true) {

            System.out.print(message);

            if (scanner.hasNextLong()) {
                return scanner.nextLong();

            } else {
                System.out.println("Invalid input. Please enter a number.");
                scanner.next();
            }
        }
    }

    private void listCities() {
        List<City> cities = cityService.getAllCities();

        if (cities != null && !cities.isEmpty()) {
            for (City city : cities) {
                System.out.println(city);
            }

        } else {
            System.out.println("No cities were found.");
        }
    }

    private void airportsByCity() {
        Long cityId = readLong("Enter city ID: ");

        List<Airport> airports = cityService.getAirportsByCity(cityId);

        if (airports != null && !airports.isEmpty()) {
            for (Airport airport : airports) {
                System.out.println(airport);
            }

        } else {
            System.out.println("No airports were found.");
        }
    }

    private void aircraftByPassenger() {
        Long passengerId = readLong("Enter passenger ID: ");

        List<Aircraft> aircraft = passengerService.getAircraftByPassenger(passengerId);

        if (aircraft != null && !aircraft.isEmpty()) {
            for (Aircraft aircraft1 : aircraft) {
                System.out.println(aircraft1);
            }

        } else {
            System.out.println("No aircraft found.");
        }
    }

    private void airportsByPassenger() {
        Long passengerId = readLong("Enter passenger ID: ");

        List<Airport> airports = passengerService.getAirportsByPassenger(passengerId);

        if (airports != null && !airports.isEmpty()) {
            for (Airport airport : airports) {
                System.out.println(airport);
            }

        } else {
            System.out.println("No airports found.");
        }
    }

    private void airportsByAircraft() {
        Long aircraftId = readLong("Enter aircraft ID: ");

        List<Airport> airports = aircraftService.getAirportsByAircraft(aircraftId);

        if (airports != null && !airports.isEmpty()) {
            for (Airport airport : airports) {
                System.out.println(airport);
            }

        } else {
            System.out.println("No airports found.");
        }
    }
}

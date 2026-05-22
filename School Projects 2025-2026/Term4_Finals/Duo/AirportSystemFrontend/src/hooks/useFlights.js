import { useEffect, useState } from "react";
import { getFlights } from "../api/flightApi";
import { getAirlines } from "../api/airlineApi";
import { getAirports } from "../api/airportApi";
import { getGates } from "../api/gateApi";
import { mapFlightData } from "../utils/mappers";

export const useFlights = () => {
  const [flights, setFlights] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAllData = async () => {
      try {
        setLoading(true);

        const [flightRes, airlineRes, airportRes, gateRes] =
          await Promise.all([
            getFlights(),
            getAirlines(),
            getAirports(),
            getGates(),
          ]);

        const mappedFlights = mapFlightData(
          flightRes.data,
          airlineRes.data,
          airportRes.data,
          gateRes.data
        );

        setFlights(mappedFlights);
      } catch (error) {
        setError(error);
        
      } finally {
        setLoading(false);
      }
    };

    fetchAllData();
  }, []);

  return { flights, loading, error };
};
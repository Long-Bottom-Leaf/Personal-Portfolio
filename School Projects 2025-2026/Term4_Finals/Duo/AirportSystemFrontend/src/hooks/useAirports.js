import { useEffect, useState } from "react";
import { getAirports } from "../api/airportApi";

export const useAirports = () => {
  const [airports, setAirports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getAirports()
      .then((res) => setAirports(res.data))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, []);

  return { airports, loading, error };
};
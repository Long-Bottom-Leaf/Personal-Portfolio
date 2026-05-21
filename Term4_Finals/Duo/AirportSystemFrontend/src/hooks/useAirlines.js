import { useEffect, useState } from "react";
import { getAirlines } from "../api/airlineApi";

export const useAirlines = () => {
  const [airlines, setAirlines] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getAirlines()
      .then((res) => setAirlines(res.data))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, []);

  return { airlines, loading, error };
};
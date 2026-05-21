import { useEffect, useState } from "react";
import { getAircraft } from "../api/aircraftApi";

export const useAircraft = () => {
  const [aircraft, setAircraft] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getAircraft()
      .then((res) => setAircraft(res.data))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, []);

  return { aircraft, loading, error };
};
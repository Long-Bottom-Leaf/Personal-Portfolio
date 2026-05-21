import { useEffect, useState } from "react";
import { getGates } from "../api/gateApi";

export const useGates = () => {
  const [gates, setGates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getGates()
      .then((res) => setGates(res.data))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, []);

  return { gates, loading, error };
};
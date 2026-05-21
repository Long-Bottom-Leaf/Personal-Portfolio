import axios from "./axiosConfig";

// GET all flights
export const getFlights = () => axios.get("/flights");

// GET one flight
export const getFlightById = (id) => axios.get(`/flights/${id}`);

// CREATE flight
export const createFlight = (flightData) =>
  axios.post("/flights", flightData);

// UPDATE flight
export const updateFlight = (id, flightData) =>
  axios.put(`/flights/${id}`, flightData);

// DELETE flight
export const deleteFlight = (id) =>
  axios.delete(`/flights/${id}`);
import axios from "./axiosConfig";

// Get all gates
export const getAirports = () => axios.get("/aircrafts");

// Get one gate
export const getAirportById = (id) => axios.get(`/aircrafts/${id}`);

// Create gate
export const createAirline = (aircraftData) =>
    axios.post("/aircrafts", aircraftData);

// Update gate
export const updateAirline = (id, aircraftData) =>
    axios.put(`/aircrafts/${id}`, aircraftData);

// Delete gate
export const deleteFlight = (id) =>
    axios.delete(`/aircrafts/${id}`);
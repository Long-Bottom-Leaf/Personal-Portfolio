import axios from "./axiosConfig";

// Get all airlines
export const getAirports = () => axios.get("/airlines");

// Get one airline
export const getAirportById = (id) => axios.get(`/airlines/${id}`);

// Create airline
export const createAirline = (airlineData) =>
    axios.post("/airports", airlineData);

// Update airline
export const updateAirline = (id, airlineData) =>
    axios.put(`/airports/${id}`, airlineData);

// Delete airline
export const deleteFlight = (id) =>
    axios.delete(`/airline/${id}`);
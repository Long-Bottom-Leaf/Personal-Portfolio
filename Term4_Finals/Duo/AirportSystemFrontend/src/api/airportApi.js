import axios from "./axiosConfig";

// Get all airports
export const getAirports = () => axios.get("/airports");

// Get one airport
export const getAirportById = (id) => axios.get(`/airports/${id}`);

// Create airport
export const createAirport = (airportData) =>
    axios.post("/airports", airportData);

// Update airport
export const updateAirport = (id, airportData) =>
    axios.put(`/airports/${id}`, airportData);

// Delete airport
export const deleteAirport = (id) =>
    axios.delete(`/airports/${id}`);
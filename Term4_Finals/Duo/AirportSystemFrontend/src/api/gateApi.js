import axios from "./axiosConfig";

// Get all gates
export const getAirports = () => axios.get("/gates");

// Get one gate
export const getAirportById = (id) => axios.get(`/gates/${id}`);

// Create gate
export const createAirline = (gateData) =>
    axios.post("/gates", gateData);

// Update gate
export const updateAirline = (id, gateData) =>
    axios.put(`/gates/${id}`, gateData);

// Delete gate
export const deleteFlight = (id) =>
    axios.delete(`/gates/${id}`);
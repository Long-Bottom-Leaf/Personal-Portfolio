import axios from "./axiosConfig";

export const login = (credentials) =>
  axios.post("/auth/login", credentials);
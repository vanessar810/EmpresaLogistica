import api from "./api";

export const getProductos = () => api.get("/productos/");
export const getBodegas = () => api.get("/bodega/");
export const getPuertos = () => api.get("/puertos/")
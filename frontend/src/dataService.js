import api from "./api";

export const getProductos = () => api.get("/api/productos/");
export const getBodegas = () => api.get("/api/bodega/");
export const getPuertos = () => api.get("/api/puertos/")
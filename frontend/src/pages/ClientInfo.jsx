import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/ClientInfo.css"

const ClientInfo = () => {
    const [form, setForm] = useState({ nombre: "", telefono: "" });
    const { user, isAuthenticated , personalInformation, getToken, updateUser } = useAuth();
    const navigate = useNavigate();

    if (isAuthenticated) {
        console.log("✅ Usuario autenticado:", user);
    } else {
        console.log("⚠️ No hay usuario autenticado");
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = getToken();
            const data = await personalInformation(form.nombre, form.telefono, token);
            console.log("Cliente creado exitosamente");
        // updateUser({ ...user, hasClient: true });
            navigate("/dashboard", { replace: true });
        } catch (error) {
            console.error("Error al guardar cliente: ", error.response?.data || error.message);
        }
    };

    return (
        <div className="client-info">
            <h3>información personal</h3>
            <form onSubmit={handleSubmit}  className="client-form">
                <input
                    placeholder="Nombre"
                    value={form.nombre}
                    onChange={(e) => setForm({ ...form, nombre: e.target.value })}
                /><br />
                <input
                    type="number"
                    placeholder="telefono"
                    value={form.telefono}
                    onChange={(e) => setForm({ ...form, telefono: e.target.value })}
                /><br />
                <button type="submit">Enviar</button>
            </form>
        </div>
    );
};

export default ClientInfo;
import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Register = () => {
    const [form, setForm] = useState({ username: "", email: "", password: "" });
    const { register } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        await register(form.username, form.email, form.password);
        alert("Registro exitoso, ahora inicia sesión");
        navigate("/login");
    };

    return (
        <div style={{ padding: 20 }}>
            <h3>Registro de usuario</h3>
            <form onSubmit={handleSubmit}>
                <input
                    placeholder="Usuario"
                    value={form.username}
                    onChange={(e) => setForm({ ...form, username: e.target.value })}
                /><br />
                <input
                    placeholder="Correo"
                    value={form.email}
                    onChange={(e) => setForm({ ...form, email: e.target.value })}
                /><br />
                <input
                    type="password"
                    placeholder="Contraseña"
                    value={form.password}
                    onChange={(e) => setForm({ ...form, password: e.target.value })}
                /><br />
                <button type="submit">Registrar</button>
            </form>
        </div>
    );
};

export default Register;
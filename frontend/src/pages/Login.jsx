import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [form, setForm] = useState({ username: "", password: "" });
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await login(form.username, form.password);
            navigate("/dashboard");
        } catch (err) {
            alert("Credenciales incorrectas");
        }
    };

    return (
        <div style={{ padding: 20 }}>
            <h3>Inicio de sesión</h3>
            <form onSubmit={handleSubmit}>
                <input
                    placeholder="Usuario"
                    value={form.username}
                    onChange={(e) => setForm({ ...form, username: e.target.value })}
                /><br />
                <input
                    type="password"
                    placeholder="Contraseña"
                    value={form.password}
                    onChange={(e) => setForm({ ...form, password: e.target.value })}
                /><br />
                <button type="submit">Ingresar</button>
            </form>
        </div>
    );
};

export default Login;
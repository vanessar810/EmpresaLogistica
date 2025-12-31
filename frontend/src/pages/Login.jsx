import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/Auth.css"

const Login = () => {
    const [form, setForm] = useState({ email: "", password: "" });
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const userData = await login(form.email, form.password);
            console.log("User after login:", userData);
            if(userData.hasClient){
            navigate("/dashboard");
            } else{
                navigate("/clientInfo");
            }
        } catch (err) {
            alert("Credenciales incorrectas");
        }
    };

    return (
        <div className="auth-container">
            <h3>Inicio de sesión</h3>
            <form onSubmit={handleSubmit} className="auth-form">
                <input
                    placeholder="email"
                    value={form.email}
                    onChange={(e) => setForm({ ...form, email: e.target.value })}
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
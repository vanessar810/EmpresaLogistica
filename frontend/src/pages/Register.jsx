import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { data, useNavigate } from "react-router-dom";

const Register = () => {

    const [form, setForm] = useState({ email: "", password: "" });
    const { register, storeToken  } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await register(form.email, form.password);
        if(data.hasClient)
        {navigate("/dashboard", { replace: true });
        } else{
        console.log("Registro exitoso, ahora inicia sesión");
        navigate("/clientInfo", { replace: true });}
    };
    
    return (
        <div style={{ padding: 20 }}>
            <h3>Registro de usuario</h3>
            <form onSubmit={handleSubmit}>
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
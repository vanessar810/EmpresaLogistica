import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const Navbar = () => {
    const { user, logout } = useAuth();
    return (
        <nav style={{ padding: 10, borderBottom: "1px solid #ccc" }}>
            <Link to="/">Inicio</Link>
            {" | "}
            {user ? (
                <>
                    <Link to="/dashboard">Panel</Link>
                    {" | "}
                    <button onClick={logout}>Cerrar sesión</button>
                </>
            ) : (
                <>
                    <Link to="/login">Login</Link>
                    {" | "}
                    <Link to="/register">Registro</Link>
                </>
            )}
        </nav>
    );
};

export default Navbar;
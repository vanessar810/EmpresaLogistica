import React, {
    createContext,
    useState,
    useContext
} from "react";
import api from "../api";

const AuthContext = createContext();

export const AuthProvider = ({
    children
}) => {
    const [user, setUser] = useState(localStorage.getItem("user") || null);

    const login = async (username, password) => {
        const res = await api.post("/auth/login", {
            username,
            password
        });
        localStorage.setItem("token", res.data.access_token);
        localStorage.setItem("user", username);
        setUser(username);
    };

    const register = async (username, email, password) => {
        await api.post("/auth/register", {
            username,
            email,
            password
        });
    };

    const logout = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("user");
        setUser(null);
    };

    return ( 
    <AuthContext.Provider value = {
            {
                user,
                login,
                register,
                logout
            }
        } > {
            children
        } </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);
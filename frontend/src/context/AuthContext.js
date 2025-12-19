import React, {
    createContext,
    useState,
    useContext,
    useEffect
} from "react";
import api from "../api";

const AuthContext = createContext();

export const AuthProvider = ({children}) => {
        const [user, setUser] = useState(() => {
            const storedUser = localStorage.getItem("user");
            return storedUser ? JSON.parse(storedUser) : null;
        });
        const storeToken = (token) => {
            localStorage.setItem("token", token);
        };
        const getToken = () => {
            return localStorage.getItem("token");
        };

        const login = async (email, password) => {
            const res = await api.post("/auth/login", {email,password});
            const {access_token, hasClient, role, id} = res.data;
            const userData = {email, role, hasClient, id};
            localStorage.setItem("user", JSON.stringify(userData));
            localStorage.setItem("token", access_token);
            setUser(userData);
            return userData;
        };

        const register = async (email, password) => {
            const response = await api.post("/auth/register", {
                email,
                password
            });
            const data = response.data;
            storeToken(data.access_token);
            const userData = {
                id: data.id,       
                email,
                hasClient: data.hasClient,
                role: data.role
                };
            console.log(userData)    
            setUser(userData);
            localStorage.setItem("user", JSON.stringify(userData));
            return userData;
        };

        const personalInformation = async (nombre, telefono, token) => {
            const response = await api.post("/clientes", {
                nombre,
                telefono
            }, {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            });
            console.log(token)
            const data = response.data
            const userData = {
                id: data.id,    
                nombre, 
                email: data.email,
                telefono,  
                hasClient: true,
                };
            console.log("desde personalInformation", userData)    
            setUser(userData);
            localStorage.setItem("user", JSON.stringify(userData));
            return userData;
        };
        const updateUser = (updateUser) => {
            setUser(updateUser);
            localStorage.setItem("user", JSON.stringify(updateUser));
        }

        const logout = () => {
            setUser(null);
            localStorage.removeItem("token");
            localStorage.removeItem("user");
            localStorage.removeItem("authData");
        };
        useEffect(() => {
            getToken()
        }, []);

        const isAuthenticated = !!user;

        return ( <AuthContext.Provider value = {
                {
                    user,
                    storeToken,
                    getToken,
                    login,
                    register,
                    personalInformation,
                    updateUser, 
                    logout,
                    isAuthenticated
                }
            } > {
                children
            } </AuthContext.Provider>);
        };

        export const useAuth = () => useContext(AuthContext);
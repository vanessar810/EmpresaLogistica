import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const PrivateRoute = ({ children }) => {
  const { user } = useAuth();
  console.log("PrivateRoute user:", user);
  if(!user){
    return <Navigate to="/login"/>;}
  if(user && !user.hasClient){  
  return <Navigate to="/clientInfo"/>;}
  return children;
};
export default PrivateRoute;
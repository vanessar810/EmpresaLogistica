import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar'; 
import Landing from "./pages/Landing";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import ClientInfo from "./pages/ClientInfo";
import PrivateRoute from './components/PrivateRoute';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/clientInfo" element={<ClientInfo/>} />
          <Route path="/dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>}/>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;

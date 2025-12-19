import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import ShipmentForm from "../components/ShipmentForm";
import api from "../api";
import ShipmentList from "../components/ShipmentList";

function Dashboard() {
    const { user, getToken } = useAuth();
    const [cliente, setCliente] = useState(null);
    const [loading, setLoading] = useState(true);

    //cargar información del cliente 
    useEffect(() => {
    const getClient = async () => {
        if(user?.id){
            try{
                const token = getToken();
                //console.log(token)
                //console.log("user id: ",user.id)
                const clienteData = await api.get(`/clientes/${user.id}`,{
                headers: {Authorization: `Bearer ${token}`}
        });
        setCliente(clienteData.data);
        console.log("respuesta: ",clienteData)
            } catch (error){
                console.error("Error obteniendo cliente: ",error);
            } finally {setLoading(false);}
        } else {setLoading(false);}
    };
    getClient();
},[user?.id]);
if (loading) return <div>Cargando</div>
if(!cliente) return <div>No hay datos del cliente</div>

    return (
        <div>
            <h2>Bienvenido, {cliente.nombre}</h2>

            <section>
                <h3>Solicitar envío marítimo</h3>
                <ShipmentForm type="maritimo" clienteId={user.id} />
            </section>

            <section>
                <h3>Solicitar envío terrestre</h3>
                <ShipmentForm type="terrestre" clienteId={user.id} />
            </section>

            <section>
                <h3>Mis envios</h3>
                <ShipmentList/>
    
            </section>
        </div>
    );
}

export default Dashboard;

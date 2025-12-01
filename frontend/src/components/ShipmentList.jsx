// src/components/ShipmentList.js
import { useEffect, useState } from "react";
import axios from "axios";

function ShipmentList({ type }) {
    // type = "maritimo" o "terrestre"
    const [shipments, setShipments] = useState([]);

    const fetchShipments = async () => {
        try {
            const endpoint =
                type === "maritimo"
                    ? "http://localhost:5000/api/envios/maritimos"
                    : "http://localhost:5000/api/envios/terrestres";
            const res = await axios.get(endpoint);
            setShipments(res.data);
        } catch (err) {
            console.error(err);
        }
    };

    useEffect(() => {
        fetchShipments();
    }, []);

    return (
        <div>
            <h4>Envíos {type === "maritimo" ? "Marítimos" : "Terrestres"}</h4>
            <ul>
                {shipments.map((s) => (
                    <li key={s.id}>
                        {s.tipo_producto} - Cantidad: {s.cantidad} - Precio: ${s.precio_envio}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ShipmentList;

// src/components/ShipmentList.js
import { useEffect, useState } from "react";
import api from "../api";
import "../styles/ShipmentList.css";

function ShipmentList({ refreshKey }) {
    const [shipments, setShipments] = useState(null);

    const fetchShipments = async () => {
        try {
            const res = await api.get("/api/envios/mis-envios");
            console.log("envios cliente: ", res)
            setShipments(res.data);
        } catch (err) {
            console.error(err);
        }
    };

    useEffect(() => {
        fetchShipments();
    }, [refreshKey]);
    if (!shipments) return <p>Cargando...</p>;

    const noTerrestres = shipments.terrestres.length === 0;
    const noMaritimos = shipments.maritimos.length === 0;
    
    if (noTerrestres && noMaritimos){
        return <p>No tiene envios registrados aún.</p>
    }

    return (
        <div className="shipment-list">
                <h3> Envios Terrestres</h3>
                {noTerrestres ? (
                <p>Sin envíos terrestres</p>
            ) : (
                <table className="shipment-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Producto</th>
                            <th>Cantidad</th>
                            <th>Fecha solicitud</th>
                            <th>Fecha entrega</th>
                            <th>Bodega</th>
                            <th>Placa</th>
                            <th>Guía</th>
                            <th>Precio envio</th>
                            <th>Descuento</th>
                            <th>Total</th>

                        </tr>
                    </thead>
                    <tbody>
                        {shipments.terrestres.map(e => (
                            <tr key={e.id}>
                                <td>{e.id}</td>
                                <td>{e.tipo_producto}</td>
                                <td>{e.cantidad}</td>
                                <td>{e.fecha_registro}</td>
                                <td>{e.fecha_entrega}</td>
                                <td>{e.bodega_entrega}</td>
                                <td>{e.placa}</td>
                                <td>{e.numero_guia}</td>
                                <td>{e.precio_envio.toLocaleString()}</td>
                                <td>{e.descuento}</td>
                                <td>{e.total}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
                <h3> Envios Marítimos</h3>
                {noMaritimos ? (
                <p>Sin envíos marítimos</p>
            ) : (
                <table className="shipment-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Producto</th>
                            <th>Cantidad</th>
                            <th>Fecha solicitud</th>
                            <th>Fecha entrega</th>
                            <th>Puerto</th>
                            <th>Flota</th>
                            <th>Guía</th>
                            <th>Precio envio</th>
                            <th>Descuento</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        {shipments.maritimos.map(e => (
                            <tr key={e.id}>
                                <td> {e.id}</td>
                                <td>{e.tipo_producto}</td>
                                <td>{e.cantidad}</td>
                                <td>{e.fecha_registro}</td>
                                <td>{e.fecha_entrega}</td>
                                <td>{e.puerto_entrega}</td>
                                <td> {e.numero_flota}</td>
                                <td>{e.numero_guia}</td>
                                <td> {e.precio_envio}</td>
                                <td>{e.descuento}</td>
                                <td>{e.total}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
}

export default ShipmentList;

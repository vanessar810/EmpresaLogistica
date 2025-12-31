// src/components/ShipmentForm.js
import { useState, useEffect } from "react";
import { getProductos, getBodegas, getPuertos } from "../dataService";
import api from "../api";
import ConfirmationModal from "./ConfirmationModal";
import "../styles/ShipmentForm.css";

function ShipmentForm({ type, clienteId, onShipmentConfirmed }) {
    const [productos, setProductos] = useState([]);
    const [bodegas, setBodegas] = useState([]);
    const [puertos, setPuertos] = useState([]);
    const [confirmationData, setConfirmationData] = useState(null);
    const [openModal, setOpenModal] = useState(false);

    //cargar productos, bodega, puertos
    useEffect(() => {
        const fetchData = async () => {
            try {
                const [productoResponse, bodegaResponse, puertosResponse] = await Promise.all([
                    getProductos(),
                    getBodegas(),
                    getPuertos()
                ]);
                setProductos(productoResponse.data);
                console.log(productoResponse.data)
                setBodegas(bodegaResponse.data);
                setPuertos(puertosResponse.data);
            } catch (error) {
                console.error("Error cargando datos: ", error);
            }
        };
        fetchData();
    }, []);

    // type = "maritimo" o "terrestre"
    const [shipment, setShipment] = useState({
        productoId: "",
        cantidad: "",
        fechaRecogida: "",
        puertoId: "",  // si marítimo
        bodegaId: "",  // si terrestre
    });

    const handleChange = (e) => {
        setShipment({ ...shipment, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const payload = {
                ...shipment,
                cantidad: Number(shipment.cantidad),
                productoId: Number(shipment.productoId),
                fechaRecogida: new Date(shipment.fechaRecogida).toISOString().split("T")[0],
                puertoId: shipment.puertoId ? Number(shipment.puertoId) : null,
                bodegaId: shipment.bodegaId ? Number(shipment.bodegaId) : null,
                cliente_id: clienteId
            };
            console.log("enviando: ", payload)
            const envioPreparado = await api.post("/preparacion/envio", payload);
            setConfirmationData(envioPreparado.data)
            setOpenModal(true)
            console.log("Envío registrado correctamente ", envioPreparado);
        } catch (err) {
            console.error(err);
            alert("Error al registrar envío");
            console.log("Error al registrar envío");
        }
    };
    const handleConfirm = async () => {
        try {
            
            const endpoint = "/envios/confirmar";
            console.log("para confirmación del envio: ", confirmationData.id)
            const response = await api.post(endpoint, {id:confirmationData.id})
            console.log("envio final: ", response)
            onShipmentConfirmed();
        } catch (error) {
            console.error("Error confirmando envio:", error);
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit} className="shipment-form">
                <label>Producto: </label>
                <select name="productoId" value={shipment.productoId} onChange={handleChange} required>
                    <option value="">Seleccionar producto</option>
                    {productos.map(p => (
                        <option key={p.id} value={p.id}>
                            {p.nombre}
                        </option>
                    ))}
                </select>
                <label> Cantidad: </label>
                <input
                    name="cantidad"
                    type="number"
                    placeholder="Cantidad"
                    value={shipment.cantidad}
                    onChange={handleChange}
                    required
                />
                <label> Fecha de recogida: </label>
                <input
                    name="fechaRecogida"
                    type="date"
                    value={shipment.fechaRecogida}
                    onChange={handleChange}
                    required
                />
                {type === "maritimo" ? (
                    <select name="puertoId" value={shipment.puertoId} onChange={handleChange} required>
                        <option value="">Seleccionar puerto</option>
                        {puertos.map(p => (
                            <option key={p.id} value={p.id}>
                                {p.nombre}
                            </option>
                        ))}
                    </select>
                ) : (
                    <select name="bodegaId" value={shipment.bodegaId} onChange={handleChange}>
                        <option value="">Seleccionar Bodega</option>
                        {bodegas.map(p => (
                            <option key={p.id} value={p.id}>
                                {p.nombre}
                            </option>
                        ))}
                    </select>
                )}
                <button type="submit">Solicitar envío</button>

            </form>

            <ConfirmationModal
                open={openModal}
                data={confirmationData}
                onConfirm={()=>{handleConfirm();
                    setOpenModal(false);
                }}
                onCancel={() => setOpenModal(false)}
            />
        </div>
    );
}

export default ShipmentForm;

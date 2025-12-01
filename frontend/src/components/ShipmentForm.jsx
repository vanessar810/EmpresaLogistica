// src/components/ShipmentForm.js
import { useState } from "react";
import axios from "axios";

function ShipmentForm({ type, clienteId }) {
    // type = "maritimo" o "terrestre"
    const [shipment, setShipment] = useState({
        tipo_producto: "",
        cantidad: 1,
        fecha_registro: "",
        fecha_entrega: "",
        puerto_entrega: "",  // si marítimo
        bodega_entrega: "",  // si terrestre
        precio_envio: 0,
        descuento: 0,
        numero_flota: "",    // marítimo
        placa: "",           // terrestre
        numero_guia: "",
    });

    const handleChange = (e) => {
        setShipment({ ...shipment, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const payload = { ...shipment,precio_envio: 0, cliente_id: clienteId };
            const endpoint =
                type === "maritimo"
                    ? "http://localhost:5000/api/envios/maritimos"
                    : "http://localhost:5000/api/envios/terrestres";

            await axios.post(endpoint, payload);
            alert("Envío registrado correctamente");
            setShipment({
                tipo_producto: "",
                cantidad: 1,
                fecha_registro: "",
                fecha_entrega: "",
                puerto_entrega: "",
                bodega_entrega: "",
                precio_envio: 0,
                descuento: 0,
                numero_flota: "",
                placa: "",
                numero_guia: "",
            });
        } catch (err) {
            console.error(err);
            alert("Error al registrar envío");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                name="tipo_producto"
                placeholder="Tipo de producto"
                value={shipment.tipo_producto}
                onChange={handleChange}
                required
            />
            <input
                name="cantidad"
                type="number"
                placeholder="Cantidad"
                value={shipment.cantidad}
                onChange={handleChange}
                required
            />
            <input
                name="fecha_registro"
                type="date"
                value={shipment.fecha_registro}
                onChange={handleChange}
                required
            />
            <input
                name="fecha_entrega"
                type="date"
                value={shipment.fecha_entrega}
                onChange={handleChange}
                required
            />
            {type === "maritimo" ? (
                <input
                    name="puerto_entrega"
                    placeholder="Puerto de entrega"
                    value={shipment.puerto_entrega}
                    onChange={handleChange}
                    required
                />
            ) : (
                <input
                    name="bodega_entrega"
                    placeholder="Bodega de entrega"
                    value={shipment.bodega_entrega}
                    onChange={handleChange}
                    required
                />
            )}
            <input
                name="precio_envio"
                type="number"
                placeholder="Precio envío"
                value={shipment.precio_envio}
                onChange={handleChange}
                required
            />
            <input
                name="descuento"
                type="number"
                placeholder="Descuento"
                value={shipment.descuento}
                onChange={handleChange}
            />
            {type === "maritimo" ? (
                <input
                    name="numero_flota"
                    placeholder="Número de flota"
                    value={shipment.numero_flota}
                    onChange={handleChange}
                    required
                />
            ) : (
                <input
                    name="placa"
                    placeholder="Placa del vehículo"
                    value={shipment.placa}
                    onChange={handleChange}
                    required
                />
            )}
            <input
                name="numero_guia"
                placeholder="Número de guía"
                value={shipment.numero_guia}
                onChange={handleChange}
                required
            />
            <button type="submit">Solicitar envío</button>
        </form>
    );
}

export default ShipmentForm;

// src/components/ProductForm.js
import { useState } from "react";
import axios from "axios";

function ProductForm({ onSaved }) {
    const [product, setProduct] = useState({
        tipo_producto: "",
        cantidad: 1,
    });

    const handleChange = (e) => {
        setProduct({ ...product, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post("http://localhost:5000/api/productos", product);
            onSaved(); // Para actualizar lista de productos en Dashboard
            setProduct({ tipo_producto: "", cantidad: 1 });
        } catch (err) {
            console.error(err);
            alert("Error al guardar el producto");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                name="tipo_producto"
                placeholder="Tipo de producto"
                value={product.tipo_producto}
                onChange={handleChange}
                required
            />
            <input
                name="cantidad"
                type="number"
                placeholder="Cantidad"
                value={product.cantidad}
                onChange={handleChange}
                required
            />
            <button type="submit">Registrar Producto</button>
        </form>
    );
}

export default ProductForm;

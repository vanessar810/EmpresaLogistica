// src/components/ProductList.js
import { useEffect, useState } from "react";
import axios from "axios";

function ProductList() {
    const [products, setProducts] = useState([]);

    const fetchProducts = async () => {
        try {
            const res = await axios.get("http://localhost:5000/api/productos");
            setProducts(res.data);
        } catch (err) {
            console.error(err);
        }
    };

    useEffect(() => {
        fetchProducts();
    }, []);

    return (
        <div>
            <h3>Productos registrados</h3>
            <ul>
                {products.map((p) => (
                    <li key={p.id}>
                        {p.tipo_producto} - Cantidad: {p.cantidad}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ProductList;

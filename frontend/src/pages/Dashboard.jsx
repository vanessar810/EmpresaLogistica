import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import ProductForm from "../components/ProductForm";
import ProductList from "../components/ProductList";
import ShipmentForm from "../components/ShipmentForm";

function Dashboard() {
    const { user } = useContext(AuthContext); // suponiendo que user tiene id

    return (
        <div>
            <h2>Bienvenido, {user.name}</h2>

            <section>
                <h3>Registrar producto</h3>
                <ProductForm onSaved={() => { }} />
            </section>

            <section>
                <h3>Productos existentes</h3>
                <ProductList />
            </section>

            <section>
                <h3>Solicitar envío marítimo</h3>
                <ShipmentForm type="maritimo" clienteId={user.id} />
            </section>

            <section>
                <h3>Solicitar envío terrestre</h3>
                <ShipmentForm type="terrestre" clienteId={user.id} />
            </section>
        </div>
    );
}

export default Dashboard;

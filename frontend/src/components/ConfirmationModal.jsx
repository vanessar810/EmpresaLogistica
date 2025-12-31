import "../styles/ConfirmationModal.css";

function ConfirmationModal({ open, data, onConfirm, onCancel}){
    if (!open || !data) return null;


    return(
    <div className="modal-overlay">
        <div className="modal-content">
            <h2> confirmar envio</h2>
            <div>
                <p><strong> Producto: </strong> {data.producto}</p>
                <p><strong> Cantidad: </strong> {data.cantidad}</p>
                <p><strong> Precio del envio: </strong> ${data.precioEnvio}</p>
                <p><strong> Precio producto: </strong> ${data.precioProductos}</p>
                <p><strong> Descuento: </strong> ${data.descuento}</p>
                <p><strong> Precio total: </strong> ${data.total}</p>
                <p><strong> Fecha estimada de entrega: </strong> ${data.fechaEntrega}</p>
                {data.placa && (
                        <p><strong>Placa asignada:</strong> {data.placa}</p>
                    )}
                {data.numeroFlota && (
                        <p><strong>Flota asignada:</strong> {data.numeroFlota}</p>
                    )}
                <p><strong>Número de guía:</strong> {data.numeroGuia}</p>
            </div>
            <div className="modal-buttons">
                <button onClick={onCancel}>Cancelar</button>
                <button onClick={onConfirm}>Confirmar envío</button>
            </div>
        </div>
    </div>
    );
};
export default ConfirmationModal
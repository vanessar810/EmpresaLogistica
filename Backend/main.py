from fastapi import FastAPI
from fastapi.requests import Request
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from app.auth.auth_controller import router as auth_router
from app.configuration.database import Base, engine
from app.controller import cliente_controller, envio_controller
from app.openApi.docs_config import custom_openapi
from fastapi.responses import JSONResponse
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Logística", description="API RESTful con JWT, CRUD, filtros y validaciones.",
    version="1.0.0")

# CORS 
origins = [
    "http://localhost:3000",   # React local
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router)
app.include_router(cliente_controller.router,  prefix="/clientes")
app.include_router(envio_controller.router, prefix="/envios")

@app.get("/", tags=["root"])
def root():
    return {"message": "API Logística funcionando correctamente 🚛🚢"}

app.openapi = lambda: custom_openapi(app)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"Error en {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor. Intente más tarde."},
    )

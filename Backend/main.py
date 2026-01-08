from fastapi import FastAPI
from fastapi.requests import Request
from fastapi import Request
from fastapi.responses import JSONResponse 
from fastapi.middleware.cors import CORSMiddleware
from app.auth.auth_controller import router as auth_router
from app.configuration.database import Base, engine, SessionLocal
from app.controller import cliente_controller, envio_controller, puerto_controller, producto_controller, bodega_controller, prep_envio_controller
from app.openApi.docs_config import custom_openapi
from app.repository.data_seed import seed_data
from contextlib import asynccontextmanager
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    # seed_data(db) # se desactiva una vez cargada toda la información.
    db.close()
    yield

app = FastAPI(title="API Logística", description="API RESTful con JWT, CRUD, filtros y validaciones.",
    version="1.0.0", lifespan=lifespan)

# CORS 
origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
    "https://empresalogistica.vercel.app",
    "https://empresalogistica.vercel.app/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Routers
app.include_router(auth_router)
app.include_router(cliente_controller.router)
app.include_router(envio_controller.router)
app.include_router(producto_controller.router)
app.include_router(puerto_controller.router)
app.include_router(bodega_controller.router)
app.include_router(prep_envio_controller.router)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

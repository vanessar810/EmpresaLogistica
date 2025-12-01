from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API Logística Terrestre y Marítima",
        version="1.0.0",
        description="API RESTful con autenticación JWT, CRUD, filtros y validaciones.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
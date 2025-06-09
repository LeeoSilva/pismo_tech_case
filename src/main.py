from src.routes import router
import fastapi


app = fastapi.FastAPI(
    title="Pismo Tech Case",
    description="API for Pismo Tech Case",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

app.include_router(router, prefix="/api/v1", tags=["v1"])

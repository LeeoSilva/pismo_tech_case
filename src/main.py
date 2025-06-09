from src.routes import router
import fastapi


app = fastapi.FastAPI(
    title="Pismo Tech Case",
    description="API for Pismo Tech Case",
    version="1.0.0",
)

app.include_router(router, prefix="/api", tags=["/"])

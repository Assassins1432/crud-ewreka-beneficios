from fastapi import FastAPI
from .app.routes.beneficio_routes import router as BeneficioRouter

app = FastAPI()

app.include_router(BeneficioRouter, prefix="/beneficios", tags=["beneficios"])

@app.get("/")
async def read_root():
    return {"mensaje": "Bienvenido al taller de FastAPI con MongoDB"}

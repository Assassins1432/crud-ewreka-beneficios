from fastapi import FastAPI
from routes import benefits

app = FastAPI()

app.include_router(benefits.router)

@app.get("/")
async def read_root():
    return {"mensaje": "Bienvenido al taller de FastAPI con MongoDB"}

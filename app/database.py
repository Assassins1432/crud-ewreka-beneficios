from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Cadena de conexión a MongoDB desde variables de entorno
MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.taller_fastapi
beneficios_collection = database.get_collection("beneficios")

# Función para conectar a MongoDB
def get_beneficio_collection():
    return beneficios_collection
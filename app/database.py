from motor.motor_asyncio import AsyncIOMotorClient
from .models import Beneficio

# Cadena de conexión a MongoDB
MONGO_DETAILS = "mongodb+srv://Tester:Test1234@testing.mzysw.mongodb.net/?retryWrites=true&w=majority&appName=Testing"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.taller_fastapi
beneficios_collection = database.get_collection("beneficios")

# Función para conectar a MongoDB
def get_beneficio_collection():
    return beneficios_collection

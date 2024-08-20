from bson import ObjectId
from .database import get_beneficio_collection
from .models import Beneficio

beneficios_collection = get_beneficio_collection()

# Crear un nuevo beneficio sustentable
async def crear_beneficio(beneficio: Beneficio):
    beneficio = await beneficios_collection.insert_one(beneficio.dict())
    nuevo_beneficio = await beneficios_collection.find_one({"_id": beneficio.inserted_id})
    return nuevo_beneficio

# Obtener todos los beneficios sustentables
async def obtener_beneficios():
    beneficios = []
    async for beneficio in beneficios_collection.find():
        beneficios.append(beneficio)
    return beneficios

# Obtener un beneficio sustentable por ID
async def obtener_beneficio_por_id(id: str):
    beneficio = await beneficios_collection.find_one({"_id": ObjectId(id)})
    return beneficio

# Actualizar un beneficio sustentable
async def actualizar_beneficio(id: str, data: dict):
    if len(data) < 1:
        return False
    beneficio = await beneficios_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return beneficio

# Eliminar un beneficio sustentable
async def eliminar_beneficio(id: str):
    beneficio = await beneficios_collection.delete_one({"_id": ObjectId(id)})
    return beneficio.deleted_count

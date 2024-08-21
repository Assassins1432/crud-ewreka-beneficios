from fastapi import APIRouter, HTTPException
from typing import List
from app import crud
from app import models

router = APIRouter(prefix="/beneficios", tags=["beneficios"])

# Ruta para crear un nuevo beneficio
@router.post("/", response_description="Crear un nuevo beneficio", response_model=models.Beneficio)
async def route_crear_beneficio(beneficio: models.Beneficio):
    nuevo_beneficio = await crud.crear_beneficio(beneficio)
    return nuevo_beneficio

# Ruta para obtener todos los beneficios
@router.get("/", response_description="Obtener todos los beneficios", response_model=List[models.Beneficio])
async def route_obtener_beneficios():
    beneficios = await crud.obtener_beneficios()
    return beneficios

# Ruta para obtener un beneficio por ID
@router.get("/{id}", response_description="Obtener un beneficio por ID", response_model=models.Beneficio)
async def route_obtener_beneficio(id: str):
    beneficio = await crud.obtener_beneficio_por_id(id)
    if beneficio is None:
        raise HTTPException(status_code=404, detail="Beneficio no encontrado")
    return beneficio

# Ruta para actualizar un beneficio por ID
@router.put("/{id}", response_description="Actualizar un beneficio", response_model=models.Beneficio)
async def route_actualizar_beneficio(id: str, beneficio: models.Beneficio):
    actualizado = await crud.actualizar_beneficio(id, beneficio.dict(exclude_unset=True))
    if actualizado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Beneficio no encontrado")
    return await crud.obtener_beneficio_por_id(id)

# Ruta para eliminar un beneficio por ID
@router.delete("/{id}", response_description="Eliminar un beneficio")
async def route_eliminar_beneficio(id: str):
    eliminado = await crud.eliminar_beneficio(id)
    if eliminado == 0:
        raise HTTPException(status_code=404, detail="Beneficio no encontrado")
    return {"mensaje": "Beneficio eliminado con éxito"}

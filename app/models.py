from pydantic import BaseModel, Field
from typing import Optional

class Beneficio(BaseModel):
    nombre: str = Field(..., description="El nombre del beneficio")
    descripcion: Optional[str] = Field(None, description="Descripción del beneficio")
    valor: float = Field(..., description="Valor monetario del beneficio")
    activo: bool = Field(..., description="Indica si el beneficio está activo")
    categoria: str = Field(..., description="Categoría del beneficio")

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Beneficio Sustentable A",
                "descripcion": "Este es un beneficio enfocado en energías renovables.",
                "valor": 1000.0,
                "activo": True,
                "categoria": "Energía"
            }
        }

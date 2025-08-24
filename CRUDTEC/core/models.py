from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Producto:
    id: Optional[int] = None
    codigo: str = ""
    nombre: str = ""
    precio_compra: float = 0.0
    precio_venta: float = 0.0
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None
    
    def margen(self) -> float:
        if self.precio_compra == 0:
            return 0
        return ((self.precio_venta - self.precio_compra) / self.precio_compra) * 100
    
    def margen_absoluto(self) -> float:
        return self.precio_venta - self.precio_compra
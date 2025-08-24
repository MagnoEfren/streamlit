import sqlite3
import os
from typing import List, Optional
from datetime import datetime
from core.models import Producto

class ProductoRepository:
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def init_db(self):
        if not os.path.exists(self.db_path):
            open(self.db_path, 'a').close()
            
        with self.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT UNIQUE NOT NULL,
                    nombre TEXT NOT NULL,
                    precio_compra REAL NOT NULL CHECK(precio_compra >= 0),
                    precio_venta REAL NOT NULL CHECK(precio_venta >= precio_compra),
                    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    
    def crear(self, producto: Producto) -> int:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO productos (codigo, nombre, precio_compra, precio_venta) VALUES (?, ?, ?, ?)",
                (producto.codigo, producto.nombre, producto.precio_compra, producto.precio_venta)
            )
            conn.commit()
            return cursor.lastrowid
    
    def obtener_todos(self) -> List[Producto]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos ORDER BY actualizado_en DESC")
            rows = cursor.fetchall()
            return [self._row_to_producto(row) for row in rows]
    
    def obtener_por_id(self, id: int) -> Optional[Producto]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
            row = cursor.fetchone()
            return self._row_to_producto(row) if row else None
    
    def obtener_por_codigo(self, codigo: str) -> Optional[Producto]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
            row = cursor.fetchone()
            return self._row_to_producto(row) if row else None
    
    def buscar(self, termino: str) -> List[Producto]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM productos WHERE nombre LIKE ? OR codigo LIKE ? ORDER BY nombre",
                (f"{termino}%", f"{termino}%")
            )
            rows = cursor.fetchall()
            return [self._row_to_producto(row) for row in rows]
    
    def filtrar_por_precio(self, min_compra: float = None, max_compra: float = None, 
                          min_venta: float = None, max_venta: float = None,
                          min_margen: float = None, max_margen: float = None) -> List[Producto]:
        query = "SELECT * FROM productos WHERE 1=1"
        params = []
        
        if min_compra is not None:
            query += " AND precio_compra >= ?"
            params.append(min_compra)
        
        if max_compra is not None:
            query += " AND precio_compra <= ?"
            params.append(max_compra)
        
        if min_venta is not None:
            query += " AND precio_venta >= ?"
            params.append(min_venta)
        
        if max_venta is not None:
            query += " AND precio_venta <= ?"
            params.append(max_venta)
        
        query += " ORDER BY nombre"
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            productos = [self._row_to_producto(row) for row in rows]
            
            # Filtrar por margen si se especifica
            if min_margen is not None or max_margen is not None:
                productos = [
                    p for p in productos 
                    if (min_margen is None or p.margen() >= min_margen) and 
                       (max_margen is not None or p.margen() <= max_margen)
                ]
            
            return productos
    
    def actualizar(self, producto: Producto) -> bool:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE productos SET codigo = ?, nombre = ?, precio_compra = ?, precio_venta = ?, actualizado_en = CURRENT_TIMESTAMP WHERE id = ?",
                (producto.codigo, producto.nombre, producto.precio_compra, producto.precio_venta, producto.id)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    def eliminar(self, id: int) -> bool:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def _row_to_producto(self, row) -> Producto:
        return Producto(
            id=row[0],
            codigo=row[1],
            nombre=row[2],
            precio_compra=row[3],
            precio_venta=row[4],
            creado_en=datetime.fromisoformat(row[5]) if isinstance(row[5], str) else row[5],
            actualizado_en=datetime.fromisoformat(row[6]) if isinstance(row[6], str) else row[6]
        )
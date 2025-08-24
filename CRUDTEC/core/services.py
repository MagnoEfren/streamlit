import pandas as pd
from typing import List, Tuple
from core.models import Producto
from core.repository import ProductoRepository

class ProductoService:
    def __init__(self):
        self.repository = ProductoRepository()
    
    def crear_producto(self, codigo: str, nombre: str, precio_compra: float, precio_venta: float) -> Tuple[bool, str]:
        if precio_compra < 0:
            return False, "El precio de compra no puede ser negativo"
        
        if precio_venta < precio_compra:
            return False, "El precio de venta no puede ser menor al precio de compra"
        
        if self.repository.obtener_por_codigo(codigo):
            return False, "Ya existe un producto con este código"
        
        producto = Producto(codigo=codigo, nombre=nombre, precio_compra=precio_compra, precio_venta=precio_venta)
        self.repository.crear(producto)
        return True, "Producto creado exitosamente"
    
    def obtener_todos(self) -> List[Producto]:
        return self.repository.obtener_todos()
    
    def buscar(self, termino: str) -> List[Producto]:
        return self.repository.buscar(termino)
    
    def filtrar(self, min_compra: float = None, max_compra: float = None, 
                min_venta: float = None, max_venta: float = None,
                min_margen: float = None, max_margen: float = None) -> List[Producto]:
        return self.repository.filtrar_por_precio(min_compra, max_compra, min_venta, max_venta, min_margen, max_margen)
    
    def actualizar_producto(self, id: int, codigo: str, nombre: str, precio_compra: float, precio_venta: float) -> Tuple[bool, str]:
        if precio_compra < 0:
            return False, "El precio de compra no puede ser negativo"
        
        if precio_venta < precio_compra:
            return False, "El precio de venta no puede ser menor al precio de compra"
        
        # Verificar si el código ya existe en otro producto
        producto_existente = self.repository.obtener_por_codigo(codigo)
        if producto_existente and producto_existente.id != id:
            return False, "Ya existe otro producto con este código"
        
        producto = Producto(id=id, codigo=codigo, nombre=nombre, precio_compra=precio_compra, precio_venta=precio_venta)
        success = self.repository.actualizar(producto)
        return success, "Producto actualizado exitosamente" if success else "No se pudo actualizar el producto"
    
    def eliminar_producto(self, id: int) -> Tuple[bool, str]:
        success = self.repository.eliminar(id)
        return success, "Producto eliminado exitosamente" if success else "No se pudo eliminar el producto"
    
    def duplicar_producto(self, id: int) -> Tuple[bool, str]:
        producto = self.repository.obtener_por_id(id)
        if not producto:
            return False, "Producto no encontrado"
        
        # Generar un nuevo código único
        base_codigo = producto.codigo
        nuevo_codigo = base_codigo + "_COPY"
        contador = 1
        
        while self.repository.obtener_por_codigo(nuevo_codigo):
            nuevo_codigo = f"{base_codigo}_COPY{contador}"
            contador += 1
        
        nuevo_producto = Producto(
            codigo=nuevo_codigo,
            nombre=producto.nombre + " (Copia)",
            precio_compra=producto.precio_compra,
            precio_venta=producto.precio_venta
        )
        
        self.repository.crear(nuevo_producto)
        return True, "Producto duplicado exitosamente"
    
    def calcular_kpis(self) -> dict:
        productos = self.obtener_todos()
        if not productos:
            return {
                "total_productos": 0,
                "valor_inventario": 0,
                "margen_promedio": 0,
                "valor_venta_total": 0
            }
        
        total_productos = len(productos)
        valor_inventario = sum(p.precio_compra for p in productos)
        valor_venta_total = sum(p.precio_venta for p in productos)
        margen_promedio = sum(p.margen() for p in productos) / total_productos
        
        return {
            "total_productos": total_productos,
            "valor_inventario": valor_inventario,
            "margen_promedio": margen_promedio,
            "valor_venta_total": valor_venta_total
        }
    
    def exportar_csv(self, productos: List[Producto] = None) -> str:
        if productos is None:
            productos = self.obtener_todos()
        
        data = {
            "Código": [p.codigo for p in productos],
            "Nombre": [p.nombre for p in productos],
            "Precio Compra": [p.precio_compra for p in productos],
            "Precio Venta": [p.precio_venta for p in productos],
            "Margen %": [p.margen() for p in productos],
            "Creado": [p.creado_en.strftime("%Y-%m-%d %H:%M") for p in productos],
            "Actualizado": [p.actualizado_en.strftime("%Y-%m-%d %H:%M") for p in productos]
        }
        
        df = pd.DataFrame(data)
        return df.to_csv(index=False)
    
    def exportar_excel(self, productos: List[Producto] = None) -> bytes:
        if productos is None:
            productos = self.obtener_todos()
        
        data = {
            "Código": [p.codigo for p in productos],
            "Nombre": [p.nombre for p in productos],
            "Precio Compra": [p.precio_compra for p in productos],
            "Precio Venta": [p.precio_venta for p in productos],
            "Margen %": [p.margen() for p in productos],
            "Creado": [p.creado_en.strftime("%Y-%m-%d %H:%M") for p in productos],
            "Actualizado": [p.actualizado_en.strftime("%Y-%m-%d %H:%M") for p in productos]
        }
        
        df = pd.DataFrame(data)
        return df.to_excel(index=False)
    
    def importar_csv(self, csv_data: str) -> Tuple[int, int, list]:
        try:
            df = pd.read_csv(csv_data)
            required_columns = ["Código", "Nombre", "Precio Compra", "Precio Venta"]
            
            for col in required_columns:
                if col not in df.columns:
                    return 0, 0, [f"Falta la columna requerida: {col}"]
            
            success_count = 0
            error_count = 0
            errors = []
            
            for index, row in df.iterrows():
                try:
                    codigo = str(row["Código"]).strip()
                    nombre = str(row["Nombre"]).strip()
                    precio_compra = float(row["Precio Compra"])
                    precio_venta = float(row["Precio Venta"])
                    
                    if precio_compra < 0 or precio_venta < precio_compra:
                        error_count += 1
                        errors.append(f"Fila {index+1}: Precios inválidos")
                        continue
                    
                    # Verificar si el código ya existe
                    if self.repository.obtener_por_codigo(codigo):
                        error_count += 1
                        errors.append(f"Fila {index+1}: El código {codigo} ya existe")
                        continue
                    
                    producto = Producto(
                        codigo=codigo,
                        nombre=nombre,
                        precio_compra=precio_compra,
                        precio_venta=precio_venta
                    )
                    
                    self.repository.crear(producto)
                    success_count += 1
                    
                except Exception as e:
                    error_count += 1
                    errors.append(f"Fila {index+1}: Error - {str(e)}")
            
            return success_count, error_count, errors
            
        except Exception as e:
            return 0, 0, [f"Error al procesar el archivo: {str(e)}"]
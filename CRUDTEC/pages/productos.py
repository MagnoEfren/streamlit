import streamlit as st
from core.services import ProductoService
from ui.components import formulario_producto, tabla_productos, mostrar_toast
from ui.layout import mostrar_encabezado, barra_lateral, inicializar_estado
from ui.styles import aplicar_estilos

def main():
    # Configuración de página
    st.set_page_config(
        page_title="Gestion de Productos",
        page_icon="📱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Aplicar estilos
    aplicar_estilos()    
    # Inicializar servicio
    servicio = ProductoService()    
    # Inicializar estado de la sesión
    inicializar_estado()   
    # Mostrar encabezado
    mostrar_encabezado()    
    # Barra lateral
    barra_lateral(servicio)
    
    # Contenido principal
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 📦 Lista de Productos")
    
    with col2:
        if st.button("➕ Nuevo Producto", use_container_width=True):
            st.session_state.editando_producto = "nuevo"
            st.rerun()
    
    # Manejar edición de producto
    if st.session_state.editando_producto:
        if st.session_state.editando_producto == "nuevo":
            st.markdown("### 🆕 Crear Nuevo Producto")
            success, mensaje = formulario_producto(servicio=servicio)
            if success:
                st.session_state.editando_producto = None
                st.rerun()
        else:
            producto = servicio.repository.obtener_por_id(st.session_state.editando_producto)
            if producto:
                st.markdown(f"### ✏️ Editando: {producto.nombre}")
                success, mensaje = formulario_producto(producto, servicio)
                if success:
                    st.session_state.editando_producto = None
                    st.rerun()
            else:
                st.error("Producto no encontrado")
                st.session_state.editando_producto = None
    
    # Manejar eliminación de producto
    if st.session_state.eliminando_producto:
        producto = servicio.repository.obtener_por_id(st.session_state.eliminando_producto)
        if producto:
            st.warning(f"¿Estás seguro de que deseas eliminar el producto '{producto.nombre}'?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Confirmar Eliminación"):
                    success, mensaje = servicio.eliminar_producto(producto.id)
                    mostrar_toast(mensaje, "success" if success else "error")
                    st.session_state.eliminando_producto = None
                    st.rerun()
            with col2:
                if st.button("❌ Cancelar"):
                    st.session_state.eliminando_producto = None
                    st.rerun()
        else:
            st.error("Producto no encontrado")
            st.session_state.eliminando_producto = None
    
    # Obtener y mostrar productos
    if st.session_state.termino_busqueda:
        productos = servicio.buscar(st.session_state.termino_busqueda)
    elif st.session_state.filtros_activos and "filtros" in st.session_state:
        filtros = st.session_state.filtros
        productos = servicio.filtrar(
            min_compra=filtros.get("min_compra"),
            max_compra=filtros.get("max_compra"),
            min_venta=filtros.get("min_venta"),
            max_venta=filtros.get("max_venta"),
            min_margen=filtros.get("min_margen"),
            max_margen=filtros.get("max_margen")
        )
    else:
        productos = servicio.obtener_todos()
    
    # Mostrar tabla de productos
    tabla_productos(productos, servicio, st.session_state.pagina)

if __name__ == "__main__":
    main()
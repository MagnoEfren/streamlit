import streamlit as st

def mostrar_encabezado():
    st.markdown("""
    <div class='main-header'>
        <h1 style='margin:0; color:white;'> Gestión de Productos Tecnológicos</h1>
        <p style='margin:0; color:rgba(255,255,255,0.8);'>Sistema CRUD completo para gestión de inventario</p>
    </div>
    """, unsafe_allow_html=True)

def inicializar_estado():
    if "pagina" not in st.session_state:
        st.session_state.pagina = 1
    
    if "termino_busqueda" not in st.session_state:
        st.session_state.termino_busqueda = ""
    
    if "filtros_activos" not in st.session_state:
        st.session_state.filtros_activos = False
    
    if "editando_producto" not in st.session_state:
        st.session_state.editando_producto = None
    
    if "eliminando_producto" not in st.session_state:
        st.session_state.eliminando_producto = None

def barra_lateral(servicio):
    with st.sidebar:
 
        st.markdown("""
            <div class='sidebar-header'>
                <h2 style='margin:0; color:white;'> Menú Principal</h2>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("---")
        # Opciones de menú con estilo mejorado
 
        st.page_link("main.py", label="Inicio", icon="🏠")
 
        st.page_link("pages/productos.py", label="Productos", icon="📦")
 
        st.page_link("pages/metricas.py", label="Métricas", icon="📊")
 
        st.page_link("pages/importar_exportar.py", label="Importar/Exportar", icon="📤")
  
        
        st.markdown("---")
        
        termino = st.text_input("Buscar por código o nombre", value=st.session_state.termino_busqueda,
                               placeholder="Escribe para buscar...")
        
        if termino != st.session_state.termino_busqueda:
            st.session_state.termino_busqueda = termino
            st.session_state.pagina = 1
            st.rerun()


        st.markdown("### Filtros")
        with st.expander("Filtros de precios y margen", expanded=st.session_state.filtros_activos):
            min_compra = st.number_input("Precio compra mínimo", min_value=0.0, value=0.0, step=10.0)
            max_compra = st.number_input("Precio compra máximo", min_value=0.0, value=0.0, step=10.0)
            
            min_venta = st.number_input("Precio venta mínimo", min_value=0.0, value=0.0, step=10.0)
            max_venta = st.number_input("Precio venta máximo", min_value=0.0, value=0.0, step=10.0)
            
            min_margen = st.number_input("Margen mínimo %", min_value=0.0, value=0.0, step=5.0)
            max_margen = st.number_input("Margen máximo %", min_value=0.0, value=0.0, step=5.0)
            
            aplicar_filtros = st.button("Aplicar Filtros")
            limpiar_filtros = st.button("Limpiar Filtros")
            
            if aplicar_filtros:
                st.session_state.filtros = {
                    "min_compra": min_compra if min_compra > 0 else None,
                    "max_compra": max_compra if max_compra > 0 else None,
                    "min_venta": min_venta if min_venta > 0 else None,
                    "max_venta": max_venta if max_venta > 0 else None,
                    "min_margen": min_margen if min_margen > 0 else None,
                    "max_margen": max_margen if max_margen > 0 else None
                }
                st.session_state.filtros_activos = any(st.session_state.filtros.values())
                st.session_state.pagina = 1
                st.rerun()
            
            if limpiar_filtros:
                if "filtros" in st.session_state:
                    del st.session_state.filtros
                st.session_state.filtros_activos = False
                st.rerun()
        st.markdown("---")
        st.markdown("### KPIs")
        kpis = servicio.calcular_kpis()
        st.metric("Total Productos", kpis['total_productos'])
        st.metric("Valor Inventario", f"S/.{kpis['valor_inventario']:,.2f}")
        st.metric("Margen Promedio", f"{kpis['margen_promedio']:.1f}%")
        
 
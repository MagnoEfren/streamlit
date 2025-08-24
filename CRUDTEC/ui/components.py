import streamlit as st
from core.models import Producto
from core.services import ProductoService

def mostrar_toast(mensaje: str, tipo: str = "success"):
    if tipo == "success":
        st.toast(mensaje, icon="✅")
    elif tipo == "error":
        st.toast(mensaje, icon="❌")
    elif tipo == "warning":
        st.toast(mensaje, icon="⚠️")
    else:
        st.toast(mensaje)

def formulario_producto(producto: Producto = None, servicio: ProductoService = None):
    with st.form(key="producto_form", clear_on_submit=producto is None):
        col1, col2 = st.columns(2)
        
        with col1:
            codigo = st.text_input("Código *", value=producto.codigo if producto else "", 
                                  help="Código único del producto")
            nombre = st.text_input("Nombre *", value=producto.nombre if producto else "",
                                  help="Nombre del producto")
        
        with col2:
            precio_compra = st.number_input("Precio de Compra *", min_value=0.0, step=0.01,
                                          value=float(producto.precio_compra) if producto else 0.0,
                                          help="Precio al que se compró el producto")
            precio_venta = st.number_input("Precio de Venta *", min_value=0.0, step=0.01,
                                         value=float(producto.precio_venta) if producto else 0.0,
                                         help="Precio al que se venderá el producto")
        
        submitted = st.form_submit_button("💾 Guardar Producto" if producto else "➕ Crear Producto")
        
        if submitted:
            if not codigo or not nombre:
                mostrar_toast("Por favor, complete todos los campos obligatorios", "error")
                return False, "Campos incompletos"
            
            if precio_venta < precio_compra:
                mostrar_toast("El precio de venta no puede ser menor al precio de compra", "error")
                return False, "Precios inválidos"
            
            if producto:
                # Modo edición
                success, mensaje = servicio.actualizar_producto(
                    producto.id, codigo, nombre, precio_compra, precio_venta
                )
            else:
                # Modo creación
                success, mensaje = servicio.crear_producto(codigo, nombre, precio_compra, precio_venta)
            
            mostrar_toast(mensaje, "success" if success else "error")
            return success, mensaje
        
        return False, "Formulario no enviado"

def tabla_productos(productos: list, servicio: ProductoService, pagina: int = 1, por_pagina: int = 10):
    if not productos:
        st.info("No hay productos para mostrar")
        return
    
    total_paginas = (len(productos) + por_pagina - 1) // por_pagina
    inicio = (pagina - 1) * por_pagina
    fin = inicio + por_pagina
    productos_pagina = productos[inicio:fin]
    
    # Crear datos para la tabla
    datos = []
    for p in productos_pagina:
        datos.append({
            "ID": p.id,
            "Código": p.codigo,
            "Nombre": p.nombre,
            "Compra": f"S/.{p.precio_compra:.2f}",
            "Venta": f"S/.{p.precio_venta:.2f}",
            "Margen": f"{p.margen():.1f}%",
            "Creado": p.creado_en.strftime("%Y-%m-%d") if p.creado_en else "",
            "Acciones": p.id
        })
    
    # Mostrar tabla
    col_config = {
        "ID": st.column_config.NumberColumn("ID", width="small"),
        "Código": st.column_config.TextColumn("Código", width="medium"),
        "Nombre": st.column_config.TextColumn("Nombre", width="large"),
        "Compra": st.column_config.TextColumn("Precio Compra", width="small"),
        "Venta": st.column_config.TextColumn("Precio Venta", width="small"),
        "Margen": st.column_config.TextColumn("Margen %", width="small"),
        "Creado": st.column_config.TextColumn("Creado", width="small"),
        "Acciones": st.column_config.Column("Acciones", width="medium")
    }
    
    tabla = st.dataframe(
        datos,
        column_config=col_config,
        use_container_width=True,
        hide_index=True
    )
    
    # Controles de paginación
    if total_paginas > 1:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"<div class='pagination'>", unsafe_allow_html=True)
            col21, col22, col23, col24, col25 = st.columns(5)
            
            with col21:
                if st.button("⏮️", key="first_page", disabled=pagina == 1):
                    st.session_state.pagina = 1
                    st.rerun()
            
            with col22:
                if st.button("◀️", key="prev_page", disabled=pagina == 1):
                    st.session_state.pagina = pagina - 1
                    st.rerun()
            
            with col23:
                st.markdown(f"**{pagina} / {total_paginas}**")
            
            with col24:
                if st.button("▶️", key="next_page", disabled=pagina == total_paginas):
                    st.session_state.pagina = pagina + 1
                    st.rerun()
            
            with col25:
                if st.button("⏭️", key="last_page", disabled=pagina == total_paginas):
                    st.session_state.pagina = total_paginas
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Botones de acción para cada producto
    for producto in productos_pagina:
        with st.expander(f"Acciones para {producto.nombre}", expanded=False):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("✏️ Editar", key=f"edit_{producto.id}"):
                    st.session_state.editando_producto = producto.id
                    st.rerun()
            
            with col2:
                if st.button("❌ Eliminar", key=f"delete_{producto.id}"):
                    st.session_state.eliminando_producto = producto.id
                    st.rerun()
            
            with col3:
                if st.button("📋 Duplicar", key=f"duplicate_{producto.id}"):
                    success, mensaje = servicio.duplicar_producto(producto.id)
                    mostrar_toast(mensaje, "success" if success else "error")
                    if success:
                        st.rerun()

def mostrar_kpis(servicio: ProductoService):
    kpis = servicio.calcular_kpis()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>{kpis['total_productos']}</div>
            <div class='metric-label'>Total Productos</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>S/.{kpis['valor_inventario']:,.2f}</div>
            <div class='metric-label'>Valor Inventario</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>S/.{kpis['valor_venta_total']:,.2f}</div>
            <div class='metric-label'>Valor Venta Total</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>{kpis['margen_promedio']:.1f}%</div>
            <div class='metric-label'>Margen Promedio</div>
        </div>
        """, unsafe_allow_html=True)
import streamlit as st
import plotly.express as px
import pandas as pd
from core.services import ProductoService
from ui.styles import aplicar_estilos
from ui.layout import mostrar_encabezado, barra_lateral, inicializar_estado

def main():
    st.set_page_config(
        page_title="Gestion de Productos",
        page_icon="📱",
        layout="wide"
    )
    
    aplicar_estilos()
    mostrar_encabezado()
    inicializar_estado() 
    servicio = ProductoService()
    
    # Barra lateral
    barra_lateral(servicio)

    productos = servicio.obtener_todos()
    
    if not productos:
        st.info("No hay productos para mostrar métricas")
        return
    
    # Preparar datos para visualización
    datos = []
    for p in productos:
        datos.append({
            "Nombre": p.nombre,
            "Código": p.codigo,
            "Precio Compra": p.precio_compra,
            "Precio Venta": p.precio_venta,
            "Margen %": p.margen(),
            "Margen Absoluto": p.margen_absoluto()
        })
    
    df = pd.DataFrame(datos)
    
    # KPIs
    st.markdown("### 📊 Métricas Principales")
    
    kpis = servicio.calcular_kpis()
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Productos", kpis['total_productos'])
    
    with col2:
        st.metric("Valor Inventario", f"S/.{kpis['valor_inventario']:,.2f}")
    
    with col3:
        st.metric("Valor Venta Total", f"S/.{kpis['valor_venta_total']:,.2f}")
    
    with col4:
        st.metric("Margen Promedio", f"{kpis['margen_promedio']:.1f}%")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Distribución de Precios de Compra")
        fig_compra = px.histogram(df, x="Precio Compra", nbins=20, 
                                 color_discrete_sequence=["#50dde6"])
        fig_compra.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                               font_color="white")
        st.plotly_chart(fig_compra, use_container_width=True)
    
    with col2:
        st.markdown("#### 📈 Distribución de Margen de Ganancia")
        fig_margen = px.histogram(df, x="Margen %", nbins=20,
                                 color_discrete_sequence=["#4252ae"])
        fig_margen.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                               font_color="white")
        st.plotly_chart(fig_margen, use_container_width=True)
    
    # Top productos por margen
    st.markdown("#### 🏆 Top Productos por Margen de Ganancia")
    top_margen = df.nlargest(10, "Margen %")
    fig_top = px.bar(top_margen, x="Nombre", y="Margen %", 
                    color="Margen %", color_continuous_scale="Viridis")
    fig_top.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                         font_color="white", xaxis_tickangle=-45)
    st.plotly_chart(fig_top, use_container_width=True)
    
    # Relación entre precio compra y venta
    st.markdown("#### 🔗 Relación entre Precio de Compra y Venta")
    fig_scatter = px.scatter(df, x="Precio Compra", y="Precio Venta", 
                            hover_data=["Nombre"], trendline="ols",
                            color_discrete_sequence=["#9f5874"])
    fig_scatter.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                            font_color="white")
    st.plotly_chart(fig_scatter, use_container_width=True)

if __name__ == "__main__":
    main()
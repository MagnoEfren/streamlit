import streamlit as st
from ui.styles import aplicar_estilos
from ui.layout import mostrar_encabezado, barra_lateral,inicializar_estado
from core.services import ProductoService

# Configuración de la aplicación principal
st.set_page_config(
    page_title="Gestion de Productos",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar estilos personalizados
aplicar_estilos()

inicializar_estado()
# Mostrar encabezado
mostrar_encabezado()

servicio = ProductoService()
barra_lateral(servicio)
kpis = servicio.calcular_kpis()

# Página de inicio con descripción
st.markdown("""
<div class='card'>
    <h2>🚀 Bienvenido al Sistema de Gestión de Productos Tecnológicos</h2>
    <p>Esta aplicación te permite gestionar tu inventario de productos tecnológicos con todas las funcionalidades CRUD:</p>
    <ul>
        <li><strong>📦 Productos</strong>: Crear, visualizar, editar y eliminar productos</li>
        <li><strong>📊 Métricas</strong>: Ver KPIs y gráficos de tu inventario</li>
        <li><strong>📤 Importar/Exportar</strong>: Cargar y descargar datos en formatos CSV y Excel</li>
    </ul>
    <p>Utiliza el menú lateral para navegar entre las diferentes secciones de la aplicación.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📊 Resumen General")
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

# Información de la aplicación
st.markdown("---")
st.markdown("""
<div class='card'>
    <h3>ℹ️ Acerca de esta aplicación</h3>
    <p>Esta es una aplicación de escritorio desarrollada con:</p>
    <ul>
        <li><strong>Python</strong>: Lenguaje de programación backend</li>
        <li><strong>Streamlit</strong>: Framework para la interfaz de usuario</li>
        <li><strong>SQLite</strong>: Base de datos local para almacenamiento</li>
        <li><strong>Pandas</strong>: Procesamiento y análisis de datos</li>
    </ul>
    <p>La aplicación incluye todas las funcionalidades CRUD, búsqueda incremental, filtros avanzados, 
    importación/exportación de datos y un dashboard de métricas.</p>
</div>
""", unsafe_allow_html=True)
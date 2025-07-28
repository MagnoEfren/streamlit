# Patreon:
# patreon.com/magnoefren

# GitHub:
# github.com/MagnoEfren

# YouTube:
# https://www.youtube.com/@MagnoEfren

import streamlit as st
from utils.config import load_config, save_config
from utils.styles import apply_custom_css, create_theme_toggle
from components.protect import protect_pdf_component
from components.compress import compress_pdf_component
from components.settings import settings_component

# Configuración de la página
st.set_page_config(
    page_title="PDF Tools",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    # Inicializar estado de sesión con configuración persistente
    if 'config' not in st.session_state:
        st.session_state.config = load_config()
    
    # Tu lógica de configuración existente
    current_theme = st.session_state.config.get('theme', 'light')
    primary_color = st.session_state.config.get('primary_color', '#00CED1')
    
    # Aplicar CSS
    apply_custom_css(current_theme, primary_color)
 
    create_theme_toggle(current_theme, primary_color, st.session_state.config, save_config)
 
    # Encabezado principal
    st.markdown("""
    <div class="main-header">
        <h1>📄 PDF Tools</h1>
        <p>Suite completa de herramientas para procesamiento de archivos PDF</p>
    </div>
    """, unsafe_allow_html=True)

    # Pestañas principales
    tabs = st.tabs([
        "🔐 Proteger PDF",
        "📦 Comprimir PDF", 
        "⚙️ Configuración"
    ])

    # Componentes de cada pestaña
    with tabs[0]:
        protect_pdf_component()
    with tabs[1]:
        compress_pdf_component()
    with tabs[2]:
        settings_component()

    # Footer
    st.markdown("""
    ---
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>© 2025 PDF Tools - Desarrollado con ❤️ usando Streamlit</p>
        <p>Todas las operaciones se realizan localmente en tu navegador para máxima seguridad</p>
    </div>
    """, unsafe_allow_html=True)

    # Instrucciones de uso
    if st.sidebar.button("ℹ️ Ayuda"):
        st.sidebar.markdown("""
        ## 📋 Instrucciones de Uso
        
        ### 🔐 Proteger PDF
        1. Sube tu archivo PDF
        2. Ingresa una contraseña segura
        3. Haz clic en "Proteger PDF"
        4. Descarga el archivo protegido
        
        ### 📦 Comprimir PDF
        1. Sube tu archivo PDF
        2. Haz clic en "Comprimir PDF"
        3. El sistema optimizará automáticamente
        4. Descarga el archivo comprimido
 
        ### ⚙️ Configuración
        - Cambia el color principal
        - Alterna entre tema claro/oscuro
        - Restablece configuraciones
        - Consulta información de la app
        """)

if __name__ == "__main__":
    main()
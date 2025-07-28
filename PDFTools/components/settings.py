import streamlit as st
from utils.config import save_config
from utils.ui import show_success

def settings_component():
    st.markdown('<div class="tool-card">', unsafe_allow_html=True)
    st.subheader("⚙️ Configuración")
    st.write("Personaliza la apariencia de la aplicación.")
    st.write("### Color Principal")
    color_presets = {
        "Aqua": "#00CED1",
        "Púrpura": "#6F42C1",
        "Naranja": "#FD7E14",
        "Rojo": "#DC3545",
        "Rosa": "#E91E63",
        "Índigo": "#6610F2",
        "Turquesa": "#20C997",
    }
    col1, col2 = st.columns(2)
    with col1:
        selected_preset = st.selectbox(
            "Colores predefinidos:",
            list(color_presets.keys()),
            index=0
        )
        if st.button("Aplicar Color Predefinido"):
            st.session_state.config['primary_color'] = color_presets[selected_preset]
            save_config(st.session_state.config)
            show_success("Color aplicado exitosamente!")
            st.rerun()
    with col2:
        custom_color = st.color_picker(
            "O selecciona un color personalizado:",
            value=st.session_state.config.get('primary_color', '#00CED1')
        )
        if st.button("Aplicar Color Personalizado"):
            st.session_state.config['primary_color'] = custom_color
            save_config(st.session_state.config)
            show_success("Color personalizado aplicado exitosamente!")
            st.rerun()
    st.write("### Tema Actual")
    theme_info = "Oscuro" if st.session_state.config.get('theme', 'light') == 'dark' else "Claro"
    st.write(f"**Tema:** {theme_info}")
    st.write(f"**Color Principal:** {st.session_state.config.get('primary_color', '#00CED1')}")
    st.write("### Restablecer Configuración")
    if st.button("Restablecer a Valores por Defecto", type="secondary"):
        st.session_state.config = {'theme': 'light', 'primary_color': '#00CED1'}
        save_config(st.session_state.config)
        show_success("Configuración restablecida exitosamente!")
        st.rerun()
    st.write("### Información de la Aplicación")
    st.info("""
    **PDF Tools v1.0**
    
    Esta aplicación ofrece una suite completa de herramientas para el procesamiento de archivos PDF:
    
    - **Proteger PDF**: Añade contraseñas para proteger documentos
    - **Comprimir PDF**: Reduce el tamaño de archivos manteniendo la calidad
    - Obten  codigo completo uniendote a Patreon:  patreon.com/magnoefren
    
    **Características:**
    - Interfaz moderna y responsiva
    - Modo claro y oscuro
    - Colores personalizables
    - Procesamiento local seguro
    - Descarga directa de archivos procesados
    """)
    st.write("### Requisitos del Sistema")
    st.warning("""
    **Librerías Python requeridas:**
    ```
    pip install streamlit PyPDF2 pymupdf pillow reportlab
    ```
    """)
    st.markdown('</div>', unsafe_allow_html=True)
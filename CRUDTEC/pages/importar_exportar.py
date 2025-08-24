import streamlit as st
import pandas as pd
from io import StringIO, BytesIO
from core.services import ProductoService
from ui.styles import aplicar_estilos
from ui.layout import mostrar_encabezado, barra_lateral,inicializar_estado
from ui.components import mostrar_toast

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
    barra_lateral(servicio)

    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📤 Exportar Productos")
        
        formato = st.radio("Formato de exportación", ["CSV", "Excel"], horizontal=True)
        
        if st.button("Exportar Todos los Productos"):
            try:
                if formato == "CSV":
                    csv_data = servicio.exportar_csv()
                    st.download_button(
                        label="Descargar CSV",
                        data=csv_data,
                        file_name="productos.csv",
                        mime="text/csv"
                    )
                else:
                    excel_data = servicio.exportar_excel()
                    st.download_button(
                        label="Descargar Excel",
                        data=excel_data,
                        file_name="productos.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                
                mostrar_toast("Datos exportados correctamente", "success")
            except Exception as e:
                mostrar_toast(f"Error al exportar: {str(e)}", "error")
    
    with col2:
        st.markdown("### 📥 Importar Productos")
        
        archivo = st.file_uploader("Seleccionar archivo", type=["csv", "xlsx"])
        
        if archivo:
            try:
                if archivo.name.endswith('.csv'):
                    df = pd.read_csv(archivo)
                else:
                    df = pd.read_excel(archivo)
                
                st.markdown("#### Vista previa de datos")
                st.dataframe(df.head(), use_container_width=True)
                
                if st.button("Importar Datos"):
                    if archivo.name.endswith('.csv'):
                        csv_str = StringIO(archivo.getvalue().decode("utf-8"))
                        success, error, errores = servicio.importar_csv(csv_str)
                    else:
                        # Convertir Excel a CSV para importar
                        csv_buffer = StringIO()
                        df.to_csv(csv_buffer, index=False)
                        success, error, errores = servicio.importar_csv(csv_buffer.getvalue())
                    
                    if success > 0:
                        mostrar_toast(f"Importados {success} productos correctamente", "success")
                    
                    if error > 0:
                        st.error(f"Errores en {error} productos:")
                        for err in errores:
                            st.error(err)
                    
                    st.rerun()
            
            except Exception as e:
                mostrar_toast(f"Error al procesar el archivo: {str(e)}", "error")
    
    # Plantilla de importación
    st.markdown("---")
    st.markdown("### 📋 Plantilla de Importación")
    
    st.info("""
    Para importar productos, utiliza un archivo CSV o Excel con las siguientes columnas:
    - **Código**: Código único del producto (texto)
    - **Nombre**: Nombre del producto (texto)
    - **Precio Compra**: Precio de compra (número, debe ser ≥ 0)
    - **Precio Venta**: Precio de venta (número, debe ser ≥ Precio Compra)
    """)
    
    # Crear y ofrecer plantilla de ejemplo
    datos_ejemplo = {
        "Código": ["MON001", "TEC002", "CPU003"],
        "Nombre": ["Monitor 24\"", "Teclado Mecánico", "CPU Intel i7"],
        "Precio Compra": [150.00, 45.00, 300.00],
        "Precio Venta": [220.00, 65.00, 450.00]
    }
    
    df_ejemplo = pd.DataFrame(datos_ejemplo)
    
    col1, col2 = st.columns(2)
    
    with col1:
        csv_ejemplo = df_ejemplo.to_csv(index=False)
        st.download_button(
            label="Descargar Plantilla CSV",
            data=csv_ejemplo,
            file_name="plantilla_productos.csv",
            mime="text/csv"
        )
    
    with col2:
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df_ejemplo.to_excel(writer, index=False, sheet_name='Productos')
        excel_data = excel_buffer.getvalue()
        
        st.download_button(
            label="Descargar Plantilla Excel",
            data=excel_data,
            file_name="plantilla_productos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()
import streamlit as st
from pdf_operations.compress import compress_pdf
from utils.ui import show_success, show_error, create_download_link

def compress_pdf_component():
    st.markdown('<div class="tool-card">', unsafe_allow_html=True)
    st.subheader("📦 Comprimir PDF")
    st.write("Reduce el tamaño de tu archivo PDF manteniendo la calidad.")
    uploaded_file = st.file_uploader("Selecciona un archivo PDF para comprimir", type="pdf", key="compress_pdf")
    if st.button("Comprimir PDF", key="compress_btn"):
        if uploaded_file:
            with st.spinner("Comprimiendo PDF..."):
                compressed_pdf = compress_pdf(uploaded_file)
                if compressed_pdf:
                    original_size = len(uploaded_file.getvalue())
                    compressed_size = len(compressed_pdf)
                    reduction = ((original_size - compressed_size) / original_size) * 100
                    show_success(f"PDF comprimido exitosamente! Reducción: {reduction:.1f}%")
                    st.markdown(create_download_link(compressed_pdf, "documento_comprimido.pdf"), unsafe_allow_html=True)
        else:
            show_error("Por favor, selecciona un archivo PDF.")
    st.markdown('</div>', unsafe_allow_html=True)
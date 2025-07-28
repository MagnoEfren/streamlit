import streamlit as st
from pdf_operations.protect import protect_pdf
from utils.ui import show_success, show_error, create_download_link

def protect_pdf_component():
    st.markdown('<div class="tool-card">', unsafe_allow_html=True)
    st.subheader("🔐 Proteger PDF con Contraseña")
    st.write("Añade una contraseña para proteger tu documento PDF.")
    uploaded_file = st.file_uploader("Arrastra y suelta el archivo aquí (Límite: 200MB por archivo • PDF)", type="pdf", key="protect_pdf")
    password = st.text_input("Contraseña", type="password", key="protect_password")
    if st.button("Proteger PDF", key="protect_btn"):
        if uploaded_file and password:
            with st.spinner("Protegiendo PDF..."):
                protected_pdf = protect_pdf(uploaded_file, password)
                if protected_pdf:
                    show_success("PDF protegido exitosamente!")
                    st.markdown(create_download_link(protected_pdf, "documento_protegido.pdf"), unsafe_allow_html=True)
        else:
            show_error("Por favor, selecciona un archivo PDF y establece una contraseña.")
    st.markdown('</div>', unsafe_allow_html=True)
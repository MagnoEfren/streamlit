import streamlit as st
import base64

def show_success(message):
    st.markdown(f'<div class="success-message">✅ {message}</div>', unsafe_allow_html=True)

def show_error(message):
    st.markdown(f'<div class="error-message">❌ {message}</div>', unsafe_allow_html=True)

def create_download_link(file_data, filename, text="Descargar archivo"):
    b64 = base64.b64encode(file_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}" style="text-decoration: none; color: white; background: linear-gradient(135deg, {st.session_state.config.get("primary_color", "#00CED1")}, {st.session_state.config.get("primary_color", "#00CED1")}DD); padding: 10px 20px; border-radius: 8px; font-weight: 600; display: inline-block; margin: 10px 0;">{text}</a>'
    return href


import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

# Personalizar 


st.markdown("""
        <style>
            .stApp {
            background: linear-gradient(135deg, #141e30, #243b55);
            font-family: 'Segoe UI', sans-serif;
            color: white;
        }
        
        .card{
            background: linear-gradient(135deg, #2b5876, #4e4376);
            padding: 18px;
            border-radius: 15px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.4);
            margin-bottom: 15px;
            color: white;
            }
            

        </style>         

""", unsafe_allow_html= True)


## título 

st.title("Dashboard- Widgets")
st.write("Ejemplo práctico de cómoorganizar y personalizar widgets en un layout")

# columnas

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class ='card'><h4> 📝 Texto<h4>", unsafe_allow_html=True)
    nombre = st.text_input("Nombre")
    comentario = st.text_area("Comentario: ")
    clave = st.text_input("Contraseña: ", type="password")
    st.markdown("</div>", unsafe_allow_html=True)


with col2: 
    st.markdown("<div class ='card'><h4> ✅ Selección<h4>", unsafe_allow_html=True)
    
    opcion = st.selectbox("Selecciona un pais", ["Perú", "Mexico", "Colombia", "Argentina"])
    multi = st.multiselect("Selecciona tus lenguaje: ", ["Python", "Dart", "Rust"])
    check = st.checkbox("Acepto términos y condiciones")
    radio = st.radio("Nivel", ["Basico", "Intermedio", "Avanzado"])
    st.markdown("</div>", unsafe_allow_html=True)  

with col3: 
    st.markdown("<div class ='card'><h4> 📅 Fechas<h4>", unsafe_allow_html=True)
    fecha = st.date_input("Seleccione una fecha")
    tiempo = st.time_input("Seleccione una hora")

    st.markdown("</div>", unsafe_allow_html=True)

# segunda fila 

c1, c2 =  st.columns([1,2])

with c1: 
    st.markdown("<div class ='card'><h4> ⚙️ Sliders<h4>", unsafe_allow_html=True)
    slider1 = st.slider("Nivel de progreso", 0,100,50)
    slider2 = st.slider("Rango de valores", 0, 100, (20,80))
    st.markdown("</div>", unsafe_allow_html=True)


with c2: 
    st.markdown("<div class ='card'><h4> 📂 Subir archivos<h4>", unsafe_allow_html=True)
    archivo = st.file_uploader("Subir archivo", type=["csv", "txt", "jpg"])
    if archivo is not None:
        st.success("Archivo cargado con éxito")

    st.markdown("</div>", unsafe_allow_html=True)

# tercera fila 

st.markdown("<div class ='card'><h4> 💻 Otros Widgets<h4>", unsafe_allow_html=True)

colA, colB, colC = st.columns(3)

with colA:
    st.metric("Usuarios activos", "1245", "+45")
with colB:
    st.metric("Ventas", "S/. 10,000.0", "1%")
with colC:
    st.metric("Clientes nuevos", "87", "+12%")


st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st

def aplicar_estilos():
    st.markdown("""
    <style>
    :root {
        --primary: #50dde6;
        --secondary: #25265d;
        --accent: #4252ae;
        --highlight: #9f5874;
        --dark: #0b0c13;
    }
    
    .stApp {
        background: linear-gradient(135deg, var(--dark) 0%, var(--secondary) 100%);
        color: #ffffff;
    }
    
    .main-header {
        background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .card {
        background: rgba(37, 38, 93, 0.7);
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        border: 1px solid var(--accent);
    }
    
    .metric-card {
        background: linear-gradient(135deg, var(--secondary) 0%, var(--accent) 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: var(--primary);
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.8);
    }
    
    .stButton>button {
        background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(90deg, var(--accent) 0%, var(--highlight) 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid var(--accent);
        border-radius: 8px;
    }
    
    .stDataFrame {
        background: rgba(37, 38, 93, 0.7);
        border-radius: 10px;
        border: 1px solid var(--accent);
    }
    
    .stAlert {
        background: rgba(37, 38, 93, 0.7);
        border: 1px solid var(--accent);
        border-radius: 10px;
    }
    
    .success-toast {
        background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
        color: white;
        border-radius: 10px;
    }
    
    .error-toast {
        background: linear-gradient(90deg, var(--highlight) 0%, #c23b5c 100%);
        color: white;
        border-radius: 10px;
    }
    
    /* Tabla personalizada */
    .dataframe {
        background: rgba(37, 38, 93, 0.7) !important;
        color: white !important;
        border-radius: 10px;
    }
    
    .dataframe th {
        background: var(--accent) !important;
        color: white !important;
    }
    
    .dataframe td {
        background: rgba(37, 38, 93, 0.5) !important;
        color: white !important;
    }
    
    /* Paginación */
    .pagination {
        display: flex;
        justify-content: center;
        margin-top: 1rem;
    }
    
    .pagination button {
        margin: 0 0.25rem;
        background: var(--accent);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.25rem 0.5rem;
    }
    
    .pagination button:hover {
        background: var(--primary);
    }
    
    .pagination button:disabled {
        background: var(--highlight);
        opacity: 0.7;
    }







 
 
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #25265d 0%, #0b0c13 100%);
    }
    [data-testid="stSidebarNav"] {
        display: none;
    }
    .sidebar-header {
        background: linear-gradient(90deg, #50dde6 0%, #4252ae 100%);
        padding: 1rem;
        border-radius: 0 0 10px 10px;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .sidebar-option {
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        transition: all 0.3s ease;
        color: white;
        text-decoration: none;
        display: block;
        font-weight: 500;
    }
    .sidebar-option:hover {
        background: rgba(80, 221, 230, 0.2);
        color: white;
    }
    .sidebar-option.active {
        background: linear-gradient(90deg, #50dde6 0%, #4252ae 100%);
    }

    </style>
    """, unsafe_allow_html=True)
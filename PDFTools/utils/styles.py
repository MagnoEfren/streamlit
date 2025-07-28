import streamlit as st

def apply_custom_css(theme, primary_color):
    """
    Aplica CSS personalizado optimizado con selectores más robustos
    """
    if theme == 'dark':
        bg_color = '#0E1117'
        text_color = '#FAFAFA'
        card_bg = '#262730'
        border_color = '#4F4F4F'
        sidebar_bg = '#0E1117'
        input_bg = '#2D2D2D'
        toggle_bg = '#444444'
        upload_bg = '#333333'
        upload_text = '#FFFFFF'
        info_bg = '#1E3A8A'
        warning_bg = '#92400E'
        success_bg = '#166534'
        error_bg = '#991B1B'
        select_bg = '#2D2D2D'
        select_text = '#FAFAFA'
        dropdown_bg = '#1E1E1E'
        dropdown_hover = '#3D3D3D'
        button_bg = toggle_bg
        button_text = text_color
        button_border = border_color
    else:
        bg_color = '#FFFFFF'
        text_color = '#262730'
        card_bg = '#F8F9FA'
        border_color = '#E0E0E0'
        sidebar_bg = '#FFFFFF'
        input_bg = '#FFFFFF'
        toggle_bg = '#FFFFFF'
        upload_bg = '#F8F9FA'
        upload_text = text_color
        info_bg = '#DBEAFE'
        warning_bg = '#FEF3C7'
        success_bg = '#D1FAE5'
        error_bg = '#FEE2E2'
        select_bg = '#FFFFFF'
        select_text = '#262730'
        dropdown_bg = '#FFFFFF'
        dropdown_hover = '#F0F2F6'
        button_bg = '#FFFFFF'
        button_text = '#262730'
        button_border = '#E0E0E0'
    
    st.markdown(f"""
    <style>
    /* =================== ESTILOS PRINCIPALES =================== */
    .stApp {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
    }}
    
    /* =================== SIDEBAR =================== */
    .css-1d391kg, .css-1544g2n, section[data-testid="stSidebar"] {{
        background-color: {sidebar_bg} !important;
        color: {text_color} !important;
    }}
    
    .css-1d391kg .stMarkdown, .css-1544g2n .stMarkdown {{
        background-color: {sidebar_bg} !important;
        color: {text_color} !important;
    }}
    
    /* =================== HEADERS PERSONALIZADOS =================== */
    .main-header {{
        background: linear-gradient(135deg, {primary_color}20, {primary_color}40);
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        border: 2px solid {primary_color};
    }}

    .main-header h1 {{
        color: {primary_color};
        font-size: 2.5rem;
        font-weight: 200;
        margin: 0;
    }}
    .main-header p {{
        color: {text_color};
        font-size: 1rem;
        margin-top: 0.5rem;
        opacity: 0.8;
    }}
    
    

    /* =================== BOTONES GENERALES =================== */
    .stButton > button {{
        background: linear-gradient(135deg, {primary_color}, {primary_color}FF) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }}
    .stButton > button:hover {{
        background: linear-gradient(135deg, {primary_color}DD, {primary_color}) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5) !important;
    }}
    
    /* =================== SELECTBOX =================== */
    /* Input del selectbox */
    .stSelectbox > div > div {{
        background-color: {select_bg} !important;
        border: 1px solid {border_color} !important;
        border-radius: 8px !important;
        color: {select_text} !important;
    }}
    
    .stSelectbox [data-baseweb="select"] > div {{
        background-color: {select_bg} !important;
        color: {select_text} !important;
    }}
    
    /* Lista desplegable del selectbox */
   
    [data-baseweb="popover"] [role="option"] {{
        color: {select_text} !important;
        background-color: {dropdown_bg} !important;
    }}
    [data-baseweb="popover"] [role="option"]:hover {{
        background-color: {dropdown_hover} !important;
    }}
    
    /* =================== FILE UPLOADER =================== */
  
    .stFileUploader {{
        background-color: {upload_bg} !important;
        border: 2px dashed {primary_color} !important;
        border-radius: 10px !important;
        padding: 1.5rem !important;
    }}
 
    .stFileUploader section {{
        background-color: {upload_bg} !important;
        color: {primary_color} !important;
        border: none !important;
    }}
 
    .stFileUploader section > div {{
        background-color: {upload_bg} !important;
        color: {text_color} !important; 
    }}

    .stFileUploader section > div > div {{
        background-color: {upload_bg} !important;
        color: {text_color} !important; 
    }} 

    .stFileUploader label {{
        color: {text_color} !important;
        
    }}
    
    /* =================== WIDGETS DE INFORMACIÓN =================== */
    .stInfo {{
        background-color: {info_bg} !important;
        border: 1px solid {primary_color} !important;
        border-radius: 8px !important;
        color: {text_color} !important;
    }}
    
    .stWarning {{
        background-color: {warning_bg} !important;
        border: 1px solid #F59E0B !important;
        border-radius: 8px !important;
        color: {text_color} !important;
    }}
    
    .stSuccess {{
        background-color: {success_bg} !important;
        border: 1px solid #10B981 !important;
        border-radius: 8px !important;
        color: {text_color} !important;
    }}
    
    .stError {{
        background-color: {error_bg} !important;
        border: 1px solid #EF4444 !important;
        border-radius: 8px !important;
        color: {text_color} !important;
    }}
    
    /* Forzar color de texto en alertas */
    [data-testid="stAlert"] * {{
        color: {text_color} !important;
    }}
    
    /* =================== TABS =================== */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 4px;
        background-color: {bg_color} !important;
        border-radius: 10px;
        padding: 0.5rem;
        flex-wrap: wrap;
        display: flex;
        justify-content: center;
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: transparent !important;
        border-radius: 8px !important;
        color: {text_color} !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        padding: 0.5rem 1rem !important;
        flex: 1 1 auto;
        min-width: 100px;
        max-width: 150px;
        text-align: center;
        margin: 2px;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: {primary_color} !important;
        color: white !important;
    }}
    
  /* Text inputs */
    .stTextInput > div > div > input {{
        background-color: {input_bg} !important;
        border: 2px solid {primary_color} !important;
        border-radius: 8px !important;
        color: {text_color} !important;
    }}

    .stTextInput >  div > div {{
        background-color: {primary_color} !important;
      
        border-radius: 8px !important;
        color: {text_color} !important;
    }}  

    .stTextInput >  div {{
        background-color: {primary_color} !important;
       
        border-radius: 8px !important;
        color: {text_color} !important;
    }}

    .stTextInput label {{
        color: {text_color} !important;
         
    }}
    
    /* =================== RESPONSIVE DESIGN =================== */
    @media (max-width: 768px) {{
        .main-header h1 {{
            font-size: 1.8rem;
        }}
        .main-header p {{
            font-size: 0.9rem;
        }}
        .tool-card {{
            padding: 1rem;
        }}
        .stTabs [data-baseweb="tab"] {{
            min-width: 100px;
            max-width: 140px;
            font-size: 0.9rem;
            padding: 0.4rem 0.8rem;
        }}
    }}
    @media (max-width: 480px) {{
        .main-header h1 {{
            font-size: 1.5rem;
        }}
        .main-header p {{
            font-size: 0.8rem;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

def create_theme_toggle(current_theme, primary_color, config, save_config_func):
    # Posicionar a la derecha
    col1, col2 = st.columns([10, 1])
    with col2:
        st.markdown(f"""
        <style>
        div[data-testid="column"]:last-child .stButton > button {{
            border-radius: 50% !important;
            width: 50px !important;
            height: 50px !important;
            background-color: {primary_color} !important;
        }}
        </style>
        """, unsafe_allow_html=True)
        
        # Ícono que cambia según el tema
        theme_icon = "🌙" if current_theme == 'light' else "☀️"
        
 
        if st.button(theme_icon, key="theme-toggle-btn"):
            new_theme = 'dark' if current_theme == 'light' else 'light'
            config['theme'] = new_theme
            save_config_func(config)
            st.rerun()
 
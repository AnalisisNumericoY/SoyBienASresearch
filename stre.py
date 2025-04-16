import sys
from pathlib import Path
import os
# Configuración crítica - Añade esto al INICIO de stre.py
BASE_DIR = Path(__file__).parent
sys.path.append(str(BASE_DIR))  # Añade el directorio raíz al path de Python

# Ahora tus imports normales
import streamlit as st

# Configura paths para assets
def asset_path(relative_path):
    return os.path.join(BASE_DIR, 'assets', relative_path)


# --- PAGE SETUP ---
# https://fonts.google.com/icons

about_page = st.Page(
    page="views/about_me.py",
    title="Soy Bien",
    icon=":material/account_circle:",
    default=True,
)
servicio_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Dashboard Soy Bien",
    icon=":material/bar_chart:",
)
servicio_2_page = st.Page(
    page="views/chatbot.py",
    title="Conversa con Soy Bien",
    icon=":material/smart_toy:",
)
proeyecto_1_page = st.Page(
    page="views/P1_BarrioEnvigado.py",
    title="Mi Barrio Envigado",
    icon=":material/smart_toy:",
)
proeyecto_2_page = st.Page(
    page="views/P2_Savia_MeCuida.py",
    title="Savia me cuida",
    icon=":material/smart_toy:",
)
# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page], 
        "Servicios": [servicio_1_page, servicio_2_page],
        "Proyectos": [proeyecto_1_page, proeyecto_2_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("./assets/cropped-cropped-LOGO.png")

# --- RUN NAVIGATION ---
pg.run()

import streamlit as st 

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

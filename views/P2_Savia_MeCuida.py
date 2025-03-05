import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="cargando datos en tiempo real",
    page_icon=None,
    layout="wide", #forma de layout ancho y compacto
    initial_sidebar_state="expanded" #se define si el sidebar aparece expandido o colapsado
)
st.image("./assets/SaviaSalud.png", width=230)
st.subheader("Proyecto Savia cuida mi corazón", anchor=False)





gsheetid='1FLzjH7ns7vXf9U3PZ0JQWQOnFRRW7yUM'
sheetid='1815695682#gid=1815695682'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}'
#st.write(url)
sheetid2='1149992398#gid=1149992398'
url2 = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid2}'
#st.write(url2)
dfDatos1 = pd.read_csv(url)
m, n = dfDatos1.shape
 
st.write(f"Total de personas atendidas en el proyecto: {m:.2f}")

dfDatos2 = pd.read_csv(url2)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Insuficiencia Cardiaca", "Riesgo Cardiovascular", "EPOC","Anticuagulados", "Protección Renal"])

with tab1:
    st.write("Programa Insuficiencia Cardiaca")
    print(dfDatos2)
    st.dataframe(dfDatos2, use_container_width=True)


with tab2:
    st.write("Programa Riesgo Cardiovascular")

with tab3:
    st.write("Programa EPOC")

with tab4:
    st.write("Programa Anticuagulados")

with tab5:
    st.write("Programa Protección Renal")





st.subheader("Programas de EPOC, Anticuagulados, Riesgo Cardiovascular y Protección Renal", anchor=False)
st.write("oprima click aqui para acceder al sitio privado del proyecto")

dfDatos = dfDatos1
print(dfDatos)

st.dataframe(dfDatos, use_container_width=True)
#st.dataframe(dfDatosTotales, use_container_width=True)
# Expander básico


with st.expander("Haz clic sobre el programa que desees consultar"):
    st.write("EPOC.")
    st.write("RCV.")
    st.image("./assets/corazon.jpg", caption="cuida tu corazón")
    st.dataframe({
        "Pacientes": [11, 32, 43],
        "Programa": ["EPOC", "RCV", "OTRO"]})

st.write(
    """
    - Crea formularios
    - Crea formularios
    - Procesa datos
    - Imprime las historias clínicas 
    - tableros de visualización de la información
    """
)

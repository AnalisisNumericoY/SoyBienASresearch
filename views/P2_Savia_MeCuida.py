import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="cargando datos en tiempo real",
    page_icon=None,
    layout="wide", #forma de layout ancho y compacto
    initial_sidebar_state="expanded" #se define si el sidebar aparece expandido o colapsado
)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/SaviaSalud.png", width=230)
with col2:
    st.title("Proyecto Savia cuida mi corazón", anchor=False)
    st.write(
        "Cuidado y bienestar de los riesgos labores y prevención de riesgo cardiovascular"
    )






gsheetid='1FLzjH7ns7vXf9U3PZ0JQWQOnFRRW7yUM'
sheetid='1815695682#gid=1815695682'
url1 = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}'
#st.write(url)
sheetid2='1149992398#gid=1149992398'
url2 = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid2}'
#st.write(url2)
dfDatos1 = pd.read_csv(url1)
m, n = dfDatos1.shape
 
st.write(f"Total de personas atendidas en el proyecto: {m:.2f}")





dfDatos2 = pd.read_csv(url2)


gsheetid_Anticoagulados='1n869pp61pyY9NgH3THKdafIvsCdvQYHJ6n4r05O60u0'
sheetid3='296901355#gid=296901355'
url3 = f'https://docs.google.com/spreadsheets/d/{gsheetid_Anticoagulados}/export?format=csv&gid={sheetid3}'
dfDatos3 = pd.read_csv(url3)


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Insuficiencia Cardiaca", "Riesgo Cardiovascular", "EPOC","Anticoagulados", "Protección Renal"])

with tab1:
    st.write("Programa Insuficiencia Cardiaca")
    print(dfDatos2)
    st.dataframe(dfDatos2, use_container_width=True)


with tab2:
    st.write("Programa Riesgo Cardiovascular")

with tab3:
    st.write("Programa EPOC")

with tab4:
    st.write("Programa Anticoagulados")
    print(dfDatos3)
    st.dataframe(dfDatos3, use_container_width=True)

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

municipios_seleccionados = st.multiselect(
    "Selecciona los municipios de interés:",  # Texto del widget
    dfDatos1["MUNICIPIOS"].unique(),     # Opciones (valores únicos de la columna MUNICIPIOS)
    default=dfDatos1["MUNICIPIOS"].unique()[0]  # Opción seleccionada por defecto (opcional)
)
st.write("Has seleccionado los siguientes municipios:", municipios_seleccionados)
# Filtrar el DataFrame según los municipios seleccionados
if municipios_seleccionados:
    df_filtrado = dfDatos1[dfDatos1["MUNICIPIOS"].isin(municipios_seleccionados)]
    st.write("Datos filtrados:", df_filtrado.shape[0])
else:
    st.write("No se ha seleccionado ningún municipio.")


#########################################################################################################
#c1, c2 = st.columns([60, 40])
#with c1:
#    dfRegistrosMes = dfDatos1.groupby('REGION').agg({'EDAD':'sum'}).reset_index().sort_values(by='EDAD',ascending=False)


import streamlit as st
import pandas as pd
import plotly.express as px

# Supongamos que dfDatos1 es tu DataFrame
# Convertimos la columna FECHA_TOMA_DATO a datetime
dfDatos1['FECHA_TOMA_DATO'] = pd.to_datetime(dfDatos1['FECHA_TOMA_DATO'], format='%d/%m/%Y')

# Extraemos el mes y el año de la fecha
dfDatos1['MES'] = dfDatos1['FECHA_TOMA_DATO'].dt.to_period('M')

# Filtro por municipio (multiselect)
municipios = dfDatos1['MUNICIPIOS'].unique()
municipios_seleccionados = st.multiselect(
    "Selecciona uno o más municipios:",  # Texto del widget
    municipios,  # Opciones (todos los municipios)
    default=municipios[0]  # Opción seleccionada por defecto (opcional)
)

# Filtramos el DataFrame por los municipios seleccionados
if municipios_seleccionados:
    df_filtrado = dfDatos1[dfDatos1['MUNICIPIOS'].isin(municipios_seleccionados)]
else:
    df_filtrado = dfDatos1  # Si no se selecciona ningún municipio, mostramos todos los datos

# Agrupamos por REGION y MES, y contamos los registros
dfRegistrosMes = df_filtrado.groupby(['REGION', 'MES']).size().reset_index(name='TOTAL')

# Convertimos el período 'MES' a string para que sea compatible con Plotly
dfRegistrosMes['MES'] = dfRegistrosMes['MES'].astype(str)

# Creamos el gráfico con Plotly
fig = px.line(
    dfRegistrosMes,
    x='MES',
    y='TOTAL',
    color='REGION',
    title=f"Total de registros por región y mes",
    labels={'MES': 'Mes', 'TOTAL': 'Total de registros', 'REGION': 'Región'}
)

# Mostramos el gráfico en Streamlit
st.plotly_chart(fig)
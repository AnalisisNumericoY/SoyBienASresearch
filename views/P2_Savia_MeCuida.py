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
    st.write("Cuidado y bienestar de los riesgos labores y prevención de riesgo cardiovascular")



########################################################################################################################################
#
#                                       Lectura de datos 
#
########################################################################################################################################


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

#
# Datos ANTICOAGULADOS Datos ANTICOAGULADOS Datos ANTICOAGULADOS Datos ANTICOAGULADOS Datos ANTICOAGULADOS Datos ANTICOAGULADOS 
#
gsheetid_Anticoagulados='1dr11Za06_6riF8h0Dzw6iIYmAcQY-UjR59kGQvo7aMg'
sheetid3='909398495#gid=909398495'
url3 = f'https://docs.google.com/spreadsheets/d/{gsheetid_Anticoagulados}/export?format=csv&gid={sheetid3}'
dfDatos_P1_Anticoagulados = pd.read_csv(url3)


#
# Datos INSUFICIENCIA CARDIACA Datos INSUFICIENCIA CARDIACA Datos INSUFICIENCIA CARDIACA Datos INSUFICIENCIA CARDIACA Datos
#
gsheetid_InsuficienciaCardiaca='18fKdiLCGWv8bcIdAdTQ6fiJ7CqN13qhVx_u0oy2n-MM'
sheetid_P1='1062583255#gid=1062583255'
url_P1 = f'https://docs.google.com/spreadsheets/d/{gsheetid_InsuficienciaCardiaca}/export?format=csv&gid={sheetid_P1}'
dfDatos_P1_InsuficienciaCardiaca = pd.read_csv(url_P1)

#
# Datos EPOC Datos EPOC Datos EPOC Datos EPOC Datos EPOC Datos EPOC Datos EPOC Datos EPOC Datos EPOC Datos EPOC Datos
#
gsheetid_EPOC='1WPIssU89MljJqsCUpcZU5mKOxw46XXq5AAgVGjgHzbM'
sheetid_P2='134011359#gid=134011359'
url_P2 = f'https://docs.google.com/spreadsheets/d/{gsheetid_EPOC}/export?format=csv&gid={sheetid_P2}'
dfDatos_P2_EPOC = pd.read_csv(url_P2)

#
# Datos RIESGO CARDIOVASCULAR Datos RIESGO CARDIOVASCULAR Datos RIESGO CARDIOVASCULAR Datos RIESGO CARDIOVASCULAR Datos RIESGO CARDIOVASCULAR
#
gsheetid_RiesgoCardiovascular='14Xot90PD6NwSQ8anSRjjigYwtDCm1J_psXSV-y3N02A'
sheetid_P3='906683604#gid=906683604'
url_P3 = f'https://docs.google.com/spreadsheets/d/{gsheetid_RiesgoCardiovascular}/export?format=csv&gid={sheetid_P3}'
dfDatos_P3_RiesgoCardiovascular = pd.read_csv(url_P3)






tab1, tab2, tab3, tab4 = st.tabs(["Insuficiencia Cardiaca", "Riesgo Cardiovascular", "EPOC","Anticoagulados"])

with tab1:
    st.write("Programa Insuficiencia Cardiaca")
    print(dfDatos2)
    st.dataframe(dfDatos_P1_InsuficienciaCardiaca, use_container_width=True)

with tab2:
    st.write("Programa Riesgo Cardiovascular")
    st.dataframe(dfDatos_P3_RiesgoCardiovascular, use_container_width=True)

with tab3:
    st.write("Programa EPOC")
    st.dataframe(dfDatos_P1_InsuficienciaCardiaca, use_container_width=True)

with tab4:
    st.write("Programa Anticoagulados")
    print(dfDatos_P1_Anticoagulados)
    st.dataframe(dfDatos_P1_Anticoagulados, use_container_width=True)


######################################################
#                                                            https://www.youtube.com/watch?v=1CC9mCzwgK4
######################################################

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
with st.container(border=True):
    st.plotly_chart(fig)






































import streamlit as st
import pandas as pd
import numpy as np
 
st.title("Dashboard Soy Bien")
df = pd.read_excel("BasedeDatosASResearchCompleta.xlsx")
m,n =df.shape
JR_m =len(pd.unique(df['Lugar Jornada']))
#JR_m=df['Lugar Jornada'].nunique()

df = pd.read_excel("BasedeDatosASResearch_Barrios.xlsx")
####
# seccion
####
st.subheader("Sección de métricas")
#c1_1 , c1_2, c1_3, c1_4 = st.columns(4)
c1_1 , c1_2 = st.columns(2)

c1_1.container(border=True).metric("Población atendida", f"{m}", "100")
c1_2.container(border=True).metric("Jornadas realizadas", f"{JR_m}", "-50") 


st.dataframe(df, use_container_width=True)

print(df.columns)




st.header('Cantidad de personas atendidas por jornada')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)




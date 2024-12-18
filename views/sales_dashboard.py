import streamlit as st
import pandas as pd
import numpy as np
 
st.title("Dashboard Soy Bien")
df = pd.read_excel("BasedeDatosASResearchCompleta.xlsx")
m,n =df.shape
JR_m =len(pd.unique(df['Lugar Jornada']))
#JR_m=df['Lugar Jornada'].nunique()

df_barrios = pd.read_excel("BasedeDatosASResearch_Barrios.xlsx")
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



#d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
#pd.DataFrame(data=d, index=[0, 1, 2, 3])

d = {'Medicina interna': df_barrios['MEDICINA INTERNA'] , 'Salud sexual': df_barrios['SALAUD SEXUAL']}
print(df_barrios.columns)
st.header('Cantidad de personas atendidas por jornada')
chart_data = pd.DataFrame(data=d)

st.line_chart(chart_data)



st.header('Georeferenciación y cantidad de pacientes por barrio')
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

chart_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [6.17, -75.5],
    columns=["lat", "lon"],
)


st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=6.20,
            longitude=-75.5,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)
import streamlit as st
import pandas as pd
import numpy as np
 
st.title("Dashboard Soy Bien")
df = pd.read_excel("BDMinterna.xlsx")
m,n =df.shape
JR_m =len(pd.unique(df['Lugar Jornada']))
#JR_m=df['Lugar Jornada'].nunique()

####
# seccion
####
st.subheader("Seccion de metricas")
#c1_1 , c1_2, c1_3, c1_4 = st.columns(4)
c1_1 , c1_2 = st.columns(2)

c1_1.container(border=True).metric("Población atendida", f"{m}", "100")
c1_2.container(border=True).metric("Jornadas realizadas", f"{JR_m}", "50") 





st.dataframe(df, use_container_width=True)

print(df.columns)

st.dataframe(df.groupby('Lugar Jornada'), use_container_width=True)



st.header('línea temporal')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)




st.header('MAP')

map_data = pd.DataFrame(
    np.random.randn(250, 2) / [50 , 50] + [19.43 , -99.13],
    columns=['lat', 'lon'])

st.map(map_data)




st.header('Slider')

x = st.slider('x') #esto es un widget
st.write(x, 'al cuadrado es ', x * x)




st.header('Text input')
st.text_input("Your name", key="name")




st.header('Checkbox')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c'])
    
    chart_data



st.header('Columns')
left_column, right_column = st.columns(2)


left_column.subheader('Left Column')
left_column.button('Press me!') 


with right_column:
    st.subheader('Right Column')
    chosen = st.radio(
        'Sorting hat',
        ("Gryffinder", "Ravencias", "huspilas", "Simimoy"))
    st.write(f"You are in {chosen} house")


    

st.sidebar.subheader('Selectbox')
add_selectbox = st.sidebar.selectbox(
    'como desea ser contactado?',
    ('Email', 'Telefono casa', 'celular')
)


st.sidebar.subheader('Slider')
add_slider = st.sidebar.slider(
    'Selecciona un rango de valores',
    0.0, 100.0, (25.0, 75.0)
)

"""
import streamlit as st

from forms.contact import contact_formPaciente, contact_formMedicinaInterna

st.image("./assets/Envigado.jpeg")

st.subheader("Proyecto Soy Bien Envigado", anchor=False)
st.subheader("Jornadas de atención en medicina interna y salud sexual", anchor=False)
st.write(
    """
    - Crea formularios
    - Crea formularios
    - Procesa datos
    - Imprime las historias clínicas 
    - tableros de visualización de la información
    """
)

#import plotly.express as px
#fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6])
#st.plotly_chart(fig, use_container_width=True)
#st.write("oprima click aqui para acceder al sitio privado del proyecto")
#

with st.container():
    st.write("En este contenedor van las analíticas.")

tab1, tab2 = st.tabs(["Pestaña 1", "Pestaña 2"])

with tab1:
    st.write("Contenido de la pestaña 1")

with tab2:
    st.write("Contenido de la pestaña 2")
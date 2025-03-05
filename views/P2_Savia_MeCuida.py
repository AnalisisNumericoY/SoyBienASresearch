import streamlit as st



# Expander básico
with st.expander("Haz clic sobre el programa que desees consultar"):
    st.write("EPOC.")
    st.write("RCV.")
    st.image("./assets/corazon.jpg", caption="cuida tu corazón")
    st.dataframe({
        "Pacientes": [11, 32, 43],
        "Programa": ["EPOC", "RCV", "OTRO"]})




st.image("./assets/SaviaSalud.png", width=230)
st.subheader("Proyecto Savia cuida mi corazón", anchor=False)
st.subheader("Programas de EPOC, Anticuagulados, Riesgo Cardiovascular y Protección Renal", anchor=False)
st.write(
    """
    - Crea formularios
    - Crea formularios
    - Procesa datos
    - Imprime las historias clínicas 
    - tableros de visualización de la información
    """
)

st.write("oprima click aqui para acceder al sitio privado del proyecto")

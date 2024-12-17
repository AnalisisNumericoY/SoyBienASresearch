import streamlit as st

from forms.contact import contact_form


#@st.experimental_dialog("Contactanos") Please replace `st.experimental_dialog` with `st.dialog` `st.experimental_dialog` will be removed after 2025-01-01
@st.dialog("Contactanos")
def show_contact_form():
    contact_form()
    #st.text_input("Primer nombre")


# --- HERO SECTION --- 
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/cropped-cropped-LOGO.png", width=230)
with col2:
    st.title("Soy Bien", anchor=False)
    st.write(
        "Cuidado y bienestar de los riesgos labores y prevención de riesgo cardiovascular"
    )
    if st.button(" Crea usuario"):
        show_contact_form()

# --- EXPERIENCE 6 QUALIFICATIONS ---
st.write("\n")
st.subheader("Beneficios de los clientes" , anchor=False)
st.write(
    """
    - 7 años de experiencia en atención al usuario
    - Fortalezas en riesgo cardiovascular
    - Salud sexual y reproductiva 
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Tecnología de punta", anchor=False)
st.write(
    """
    - Inteligencia artifical generativa
    - Redes neuronales profundas
    - Internet de las cosas
    - tableros de visualización de la información
    """
)
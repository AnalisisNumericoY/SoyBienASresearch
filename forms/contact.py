import re

import streamlit as st
import requests

WEBHOOK_URL = ""

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_patter = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_patter, email) is not None


def contact_formPaciente():
    with st.form("contact_form"):
        name = st.text_input("Primer nombre")
        email = st.text_input("dirección email")
        message = st.text_area("descripción")
        submit_button = st.form_submit_button("Enviar")
        
        if submit_button:
            st.success("información enviada con éxito")

def contact_formMedicinaInterna():
    with st.form("contact_form"):
        name = st.text_input("Primer nombre")
        email = st.text_input("Peso")
        identificacion = st.text_input("identificacion")
        fecha_consulta = st.date_input("fecha")
        message = st.number_input("Presión arterial")
        submit_button = st.form_submit_button("Enviar")
        
        if submit_button:
            st.success("información enviada con éxito")

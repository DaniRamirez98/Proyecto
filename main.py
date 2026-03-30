import streamlit as st
from scanner_ui import run_kiosko_scanner

st.sidebar.title("App Multitarea")

def operacion_suma():

    name = st.text_input("Nombre: ")
    n1= st.number_input("Numero 1")
    n2= st.number_input("Numero 2")

    if st.button("Sumar"):
        st.success(f"Hola {name}")
        st.write(f"{n1} + {n2} = {n1+n2}")
def operacion_resta():

    name = st.text_input("Nombre: ")
    n1= st.number_input("Numero 1")
    n2= st.number_input("Numero 2")

    if st.button("Restar"):
        st.success(f"Hola {name}")
        st.write(f"{n1} - {n2} = {n1-n2}")
def operacion_multiplicacion():
    name= st.text_input("Nombre: ")
    n1= st.number_input("Numero 1")
    n2= st.number_input("Numero 2")
    if st.button("Multiplicar"):
        st.success(f"Hola {name}")
        st.write(f"{n1} * {n2} = {n1*n2}")
def operacion_division():
    name= st.text_input("Nombre: ")
    n1= st.number_input("Numero 1")
    n2= st.number_input("Numero 2")
    if st.button("Dividir"):
        st.success(f"Hola {name}")
        st.write(f"{n1} / {n2} = {n1/n2}")
def opcion_acercade():
    st.write("Derechos Reservados  ")
    st.write("UCOL-FIME_ICI")

opcion = st.sidebar.selectbox("Opciones", [
    "Escáner Kiosko 24/7", "Suma", "Resta", "Multiplicacion", "Division", "Acerca de"
    ])


match opcion:
    case "Escáner Kiosko 24/7":
        run_kiosko_scanner()
    case "Suma":
        st.write("Esta es la opcion de suma... ")
        operacion_suma()
    case "Resta":
        st.write("Esta es la opcion de resta... ")
        operacion_resta()
    case "Multiplicacion":
        st.write("Esta es la opcion de multiplicacion... ")
        operacion_multiplicacion()
    case "Division":
        st.write("Esta es la opcion de division... ")
        operacion_division()
    case "Acerca de":
        opcion_acercade()

#en python no hay constructores se llaman inicializadores

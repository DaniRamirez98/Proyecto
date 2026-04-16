import streamlit as st
import numpy as np
from nn_logic import NeuralNetwork
from image_processing import preprocess_image, load_and_preprocess_images

st.sidebar.title("Calculadora e IA ICI")

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

def leaf_classifier():
    st.title("Clasificador de Hojas (Buena vs Mala)")
    st.write("Entrena una red neuronal desde cero con tus imágenes.")

    # Model parameters
    target_size = (64, 64)
    input_size = target_size[0] * target_size[1]

    if 'nn_model' not in st.session_state:
        st.session_state.nn_model = NeuralNetwork(input_size=input_size, hidden_size=64, output_size=1)
        st.session_state.trained = False

    st.subheader("1. Entrenamiento")
    col1, col2 = st.columns(2)
    with col1:
        good_leaves = st.file_uploader("Subir imágenes de Hojas BUENAS", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'], key="good")
    with col2:
        bad_leaves = st.file_uploader("Subir imágenes de Hojas MALAS", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'], key="bad")

    if st.button("Entrenar Modelo"):
        if good_leaves and bad_leaves:
            with st.spinner("Entrenando..."):
                # Load and preprocess
                X_good = load_and_preprocess_images([img.read() for img in good_leaves], target_size)
                X_bad = load_and_preprocess_images([img.read() for img in bad_leaves], target_size)

                X = np.vstack((X_good, X_bad))
                y = np.vstack((np.ones((len(X_good), 1)), np.zeros((len(X_bad), 1))))

                # Shuffle
                indices = np.random.permutation(len(X))
                X, y = X[indices], y[indices]

                st.session_state.nn_model.train(X, y, epochs=1000, learning_rate=0.1)
                st.session_state.trained = True
                st.success("¡Modelo entrenado exitosamente!")
        else:
            st.error("Por favor sube imágenes de ambas categorías.")

    st.subheader("2. Predicción")
    test_img = st.file_uploader("Subir imagen para clasificar", type=['png', 'jpg', 'jpeg'], key="test")

    if test_img:
        st.image(test_img, caption="Imagen a clasificar", use_container_width=True)
        if st.button("Clasificar"):
            if st.session_state.trained:
                img_array = preprocess_image(test_img.read(), target_size)
                prediction = st.session_state.nn_model.predict(img_array.reshape(1, -1))

                if prediction > 0.5:
                    st.success(f"Predicción: HOJA BUENA ({prediction[0][0]*100:.2f}%)")
                else:
                    st.error(f"Predicción: HOJA MALA ({(1-prediction[0][0])*100:.2f}%)")
            else:
                st.warning("Primero debes entrenar el modelo.")

opcion = st.sidebar.selectbox("Opciones", [
    "Suma", "Resta", "Multiplicacion", "Division", "Clasificador de Hojas", "Acerca de"
    ])


match opcion:
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
    case "Clasificador de Hojas":
        st.write("Esta es la opcion de clasificador de hojas... ")
        leaf_classifier()
    case "Acerca de":
        opcion_acercade()

#en python no hay constructores se llaman inicializadores

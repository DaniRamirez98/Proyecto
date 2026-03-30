import streamlit as st
from PIL import Image
from scanner_utils import decode_barcode
from data import get_product_info

def run_kiosko_scanner():
    st.title("Escáner de Productos Kiosko 24/7")
    st.write("Escanea el código de barras de cualquier producto para ver su precio.")

    # Camera input
    img_file_buffer = st.camera_input("Toma una foto al código de barras")

    if img_file_buffer is not None:
        # Load image with PIL
        image = Image.open(img_file_buffer)

        # Decode barcode
        with st.spinner("Decodificando..."):
            barcode_data = decode_barcode(image)

        if barcode_data:
            st.success(f"Código detectado: {barcode_data}")

            # Lookup product in database
            product_info = get_product_info(barcode_data)

            if product_info:
                st.subheader(f"Producto: {product_info['name']}")
                st.write(f"**Categoría:** {product_info['category']}")
                st.metric(label="Precio", value=f"${product_info['price']:,.2f} MXN")
            else:
                st.warning("Producto no encontrado en nuestra base de datos.")
                st.info("Pruébalo con uno de nuestros códigos de prueba (en el menú lateral).")
        else:
            st.error("No se pudo detectar ningún código de barras. Intenta de nuevo enfocando bien.")

    # Sidebar tips
    with st.sidebar.expander("Códigos de Barra de Prueba"):
        st.write("Copia uno de estos códigos si no tienes un producto a la mano:")
        st.code("7501055300071")  # Coca-Cola
        st.code("7501011115124")  # Papas Fritas
        st.code("7501000111202")  # Aceite

# Mock database of Kiosko products
# Format: {barcode: {"name": product_name, "price": price_mxn, "category": category}}

PRODUCT_DATABASE = {
    # Kanasta del hogar
    "7501000111202": {
        "name": "Aceite Vegetal 1L",
        "price": 45.50,
        "category": "Kanasta del hogar"
    },
    "7501020610310": {
        "name": "Arroz Blanco 900g",
        "price": 28.00,
        "category": "Kanasta del hogar"
    },
    "7501032902687": {
        "name": "Frijoles Refritos 440g",
        "price": 18.50,
        "category": "Kanasta del hogar"
    },

    # Fiesta (Botanas y Refrescos)
    "7501011115124": {
        "name": "Papas Fritas Original 170g",
        "price": 52.00,
        "category": "Fiesta"
    },
    "7501055300071": {
        "name": "Coca-Cola Original 600ml",
        "price": 18.00,
        "category": "Fiesta"
    },
    "7501030462002": {
        "name": "Cerveza Lata 355ml",
        "price": 22.00,
        "category": "Fiesta"
    },

    # Individual (Dulces y antojos)
    "7501000671607": {
        "name": "Chocolate Barra 50g",
        "price": 15.00,
        "category": "Individual"
    },
    "7501001150033": {
        "name": "Gomitas de Fruta 80g",
        "price": 12.50,
        "category": "Individual"
    },
    "7501025411219": {
        "name": "Galletas de Chocolate 100g",
        "price": 16.00,
        "category": "Individual"
    }
}

def get_product_info(barcode):
    """
    Looks up a product in the database by barcode.
    """
    return PRODUCT_DATABASE.get(barcode)

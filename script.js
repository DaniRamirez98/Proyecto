// Mock database of Kiosko products
const PRODUCT_DATABASE = {
    // Kanasta del hogar
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

    // Fiesta (Botanas y Refrescos)
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

    // Individual (Dulces y antojos)
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
};

function onScanSuccess(decodedText, decodedResult) {
    // Handle the scanned code
    console.log(`Code scanned: ${decodedText}`);

    const product = PRODUCT_DATABASE[decodedText];
    const resultContainer = document.getElementById('result-container');
    const readerContainer = document.getElementById('reader-container');

    if (product) {
        // Show product info
        document.getElementById('product-name').textContent = product.name;
        document.getElementById('product-category').textContent = product.category;
        document.getElementById('product-price').textContent = product.price.toFixed(2);

        resultContainer.classList.remove('hidden');
        readerContainer.classList.add('hidden');

        // Stop the scanner
        html5QrcodeScanner.clear();
    } else {
        alert("Producto no encontrado en nuestra base de datos: " + decodedText);
    }
}

function onScanError(errorMessage) {
    // Handle scan error (often occurs multiple times per second)
    // console.log(`Scan error: ${errorMessage}`);
}

const html5QrcodeScanner = new Html5QrcodeScanner(
    "reader", { fps: 10, qrbox: { width: 250, height: 150 } }, /* verbose= */ false);

html5QrcodeScanner.render(onScanSuccess, onScanError);

// Scan again button logic
document.getElementById('scan-again').addEventListener('click', () => {
    document.getElementById('result-container').classList.add('hidden');
    document.getElementById('reader-container').classList.remove('hidden');
    html5QrcodeScanner.render(onScanSuccess, onScanError);
});

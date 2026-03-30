from data import get_product_info
from scanner_utils import decode_barcode
from PIL import Image
import numpy as np

def test_database_lookup():
    print("Testing database lookup...")
    # Test known product
    coca_cola = get_product_info("7501055300071")
    assert coca_cola is not None
    assert coca_cola["name"] == "Coca-Cola Original 600ml"
    assert coca_cola["price"] == 18.00

    # Test unknown product
    unknown = get_product_info("0000000000000")
    assert unknown is None
    print("Database lookup tests passed!")

def test_decoding_logic():
    print("Testing decoding logic structure...")
    # Since we can't easily provide a real image with a barcode in this environment
    # without a file, we at least check if the function handles empty/invalid input
    try:
        # Create a blank image
        blank_image = Image.new('RGB', (100, 100), color = 'white')
        result = decode_barcode(blank_image)
        assert result is None
        print("Decoding logic (empty case) passed!")
    except Exception as e:
        print(f"Decoding logic test failed: {e}")
        raise e

if __name__ == "__main__":
    test_database_lookup()
    test_decoding_logic()

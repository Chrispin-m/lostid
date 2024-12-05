import tempfile
from paddleocr import PaddleOCR
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
import os
import shutil

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")

def clear_paddleocr_cache():
    cache_dir = os.path.expanduser("~/.paddleocr/")
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)

def preprocess_image(image):
    image = image.convert("L")
    image = image.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(2)

def extract_text_from_image(image):
    if not isinstance(image, Image.Image):
        raise ValueError("The input should be a PIL.Image object")

    clear_paddleocr_cache()

    # Save the processed image to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_image_file:
        temp_image_path = temp_image_file.name
        processed_image = preprocess_image(image)
        processed_image.save(temp_image_path)

    try:
        result = ocr.ocr(temp_image_path, cls=True)
        extracted_text = "\n".join([line[1][0] for line in result[0]])
        print(extracted_text)
        return extracted_text
    except Exception as e:
        print(f"Error during OCR: {e}")
        return ""
    finally:
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)
        clear_paddleocr_cache()
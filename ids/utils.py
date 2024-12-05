from paddleocr import PaddleOCR
from PIL import Image, ImageEnhance, ImageFilter
import os

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def preprocess_image(image):
    image = image.convert("L")
    image = image.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(2)

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")

    with Image.open(image_path) as img:
        processed_image = preprocess_image(img)

    temp_image_path = "temp_image.png"
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


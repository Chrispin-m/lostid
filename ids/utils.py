import easyocr
from PIL import Image, ImageEnhance, ImageFilter
import os

def preprocess_image(image):
    image = image.convert("L")  
    image = image.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(image)  
    return enhancer.enhance(2)

def extract_text_from_image(image):
    if not isinstance(image, Image.Image):
        raise ValueError("The input should be a PIL.Image object")

    processed_image = preprocess_image(image)
    
    reader = easyocr.Reader(['en']) 
    result = reader.readtext(processed_image)
    extracted_text = "\n".join([text[1] for text in result])
    print(extracted_text)
    return extracted_text
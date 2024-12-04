import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def extract_text_from_image(image):
    if not isinstance(image, Image.Image):
        image = Image.open(image)
    image = image.convert("L")  
    image = image.filter(ImageFilter.MedianFilter())  
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  

    # Extract text using pytesseract
    custom_config = r'--psm 6' 
    text = pytesseract.image_to_string(image, config=custom_config)
    print(text)

    return text

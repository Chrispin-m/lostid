import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def extract_text_from_image(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Optional preprocessing for better OCR results
    image = image.convert("L")  # Convert to grayscale
    image = image.filter(ImageFilter.MedianFilter())  # Reduce noise
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Increase contrast
    
    # Extract text using pytesseract
    custom_config = r'--psm 6'  # Page segmentation mode: Assume a single uniform block of text
    text = pytesseract.image_to_string(image, config=custom_config)
    print(text)
    
    return text

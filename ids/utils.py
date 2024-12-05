from paddleocr import PaddleOCR
from PIL import Image, ImageEnhance, ImageFilter

def extract_text_from_image(image):
    # Ensure image is a PIL Image
    if not isinstance(image, Image.Image):
        image = Image.open(image)
    
    # Preprocess the image
    image = image.convert("L")  # Convert to grayscale
    image = image.filter(ImageFilter.MedianFilter()) 
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  

    temp_image_path = "temp_image.png"
    image.save(temp_image_path)

    # Initialize PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang="en")  

    # Perform OCR
    result = ocr.ocr(temp_image_path, cls=True)
    
    # Extract text
    extracted_text = "\n".join([line[1][0] for line in result[0]]) 

    print(extracted_text)
    return extracted_text

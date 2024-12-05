from google.cloud import vision
from PIL import Image

def extract_text_from_image(image):
    client = vision.ImageAnnotatorClient()

    if not isinstance(image, Image.Image):
        image = Image.open(image)

    image_bytes = image.tobytes()

    content = vision.Image(content=image_bytes)

    #text detection
    response = client.text_detection(image=content)
    text = response.full_text_annotation.text
    print(text)

    return text
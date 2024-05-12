from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import warnings

def load_model():
    warnings.filterwarnings('ignore', category=UserWarning, module='transformers')
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
    return processor, model

def generate_image_description(img_path, text, processor, model):
    raw_image = Image.open(img_path).convert('RGB')
    inputs = processor(raw_image, text, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=20)
    description = processor.decode(output[0], skip_special_tokens=True)
    return description

# Usage example:
processor, model = load_model()
img_path = './images/take2.jpeg'
text = "The only object here is "
description = generate_image_description(img_path, text, processor, model)
print(description)

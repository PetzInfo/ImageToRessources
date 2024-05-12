from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import warnings

# Suppress warnings if you don't want to see them in your console
warnings.filterwarnings('ignore', category=UserWarning, module='transformers')

# Set up the image captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

img_path = './images/take3.jpeg'  # Make sure the path is correct and accessible
raw_image = Image.open(img_path).convert('RGB')  # Open the image directly

# Conditional image captioning
text = "The only object here is "
inputs = processor(raw_image, text, return_tensors="pt")

# Control the generation length by specifying max_new_tokens
out = model.generate(**inputs, max_new_tokens=20)
image_description = processor.decode(out[0], skip_special_tokens=True)

# Only print the final description
print(image_description)

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

img_path = './images/take3.jpeg'  # Make sure the path is correct and accessible
raw_image = Image.open(img_path).convert('RGB')  # Open the image directly

# Conditional image captioning
text = "the main objekt here is "
inputs = processor(raw_image, text, return_tensors="pt")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))
from salesForce_imageToText import load_model, generate_image_description
from textToPrompt import send_post_request, handle_streaming_response
from captureImage import capture_image

# Load the model once
processor, model = load_model()

# Main loop
while True:
    if not capture_image():  # Check if user chose to exit during capture
        print("Exiting...")
        break

    # Generate description
    img_path = './images/captured_image.jpg'
    text = "The only object here is "
    description = generate_image_description(img_path, text, processor, model)
    print(description)

    # Send description to prompt generation service
    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "promptEng",
        "prompt": description,
        "max_tokens": 50
    }
    response = send_post_request(url, data)
    final_prompt = handle_streaming_response(response)
    if final_prompt:
        print(final_prompt)

    # Ask the user if they want to continue
    if input("Capture another image? (y/n): ").strip().lower() != 'y':
        print("Exiting...")
        break

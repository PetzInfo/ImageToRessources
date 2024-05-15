from image_to_text import load_model, generate_image_description
from text_to_prompt import send_post_request, handle_streaming_response
from capture_image import capture_image
import time

# Load the model once
processor, model = load_model()

# Main loop
while True:
    start = time.time()
    if not capture_image():  # Check if user chose to exit during capture
        print("Exiting...")
        break

    # Generate description
    img_path = './images/captured_image.jpg'
    text = "The only one object here is a: "
    description = generate_image_description(img_path, text, processor, model)
    timeTillDescription = time.time()
    print(description)
    print(f"Time taken to generate description: {timeTillDescription - start:.2f} seconds")

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

    final = time.time()
    print(f"Whole time taken: {final - start:.2f} seconds")
    # Ask the user if they want to continue
    if input("Capture another image? (y/n): ").strip().lower() != 'y':
        print("Exiting...")
        break

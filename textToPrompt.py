import requests
import json

# URL for the Ollama API endpoint
url = 'http://localhost:11434/api/generate'

# Data to send in the POST request, change the 'model' if you have a different model name
data = {
    "model": "promptEng",  # This should match the model name your Ollama server is configured to use
    "prompt": "Pencil",
    "max_tokens": 50
}

# Send a POST request to the server with stream enabled
response = requests.post(url, json=data, stream=True)

prompt = 'Generate an image displaying the following resources: '

# Check if the request was successful
if response.status_code == 200:
    print("Streaming data from model:")
    try:
        for chunk in response.iter_lines():
            if chunk:  
                decoded_chunk = json.loads(chunk.decode('utf-8'))
                prompt += decoded_chunk['response']

                if decoded_chunk.get('done', False):
                    print(prompt)
                    break

    except Exception as e:
        print("Error while streaming the data:", e)
else:
    print("Failed to get response, status code:", response.status_code)

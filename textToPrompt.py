import requests
import json

def send_post_request(url, data):
    response = requests.post(url, json=data, stream=True)
    return response

def handle_streaming_response(response):
    prompt = 'Generate an image displaying the following resources: '
    if response.status_code == 200:
        try:
            for chunk in response.iter_lines():
                if chunk:
                    decoded_chunk = json.loads(chunk.decode('utf-8'))
                    prompt += decoded_chunk['response']
                    if decoded_chunk.get('done', False):
                        return prompt
        except Exception as e:
            print("Error while streaming the data:", e)
            return None
    else:
        print("Failed to get response, status code:", response.status_code)
        return None

# Usage example:
# url = 'http://localhost:11434/api/generate'
# data = {
#     "model": "promptEng",
#     "prompt": "the only object here is the iphone x",
#     "max_tokens": 50
# }
# response = send_post_request(url, data)
# final_prompt = handle_streaming_response(response)
# if final_prompt:
#     print(final_prompt)

import requests
import json

BASE_URL = "http://localhost:11434/api/"
GENERATE_URL = BASE_URL + "generate/"
PULL_URL = BASE_URL + "pull/"
MODEL = 'gemma:2b'


def setup_llama_client():
    data = {
        "name": MODEL,
        "stream": False
    }
    response = requests.post(PULL_URL, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Model {MODEL} is ready to use.")
    else:
        print(f"Error setting up model {MODEL}.")


def generate_text(prompt):
    data = {
        "model": "gemma:2b",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(GENERATE_URL, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json().get('response')
        print(f"Response from LLAMA: {result}")
        return result
    else:
        print(f"Error generating text: {response.status_code}")
        return None


setup_llama_client()

from flask import Flask, request, jsonify
from llama_client import generate_text

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_text_endpoint():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'Prompt is required.'}), 400
    print(f"Handling POST request, received prompt: {prompt}")
    result = generate_text(prompt)
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=8080)

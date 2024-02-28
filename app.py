import openai
from flask import Flask, request, jsonify ,send_from_directory

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    prompt_text = request.json['text']

    # Set up OpenAI API parameters and call the GPT-3 model
    model_engine = "text-davinci-002" # or any other model you have access to
    prompt_length = 50 # length of generated response
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        max_tokens=prompt_length
    )

    # Extract the generated response from the OpenAI API output
    response_text = response.choices[0].text.strip()

    return jsonify({'response': response_text})

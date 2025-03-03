from flask import Flask, render_template, request, jsonify
import base64
import json
import boto3
from PIL import Image
from io import BytesIO
import re
from utils.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, MODEL_ID
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Add a secure secret key

# Initialize Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def normalize_text(text):
    """Normalize text for comparison"""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

def process_image(img):
    """Process image using Bedrock"""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode()

    payload = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": encoded_image
                        }
                    },
                    {
                        "type": "text",
                        "text": "Extract text exactly as it appears in this image."
                    }
                ]
            }
        ],
        "max_tokens": 2000,
        "anthropic_version": "bedrock-2023-05-31"
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        contentType="application/json",
        body=json.dumps(payload)
    )

    output_binary = response["body"].read()
    output_json = json.loads(output_binary)
    return output_json["content"][0]["text"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if not file:
        return jsonify({'error': 'Empty file'}), 400

    prompt = request.form.get('prompt', 'Extract text exactly as it appears in this image.')
    ground_truth = request.form.get('ground_truth', '')

    try:
        # Process image
        img = Image.open(file)
        extracted_text = process_image(img)
        
        # Compare with ground truth
        normalized_extracted = normalize_text(extracted_text)
        normalized_truth = normalize_text(ground_truth)
        matches = normalized_extracted == normalized_truth
        
        return jsonify({
            'extracted_text': extracted_text,
            'normalized_extracted': normalized_extracted,
            'normalized_truth': normalized_truth,
            'matches': matches
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
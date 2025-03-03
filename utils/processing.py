import base64
import json
import requests
import boto3
from PIL import Image
from io import BytesIO
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, MODEL_ID

# Initialize Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def process_image(img):
    """
    Process an image and extract text using Bedrock LLM.
    """
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
    output_text = output_json["content"][0]["text"]

    return output_text
import boto3
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_aws_credentials():
    try:
        # Get credentials from environment variables with proper names
        aws_access_key_id = os.getenv("AWS_BEDROCK_KEY")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_region = os.getenv("AWS_REGION")
        model_id = os.getenv("MODEL_ID")
        
        # Debug prints
        print("Environment variables loaded:")
        print(f"AWS Access Key: {'*' * len(aws_access_key_id) if aws_access_key_id else 'Not set'}")
        print(f"AWS Secret Key: {'*' * len(aws_secret_access_key) if aws_secret_access_key else 'Not set'}")
        print(f"AWS Region: {aws_region}")
        print(f"Model ID: {model_id}")
        
        if not all([aws_access_key_id, aws_secret_access_key, aws_region, model_id]):
            missing_vars = []
            if not aws_access_key_id: missing_vars.append("AWS_BEDROCK_KEY")
            if not aws_secret_access_key: missing_vars.append("AWS_SECRET_ACCESS_KEY")
            if not aws_region: missing_vars.append("AWS_REGION")
            if not model_id: missing_vars.append("MODEL_ID")
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        # Initialize Bedrock client
        print("\nInitializing Bedrock client...")
        bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        
        # AWS Bedrock Claude specification
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "system": "",
            "messages": [{
                "role": "user",
                "content": "Say hello!"
            }]
        }
        
        print("Sending test request to Bedrock...")
        try:
            response = bedrock.invoke_model(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(body)
            )
            
            print("\nProcessing response...")
            response_body = json.loads(response['body'].read().decode('utf-8'))
            if 'error' in response_body:
                raise Exception(f"Error in Bedrock response: {response_body['error']}")
                
            print("\nAWS credentials are valid!")
            print("Successfully connected to Bedrock")
            print(f"Response from model: {json.dumps(response_body, indent=2)}")
            return True
            
        except bedrock.exceptions.ValidationException as e:
            print("\nValidation error with request format:")
            print(str(e))
            print("\nRequest payload was:")
            print(json.dumps(body, indent=2))
            return False
            
    except ValueError as e:
        print("\nError with environment variables:")
        print(str(e))
        return False
    except Exception as e:
        print("\nError testing AWS credentials:")
        print(str(e))
        print("\nFull error details:")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_aws_credentials()
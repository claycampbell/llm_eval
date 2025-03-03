from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_BEDROCK_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"
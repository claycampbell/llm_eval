# Technical Context

## Project Structure
- utils/: Core utility functions including text comparison and image processing
- tests/: Unit tests for utility functions
- data/: Reserved for data storage (currently unused)

## Dependencies
### Core Python Packages
- boto3: AWS SDK for Bedrock API integration
- PIL: Python Imaging Library for image handling
- pytest: Testing framework
- base64: For image encoding
- json: For API payload handling
- requests: HTTP client library

### AWS Resources
- Bedrock Runtime: For LLM-based text extraction from images
- Required Environment Variables:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - AWS_REGION
  - MODEL_ID

## Architecture
- Modular design with clear separation of concerns:
  - utils/processing.py: Handles image processing and AWS Bedrock integration
  - utils/comparison.py: Text comparison utilities
  - utils/config.py: Configuration management
  - tests/: Comprehensive test coverage for all utilities

## Technical Decisions
1. Using AWS Bedrock for text extraction:
   - Provides reliable OCR capabilities
   - Easy integration with AWS infrastructure
   - Supports multiple image formats

2. Testing Strategy:
   - Unit tests for all utilities
   - Mock AWS client for testing
   - Testing both success and error cases
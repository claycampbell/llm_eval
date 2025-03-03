# System Architecture

## Overview
The application has been simplified to a single-screen interface that handles document evaluation through a streamlined process.

## Core Components

### Backend (simple.py)
- **Flask Application**: Serves the web interface and handles API requests
- **Image Processing**: Uses AWS Bedrock for text extraction
- **Text Comparison**: Normalizes and compares extracted text with ground truth
- **Error Handling**: Basic error handling for file uploads and API calls

### Frontend (templates/index.html)
- **Single Page Interface**: All functionality in one screen
- **File Upload**: Image document upload
- **Text Inputs**: 
  - Optional prompt field
  - Ground truth input field
- **Results Display**: Shows extracted text, normalized versions, and match status

### Utility Modules
- **Configuration**: AWS credentials and settings
- **Text Processing**: Normalization and comparison functions

## Data Flow
1. User uploads image and enters ground truth
2. Flask backend processes the image using AWS Bedrock
3. Text normalization applied to both extracted and ground truth text
4. Comparison performed and results returned to frontend
5. Results displayed in-place on the same page

## Design Decisions
- **Simplified Architecture**: Reduced complexity by combining functionality into a single page
- **Direct Processing**: No intermediate storage, results shown immediately
- **Clear Feedback**: Side-by-side comparison of extracted and ground truth text
- **Flexible Prompting**: Optional custom prompts for different use cases

## Dependencies
- AWS Bedrock for image text extraction
- Flask for web interface
- Pillow for image handling
- Bootstrap for basic styling
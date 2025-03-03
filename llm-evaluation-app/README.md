# Simple LLM Document Evaluation

A streamlined application for evaluating LLM text extraction capabilities by comparing outputs with ground truth.

## Features

- Upload images for text extraction
- Custom prompt support
- Ground truth comparison
- Normalized text matching
- Real-time results display

## Setup

1. Create a `.env` file with AWS credentials:
```
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=your_region
MODEL_ID=your_model_id
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python simple.py
```

## Usage

1. Open `http://localhost:5000` in your browser
2. Upload an image
3. (Optional) Enter a custom prompt
4. Enter the expected ground truth text
5. Click 'Evaluate' to see results

The application shows:
- Extracted text from the image
- Normalized versions of both extracted and ground truth text
- Whether they match

## Architecture

```
simple.py            - Main Flask application
├── templates/       - HTML templates
│   └── index.html  - Single page interface
└── utils/          - Utility modules
    ├── config.py   - AWS configuration
    └── processing.py - Image processing logic
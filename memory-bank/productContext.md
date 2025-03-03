# Product Context

## Purpose
This LLM Evaluation App provides a set of utilities for comparing and evaluating text outputs, with a particular focus on text extraction from images. It serves as a toolkit for assessing and comparing the accuracy of various text extraction methods.

## Core Functionalities
1. Image Processing:
   - Extract text from images using AWS Bedrock LLM
   - Handle various image formats and sizes
   - Normalize and process extracted text

2. Text Comparison:
   - Compare ground truth text with extracted output
   - Normalize text for fair comparison
   - Handle various text formats and special characters

## User Experience Goals
- Simple and clear API for text comparison
- Reliable image-to-text extraction
- Consistent text normalization across comparisons
- Comprehensive error handling
- Easy integration with AWS services

## Problem Space
Developers need reliable tools to:
- Extract text from images accurately
- Compare extracted text with expected output
- Normalize text for consistent evaluation
- Handle edge cases (empty text, special characters)

## Target Users
- Developers working on text extraction systems
- QA engineers testing OCR accuracy
- Researchers comparing text extraction methods
- Teams using AWS Bedrock for text processing

## Success Criteria
1. Technical:
   - Accurate text extraction from images
   - Consistent text normalization
   - Reliable comparison results
   - Comprehensive test coverage

2. User Experience:
   - Clear error messages
   - Simple integration process
   - Well-documented APIs
   - Predictable behavior
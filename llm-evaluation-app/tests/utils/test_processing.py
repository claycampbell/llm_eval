import pytest
from PIL import Image
import base64
import json
from io import BytesIO
from unittest.mock import Mock, patch
from llm_evaluation_app.utils.processing import process_image

@pytest.fixture
def sample_image():
    """Create a simple test image with some text."""
    img = Image.new('RGB', (100, 30), color='white')
    return img

@pytest.fixture
def mock_bedrock_client():
    """Mock AWS Bedrock client."""
    mock_client = Mock()
    mock_response = {
        "body": Mock(
            read=Mock(
                return_value=json.dumps({
                    "content": [{"text": "Sample extracted text"}]
                }).encode()
            )
        )
    }
    mock_client.invoke_model.return_value = mock_response
    return mock_client

@patch('boto3.client')
def test_process_image_success(mock_boto3_client, sample_image, mock_bedrock_client):
    """Test successful image processing."""
    mock_boto3_client.return_value = mock_bedrock_client
    
    result = process_image(sample_image)
    
    assert result == "Sample extracted text"
    mock_bedrock_client.invoke_model.assert_called_once()
    
    # Verify the payload structure
    call_args = mock_bedrock_client.invoke_model.call_args[1]
    payload = json.loads(call_args['body'])
    
    assert payload['messages'][0]['role'] == 'user'
    assert payload['messages'][0]['content'][0]['type'] == 'image'
    assert payload['messages'][0]['content'][1]['type'] == 'text'
    assert 'data' in payload['messages'][0]['content'][0]['source']

@patch('boto3.client')
def test_process_image_error(mock_boto3_client, sample_image):
    """Test error handling during image processing."""
    mock_client = Mock()
    mock_client.invoke_model.side_effect = Exception("API Error")
    mock_boto3_client.return_value = mock_client
    
    with pytest.raises(Exception) as exc_info:
        process_image(sample_image)
    
    assert "API Error" in str(exc_info.value)

def test_invalid_image():
    """Test handling of invalid image input."""
    with pytest.raises(AttributeError):
        process_image(None)

@pytest.fixture
def large_image():
    """Create a large test image."""
    return Image.new('RGB', (5000, 5000), color='white')

def test_large_image(large_image):
    """Test processing of large images."""
    processed = process_image(large_image)
    assert isinstance(processed, str)
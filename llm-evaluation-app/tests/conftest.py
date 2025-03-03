import pytest
from PIL import Image
from unittest.mock import Mock
import json

@pytest.fixture
def sample_image():
    """Create a simple test image."""
    return Image.new('RGB', (100, 30), color='white')

@pytest.fixture
def mock_bedrock_client():
    """Create a mock AWS Bedrock client."""
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

@pytest.fixture
def mock_error_client():
    """Create a mock AWS Bedrock client that raises an error."""
    mock_client = Mock()
    mock_client.invoke_model.side_effect = Exception("API Error")
    return mock_client

@pytest.fixture
def large_image():
    """Create a large test image."""
    return Image.new('RGB', (5000, 5000), color='white')

@pytest.fixture
def test_env(monkeypatch):
    """Set up test environment variables."""
    monkeypatch.setenv('AWS_BEDROCK_KEY', 'test_key')
    monkeypatch.setenv('AWS_SECRET_ACCESS_KEY', 'test_secret')
    monkeypatch.setenv('AWS_REGION', 'us-west-2')
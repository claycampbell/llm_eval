import pytest
from llm_evaluation_app.utils.comparison import exact_match

def test_exact_match_identical_strings():
    """Test exact match with identical strings."""
    ground_truth = "This is a test string."
    output = "This is a test string."
    assert exact_match(ground_truth, output) is True

def test_exact_match_different_strings():
    """Test exact match with different strings."""
    ground_truth = "This is a test string."
    output = "This is a different string."
    assert exact_match(ground_truth, output) is False

def test_exact_match_case_sensitivity():
    """Test exact match with different letter casing."""
    ground_truth = "This is a Test String."
    output = "this is a test string."
    # After normalization, these should match
    assert exact_match(ground_truth, output) is True

def test_exact_match_whitespace():
    """Test exact match with different whitespace."""
    ground_truth = "This   is  a   test    string."
    output = "This is a test string."
    # After normalization, these should match
    assert exact_match(ground_truth, output) is True

def test_exact_match_punctuation():
    """Test exact match with different punctuation."""
    ground_truth = "This is a test string!"
    output = "This is a test string"
    # After normalization, these should match
    assert exact_match(ground_truth, output) is True

def test_exact_match_empty_strings():
    """Test exact match with empty strings."""
    assert exact_match("", "") is True
    assert exact_match("text", "") is False
    assert exact_match("", "text") is False

def test_exact_match_special_characters():
    """Test exact match with special characters."""
    ground_truth = "Test with @#$%^&* special chars!"
    output = "Test with special chars"
    # After normalization, these should match
    assert exact_match(ground_truth, output) is True

def test_exact_match_numbers():
    """Test exact match with numbers."""
    ground_truth = "Test 123 with numbers 456"
    output = "Test 123 with numbers 456"
    assert exact_match(ground_truth, output) is True

def test_exact_match_none_values():
    """Test exact match with None values."""
    with pytest.raises(AttributeError):
        exact_match(None, "text")
    with pytest.raises(AttributeError):
        exact_match("text", None)
    with pytest.raises(AttributeError):
        exact_match(None, None)
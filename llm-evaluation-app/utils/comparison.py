import re

def normalize_text(text):
    """
    Normalize the text by:
    - Removing leading/trailing whitespaces
    - Replacing multiple spaces with a single space
    - Normalizing punctuation
    """
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

def exact_match(ground_truth, output):
    """
    Perform an exact match comparison between ground truth and model output.
    """
    normalized_gt = normalize_text(ground_truth)
    normalized_output = normalize_text(output)
    
    return normalized_gt == normalized_output
"""
Demo script to test the LLM Evaluation App functionality.
Run with: python test_demo.py
"""
import os
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
from utils.processing import process_image
from utils.comparison import exact_match

def create_test_image(text="Hello, LLM Evaluation!", size=(400, 100)):
    """Create a test image with readable text."""
    # Create white background
    img = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", size[1]//4)
    except OSError:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Add text in black
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Center text
    x = (size[0] - text_width) / 2
    y = (size[1] - text_height) / 2
    draw.text((x, y), text, fill='black', font=font)
    return img

def test_image_processing(name, text, size=(400, 100)):
    """Test image processing and comparison."""
    print(f"\nTesting image: {name}")
    print("-" * 50)
    
    # Create and save test image
    img = create_test_image(text, size)
    img_path = f"test_image_{name}.png"
    img.save(img_path)
    print(f"✅ Created test image: {img_path}")
    
    # Process the image
    try:
        extracted_text = process_image(img)
        print(f"✅ Extracted text: {extracted_text}")
        
        # Compare text
        print("\nComparison Results:")
        print(f"Ground truth : {text}")
        print(f"Extracted    : {extracted_text}")
        match_result = exact_match(text, extracted_text)
        if match_result:
            print("✅ Texts match!")
        else:
            print("❌ Texts differ")
            
        return True
        
    except Exception as e:
        print(f"❌ Error processing image: {str(e)}")
        return False

def main():
    print("LLM Evaluation App Demo\n" + "="*50)

    # Load environment variables
    print("\n1. Checking environment setup...")
    load_dotenv()
    required_vars = ['AWS_BEDROCK_KEY', 'AWS_SECRET_ACCESS_KEY', 'AWS_REGION']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        print(f"❌ Error: Missing environment variables: {', '.join(missing_vars)}")
        print("Please set them in your .env file")
        return
    print("✅ Environment variables loaded")

    # Test cases
    test_cases = [
        ("simple", "Hello, LLM Evaluation!", (400, 100)),
        ("long", "This is a longer text to test extraction capabilities.", (600, 100)),
        ("multiline", "First line\nSecond line\nThird line", (400, 150)),
    ]
    
    # Run test cases
    print("\n2. Running test cases...")
    success_count = 0
    for name, text, size in test_cases:
        if test_image_processing(name, text, size):
            success_count += 1
            
    print(f"\nTest cases completed: {success_count}/{len(test_cases)} successful")

    print("\n3. Running unit tests...")
    import pytest
    pytest.main(["-v", "tests/utils/test_processing.py", "tests/utils/test_comparison.py"])

    print("\nDemo completed! 🎉")
    print("\nGenerated test files:")
    for name, _, _ in test_cases:
        print(f"- test_image_{name}.png")
    print("\nNext steps:")
    print("1. Check the generated test images")
    print("2. Review extraction accuracy")
    print("3. Examine unit test results")
    print("4. Try with your own images!")

if __name__ == "__main__":
    main()
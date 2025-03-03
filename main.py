from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import os
from utils.processing import process_image
from utils.comparison import exact_match

app = FastAPI()

# Storage directory for uploaded files
UPLOAD_DIR = "./data/uploaded/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image, process it with LLM, and compare with ground truth.
    """
    if not file.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="File format not supported.")
    
    # Save file
    file_location = f"{UPLOAD_DIR}{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    # Open and process the image
    img = Image.open(file_location)
    extracted_text = process_image(img)
    
    # Load ground truth (for demo, you may hardcode or fetch from DB)
    ground_truth = "Your expected text here"
    
    # Exact comparison
    is_match = exact_match(ground_truth, extracted_text)

    result = {
        "extracted_text": extracted_text,
        "ground_truth": ground_truth,
        "exact_match": is_match
    }
    
    return JSONResponse(content=result)

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM Evaluation App!"}
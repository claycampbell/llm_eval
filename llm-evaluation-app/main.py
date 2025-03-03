from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import os
from utils.processing import process_image
from utils.comparison import exact_match
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Storage directory for uploaded files
UPLOAD_DIR = "./data/uploaded/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class Document(BaseModel):
    id: int
    filename: str
    content_type: str
    upload_date: str

class Experiment(BaseModel):
    id: int
    llm_name: str
    prompt: str
    dataset_id: int
    creation_date: str

class ComparisonResult(BaseModel):
    precision: float
    recall: float
    f1_score: float
    exact_match_ratio: float

class Report(BaseModel):
    experiment_id: int
    accuracy_metrics: ComparisonResult
    error_analysis: str

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

@app.post("/upload-document/")
async def upload_document(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.post("/process-document/")
async def process_document(document_id: int):
    return {"document_id": document_id}

@app.post("/compare-data/")
async def compare_data(ground_truth: str, extracted_text: str):
    return {"ground_truth": ground_truth, "extracted_text": extracted_text}

@app.get("/experiments/")
async def list_experiments():
    return [{"experiment_id": 1}, {"experiment_id": 2}]

@app.get("/experiments/{experiment_id}")
async def get_experiment(experiment_id: int):
    return {"experiment_id": experiment_id}

@app.get("/reports/")
async def generate_reports():
    return [{"report_id": 1}, {"report_id": 2}]
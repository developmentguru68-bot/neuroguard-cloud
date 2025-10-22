from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.ml_engine import predict_outcome
from services.pdf_generator import generate_pdf
import os

app = FastAPI(title="NeuroGuard Cloud API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "✅ NeuroGuard API is online"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    data = await file.read()
    prediction = predict_outcome(data)
    pdf_path = generate_pdf(prediction)
    return {"prediction": prediction, "pdf_url": f"/{pdf_path}"}

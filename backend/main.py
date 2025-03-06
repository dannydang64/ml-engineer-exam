from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
import fitz  # PyMuPDF for PDF text extraction
import re
import json
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import TextChunk

app = FastAPI()

# Initialize the database
init_db()

# Define the maximum file size (e.g., 5MB)
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

def chunk_text(text, chunk_size=50):
    """Splits text into chunks of 50 words each."""
    words = re.split(r"\s+", text)
    return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Uploads and processes a PDF, splitting it into text chunks."""
    # Check file size before processing
    file_size = file.file.seek(0, 2)  # Move to end of file to get size
    if file_size > MAX_FILE_SIZE_BYTES:
        raise HTTPException(status_code=413, detail=f"File size exceeds {MAX_FILE_SIZE_MB}MB limit")

    file.file.seek(0)  # Reset file pointer to the beginning

    # Read and process the PDF
    content = await file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    text_chunks = chunk_text(" ".join([page.get_text() for page in doc]), 50)

    for chunk in text_chunks:
        db.add(TextChunk(text=chunk))
    db.commit()
    return {"message": "PDF processed", "total_chunks": len(text_chunks)}

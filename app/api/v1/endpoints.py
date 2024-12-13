from fastapi import APIRouter, HTTPException, Depends
from app.schemas.pdf_schema import PDFResponse, FileUpload
from app.services.pdf_service import PDFProcessor
from app.api.v1.dependencies import get_pdf_processor

router = APIRouter()

@router.post("/upload-pdf/", response_model=PDFResponse)
async def upload_pdf(file_upload: FileUpload, processor: PDFProcessor = Depends(get_pdf_processor)):
    if file_upload.file_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")
    
    # Necessário pois o file.data pode vir com números negativos de Int8Array
    file_data = [b & 0xFF for b in file_upload.file_data] 
    file_bytes = bytes(file_data)
    result = await processor.process_pdf(file_bytes)
    return result
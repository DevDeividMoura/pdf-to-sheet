from pydantic import BaseModel, Field
from typing import List, Dict, Union

class FileUpload(BaseModel):
    file_data: List[int] = Field(..., description="List of bytes representing the file content")
    file_type: str = Field(..., description="MIME type of the file")
    file_name: str = Field(..., description="Name of the file")

class PDFResponse(BaseModel):
    success: bool = Field(default=True, description="Indicates if the processing was successful")
    message: str = Field(default="Data extracted successfully", description="Descriptive message about the processing outcome")
    data: List[Dict[str, Union[str, int]]] = Field(..., description="List of data lines extracted from the PDF")

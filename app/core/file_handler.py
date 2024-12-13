import PyPDF2
from io import BytesIO

async def get_text_from_pdf(file_data: bytes):
    combined_text = ''
    file = BytesIO(file_data)
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            combined_text += text
    return combined_text
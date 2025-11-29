from pypdf import PdfReader

def read_pdf(file_path: str) -> str:
    """
    A thin wrapper around PyPDF to extract text from a PDF document.
    """
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

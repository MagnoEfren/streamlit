import fitz
import io
from utils.ui import show_error

def compress_pdf(pdf_file):
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        for page in doc:
            page.clean_contents()
        output = io.BytesIO()
        doc.save(output, garbage=4, deflate=True, clean=True)
        doc.close()
        output.seek(0)
        return output.getvalue()
    except Exception as e:
        show_error(f"Error al comprimir el PDF: {str(e)}")
        return None
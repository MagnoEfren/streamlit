import PyPDF2
import io
from utils.ui import show_error

def protect_pdf(pdf_file, password):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        pdf_writer.encrypt(password)
        output = io.BytesIO()
        pdf_writer.write(output)
        output.seek(0)
        return output.getvalue()
    except Exception as e:
        show_error(f"Error al proteger el PDF: {str(e)}")
        return None
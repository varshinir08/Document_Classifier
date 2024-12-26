import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """
    Extracts the heading (first line) from a PDF document using PyMuPDF (fitz).
    """
    try:
        # Open the PDF file
        doc = fitz.open(file_path)

        # Extract text from the first page
        page = doc.load_page(0)  # Load the first page (index 0)
        text = page.get_text("text")  # Get text in a plain format

        # Extract the first line (heading)
        first_line = text.split('\n')[0]

        return first_line if first_line else "No heading found in the document."
    
    except Exception as e:
        return f"Error during text extraction: {str(e)}"

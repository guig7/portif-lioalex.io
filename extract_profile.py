import os
import sys

try:
    from pypdf import PdfReader
except ImportError:
    print("pypdf not found. Please run 'pip install pypdf' first.")
    sys.exit(1)

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return

    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        print("--- START OF PDF CONTENT ---")
        print(text)
        print("--- END OF PDF CONTENT ---")
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    # Using the absolute path provided in context
    pdf_path = r"c:\Users\Alex\Documents\Python\Portifólio_Alex\Profile (1).pdf"
    extract_text_from_pdf(pdf_path)

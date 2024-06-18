import os
import re
from PyPDF2 import PdfReader, PdfWriter

def remove_pages_after_text(pdf_path, regex_pattern, output_path, start_page=10):
    print(f'Starting processing {pdf_path}.')
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    pattern = re.compile(regex_pattern, re.IGNORECASE)
    text_found = False
    
    # Tambahkan halaman pertama tanpa modifikasi
    for page_num in range(min(start_page, len(reader.pages))):
        writer.add_page(reader.pages[page_num])
    
    # Mulai pencarian dari halaman setelah `start_page`
    for page_num in range(start_page, len(reader.pages)):
        page = reader.pages[page_num]
        page_text = page.extract_text()
        if pattern.search(page_text):
            text_found = True
            break
        writer.add_page(page)
    
    if not text_found:
        print(f'Text matching pattern "{regex_pattern}" not found in {pdf_path}.')
    
    with open(output_path, 'wb') as output_pdf:
        writer.write(output_pdf)

def process_pdfs_in_folder(folder_path, regex_pattern, start_page=10):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"modified_{filename}")
            remove_pages_after_text(pdf_path, regex_pattern, output_path, start_page)

# Set the folder path and the regex pattern to search for
folder_path = 'pros'
regex_pattern = r"\b[A-Z]+\.\s*PENDAPAT\s*DARI\s*SEGI\s*HUKUM\b"

# Process all PDFs in the folder
process_pdfs_in_folder(folder_path, regex_pattern, start_page=10)
import os
import re
import fitz  # PyMuPDF

# Path to folder containing PDF files
# file_in_folder = r"C:\\Users\\steve\\pyStuff\\pytesseract\\filein"
file_in_folder = 'filein'

# Check if the folder exists
if not os.path.exists(file_in_folder):
    print(f"Error: The folder '{file_in_folder}' does not exist.")
    exit()

# Establish regex patterns
regex_filename = r'<REGEX STRING>'
regex_ocr = r'LS-\d{5}-\d'

# Set the company name
co_name = 'CMS'

def ocr_core(input_pdf):
    pdf_path = os.path.join(file_in_folder, input_pdf)

    # Open the PDF file using PyMuPDF
    pdf_document = fitz.open(pdf_path)

    text = ""
    # Iterate through each page in the PDF
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    return text

# Iterate through all PDF files in the specified folder
for pdf_file in os.listdir(file_in_folder):
    if pdf_file.endswith(".pdf"):

        # # Extract string from filename
        # regex_filename_match = re.search(regex_filename, pdf_file)
        # regex_filename_result = regex_filename_match.group(1) if regex_filename_match else ''

        # Run OCR to extract string from PDF contents
        pdf_text = ocr_core(pdf_file)
        regex_ocr_matches = re.findall(regex_ocr, pdf_text)
        regex_ocr_result = regex_ocr_matches[0].lower() if regex_ocr_matches else ''

        # Rename the PDF file using variables: regex_filename_result and regex_ocr_result
        new_filename = f"{co_name} {regex_ocr_result}.pdf"
        new_filepath = os.path.join(file_in_folder, new_filename)
        os.rename(os.path.join(file_in_folder, pdf_file), new_filepath)

        print(f"Renamed '{pdf_file}' to '{new_filename}'")
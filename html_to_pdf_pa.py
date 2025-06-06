import os
import subprocess

# Define the wkhtmltopdf command
wkhtmltopdf_command = ['wkhtmltopdf', '--enable-local-file-access']

# Paths to the directories
html_dir = 'target_files/html_output/'
pdf_dir = 'target_files/pdf_output/'

# Ensure the PDF directory exists
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# Get a list of all HTML files in the HTML directory
html_files = os.listdir(html_dir)

# Iterate through each HTML file in the HTML directory
for html_file in html_files:
    # Check if the file is an HTML file
    if html_file.endswith('.html'):
        # Construct the paths to the HTML and PDF files
        html_path = os.path.join(html_dir, html_file)
        pdf_path = os.path.join(pdf_dir, os.path.splitext(html_file)[0] + '.pdf')
        print(f"HTML: {html_path}, PDF: {pdf_path}")

        # Define the command to run
        command = wkhtmltopdf_command + [html_path, pdf_path]
        
        # Run the command
        process = subprocess.run(command, text=True, capture_output=True)
        
        # Print the output of the command
        print(process.stdout)
        
        # Check if the command succeeded
        if process.returncode == 0:
            print(f'Conversion of {html_path} succeeded')
        else:
            print(f'Conversion of {html_path} failed')
            print(f'Error: {process.stderr}')

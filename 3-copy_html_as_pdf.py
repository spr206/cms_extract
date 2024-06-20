#create a docker container with wkhtmltopdf
# docker run -ti --rm --entrypoint sh -v C:\<target_files>:/target_files <image identifier>



import os
import subprocess
import wkhtmltopdf


# Define the Docker command prefix
docker_command_prefix = [
    'docker', 'exec', 'hardcore_sanderson',
    'wkhtmltopdf', '--enable-local-file-access'
]

# Get a list of all files in the /html_output/ directory
html_files = os.listdir('C:\\Users\\steve\\pyStuff\\CMS\\html_output\\')

# Iterate through each html file in the /html_output/ directory
for html_file in html_files:
    # Check if the file is an HTML file
    if html_file.endswith('.html'):
        # Construct the paths to the HTML and PDF files
        html_path = os.path.join('/target_files/html_output/', html_file)
        pdf_path = os.path.join('/target_files/pdf_output/', os.path.splitext(html_file)[0] + '.pdf')

        print({html_path, pdf_path})

        # Define the Docker command to run
        docker_command = docker_command_prefix + [html_path, pdf_path]
        
        # Run the Docker command
        process = subprocess.run(docker_command, text=True, capture_output=True)
        
        # Print the output of the Docker command
        print(process.stdout)
        
        # Check if the command succeeded
        if process.returncode == 0:
            print(f'Conversion of {html_path} succeeded')
        else:
            print(f'Conversion of {html_path} failed')

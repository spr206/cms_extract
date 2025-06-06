import os
import requests
import re
from urllib.parse import unquote

def extract_orderid(url):
    match = re.search(r'orderid=(\d+)', url)
    if match:
        return match.group(1)
    return None

def download_files_from_urls(url_file_path, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(url_file_path, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        url = unquote(url)  # Decode URL-encoded characters
        
        orderid = extract_orderid(url)
        if orderid:
            filename = f"invoice_{orderid}"
        else:
            filename = "unknown"

        pdf_file_path = os.path.join(output_directory, filename + '.pdf')

        print("Downloading:", url)
        try:
            # Add headers to mimic browser behavior
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': '*/*'
            }
            
            response = requests.get(url, headers=headers, allow_redirects=True)
            
            if response.status_code == 200:
                # Check if content appears to be PDF
                if response.content.startswith(b'%PDF-'):
                    with open(pdf_file_path, 'wb') as file:
                        file.write(response.content)
                    print("Download successful:", pdf_file_path)
                else:
                    print(f"Error: Response for {url} is not a PDF file")
            else:
                print(f"Error: Server returned status code {response.status_code}")

        except Exception as e:
            print("Error downloading {}: {}".format(url, str(e)))

url_file_path = 'links.txt'
output_directory = './pdf_output/'
download_files_from_urls(url_file_path, output_directory)
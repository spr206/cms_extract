import os
import requests
import re

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
        orderid = extract_orderid(url)
        if orderid:
            filename = f"orderid_{orderid}"
        else:
            filename = "unknown"

        html_file_path = os.path.join(output_directory, filename + '.html')
        pdf_file_path = os.path.join(output_directory, filename + '.pdf')

        print("Downloading:", url)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(html_file_path, 'wb') as file:
                    file.write(response.content)
                print("Download successful:", html_file_path)

        except Exception as e:
            print("Error downloading {}: {}".format(url, str(e)))

url_file_path = 'links.txt'
output_directory = './html_output/'
download_files_from_urls(url_file_path, output_directory)

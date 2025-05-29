import requests
from dotenv import load_dotenv

import os
from datetime import datetime, timedelta
from urllib.parse import urlparse


def get_file_extension(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path) 
    return os.path.splitext(filename)[1]  

    
def download_image(url, filename, save_dir='images'):
    
    response = requests.get(url)
    response.raise_for_status()

    os.makedirs(save_dir, exist_ok=True)

    extension = get_file_extension(url) 
    file_path = os.path.join(save_dir, f'{filename}{extension}') 

    with open(file_path, 'wb') as file:
        file.write(response.content)
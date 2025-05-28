import requests
from dotenv import load_dotenv

import os
from datetime import datetime, timedelta
from urllib.parse import urlparse


def download_image(url, filename, save_dir='images'):
    
    response = requests.get(url)
    response.raise_for_status()

    os.makedirs(save_dir, exist_ok=True)

    extension = get_file_extension(url) 
    file_path = os.path.join(save_dir, f'{filename}{extension}') 

    with open(file_path, 'wb') as file:
        file.write(response.content)
    

def fetch_spacex_last_launch():
    
    url = "https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a"  
    
    
    response = requests.get(url) 
    response.raise_for_status()

    launch = response.json()
    images = launch.get('links', {}).get('flickr', {}).get('original', [])
    return images 
    

def fetch_nasa_apod_images(api_key, count=30):
    url = "https://api.nasa.gov/planetary/apod"
    images = []
    today = datetime.now()
    days_checked = 0 

    while len(images) < count:

        date = (today - timedelta(days=days_checked)).strftime('%Y-%m-%d')
        params={'api_key': api_key,'date': date}
        
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        if data['media_type'] == 'image':
            images.append(data['url'])
                    
        days_checked += 1 
            
    return images[:count]  


def get_file_extension(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path) 
    return os.path.splitext(filename)[1]  


def download_earth_photos(api_key, num_photos, save_dir='images'):
    earth_url = "https://api.nasa.gov/EPIC/api/natural"
    params = {'api_key': api_key}
    
   
    response = requests.get(earth_url, params=params)
    response.raise_for_status()
    images_info = response.json()
   
    for i, image_info in enumerate(images_info[:num_photos]):
            
        image_date = datetime.strptime(image_info['date'], "%Y-%m-%d %H:%M:%S")
        date_str = image_date.strftime("%Y/%m/%d")
        image_filename = image_info['image']  
        photo_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{image_filename}.png"
        download_image(photo_url, f'earth_photo_{i + 1}', save_dir)            
        

def main():

    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    
    spacex_images = fetch_spacex_last_launch()  

    apod_images = fetch_nasa_apod_images(api_key)  
    
    for index, image_url in enumerate(apod_images, start=1):
        filename = f'nasa_image{index}'  
        download_image(image_url, filename) 


    for index, image_url in enumerate(spacex_images, start=1):
        filename = f'spacex{index}.jpg'  
        download_image(image_url, filename) 

    download_earth_photos(api_key, num_photos=5)


if __name__ == "__main__":
    main()


                






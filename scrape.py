import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
#https://www.mangabox.me/reader/254958/episodes/116934/
URL = "https://www.mangabox.me/reader/166016/episodes/115689/"
getURL = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(getURL.text, 'html.parser')

images = soup.find_all('img')
resolvedURLs = []

for image in images:
    src = image.get('src')
    resolvedURLs.append(requests.compat.urljoin(URL, src))

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Generate a timestamp

folder_name = f"images/images_{timestamp}"  # Create a subfolder name with the timestamp

os.makedirs(folder_name, exist_ok=True)  # Create the subfolder

for image_url in resolvedURLs:
    response = requests.get(image_url)
    if response.status_code == 200:
        filename = image_url.split('/')[-1][:7]  # Get the first 7 characters of the filename
        with open(os.path.join(folder_name, filename), 'wb') as file:
            file.write(response.content)


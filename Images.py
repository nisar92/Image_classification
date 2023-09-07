import os

# selenuim 4
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

import requests
import io
from PIL import Image

def get_urls(query:str,delay:int)->set:
    images_urls = set()
    browser=webdriver.Chrome()
    browser.get('https://images.google.com/')
    search_box=browser.find_element(By.CSS_SELECTOR,'#APjFqb.gLFyf')
    search_box.send_keys(query)
    search_box.submit()
    
    time.sleep(delay)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(delay)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(delay)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    thumbnails = browser.find_elements(By.CLASS_NAME,"Q4LuWd")
    for image in thumbnails:
        if image.get_attribute('src'):
            images_urls.add(image.get_attribute('src'))
    return images_urls




'''
def setup_browser() -> webdriver.Chrome:
    broswer=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    broswer.get('https://images.google.com/')
    time.sleep(2)

    return broswer
'''

def download_images(query,delay,no_of_images):
    images_urls=get_urls(query,delay)
    try:
        if images_urls is not None:
            os.makedirs(query,exist_ok=True)
            for i,url in enumerate(images_urls):
                if i==no_of_images:
                    break
                image_content = requests.get(url).content
                image_file = io.BytesIO(image_content)
                image= Image.open(image_file)
                file_path=os.path.jion(os.path.curdir,query,str(i)+".jpg")

                with open(file_path,'wb') as f:
                    image.save(f,"JPEG")
            return 'images download successfully'
        else:
            return "No Images Found"
    except Exception as e:
        return e

download_images('Narendra modi',2,5)

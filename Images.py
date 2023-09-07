import os

# selenuim 4
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

def get_urls(query:str,delay:int)->set:
    images_urls=set()
    browser=webdriver.Chrome()
    browser.get('https://images.google.com/')
    search_box=browser.find_element(By.CSS_SELECTOR,'#APjFqb.gLFyf')
    search_box.send_keys(query)
    search_box.submit()
    time.sleep(delay)
    return browser

'''
def setup_browser() -> webdriver.Chrome:
    broswer=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    broswer.get('https://images.google.com/')
    time.sleep(2)

    return broswer
'''
get_urls('Narendra modi',2)

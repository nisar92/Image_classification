import os

# selenuim 4
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser() -> webdriver.Chrome:
    broswer=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    broswer.get('https://images.google.com/')
    time.sleep(2)

    return broswer

    setup_browser()

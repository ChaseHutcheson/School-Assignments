from pyautogui import scroll, sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from parsel import Selector
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.google.com/maps/search/bars+near+NY,+USA/@40.7443439,-74.0197995,13z'
driver.get(url)

scrollbar = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]")
scrollbar.click()

for i in range(2000):
    scrollbar.send_keys(keys.Keys.ARROW_DOWN)
    scrollbar.send_keys(keys.Keys.ARROW_DOWN)
    scrollbar.send_keys(keys.Keys.ARROW_DOWN)
   

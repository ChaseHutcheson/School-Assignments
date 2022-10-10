from pyautogui import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def submitform1():
    web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
    web.get('https://docs.google.com/forms/d/e/1FAIpQLScXNbdAs0HF9d5DHFXo1qTjK9wMSrG1nBCb1lzFw0tkJUGvOw/viewform')
    sleep(1)

   
    text_area1 = web.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    text_area2 = web.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    CheckBox1 = web.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div")
    submit = web.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")

    text_area1.send_keys("hutcheson_chase@student.mahoningctc.com")
    text_area2.send_keys("Hutcheson Chase")
    CheckBox1.click()
    submit.click()


submitform1()
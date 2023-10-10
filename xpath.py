# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#se initializeaza un obiect driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#se acceseaza website-ul dorit
driver.get("https://www.saucedemo.com/v1/index.html")

#spre deosebire de time.sleep(3), implicitly_wait(3) efectueaza o actiune activ
# timp de 3 secunde spre deosebire de time.sleep() care suspenda orice activitate
driver.implicitly_wait(3)

#accesez 'username' prin calea absoluta xpath
username_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/input[@value='standard_user']")
username_field.send_keys("standard_user")

time.sleep(2)
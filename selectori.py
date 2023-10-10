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

#vreau sa identific 'username' dupa atributul 'name'
username_field = driver.find_element(By.NAME, "user-name")

#in campul 'username' vreau sa introduc text
username_field.send_keys("standard_user")
time.sleep(1)

#vreau sa identific campul 'password' dupa atributul 'name'
password_field = driver.find_element(By.NAME, "password")

#in campul 'password' vreau sa introduc text
password_field.send_keys("secret_sauce")
time.sleep(1)

#vreau sa gasesc butonul 'login' si sa il accesez
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

#prin time.sleep se ingheaza cadrul pentru cate secunde se specifica in paranteze
time.sleep(5)

#se inchide tab-ul curent prin accesarea metodei close a driver-ului
# driver.close()

#se inchide fereastra curenta(toate taburile)
driver.quit()
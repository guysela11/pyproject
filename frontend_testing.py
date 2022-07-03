from selenium import webdriver

# Windows:
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def res():
    driver = webdriver.Chrome(service=Service("C:/Users/Guy/Downloads/ChromeDriver.exe"))
    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1:5001/users/get_user_name/2")
    string = driver.find_element(By.TAG_NAME, value="h1").text
    print (string)
    driver.quit()

res()
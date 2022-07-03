import pymysql
import requests
from selenium import webdriver

# Windows:
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def res1():
    res = requests.post('http://127.0.0.1:5000/users/1', json={'user_name':"John"})
    if res.ok:
        print(res.json())
    else: raise Exception("Test failed")

def res2():
    res = requests.get('http://127.0.0.1:5000/users/3')
    if res.ok:
        print(res.json())
    else: raise Exception("Test failed")

def res3():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='5Lh6rumTTn', passwd='ZXUyn2QkhL', db='5Lh6rumTTn')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM 5Lh6rumTTn.users WHERE user_id = (%s)", 1)
    except:
        raise Exception("Test failed")
    value = cursor.fetchall()
    for r in value:
        print (r)
    conn.commit()
    cursor.close()
    conn.close()

def res4():
    driver = webdriver.Chrome(service=Service("C:/Users/Guy/Downloads/ChromeDriver.exe"))
    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1:5001/users/get_user_name/2")
    try:
        string = driver.find_element(By.TAG_NAME, value="h1").text
    except:
        raise Exception("Test failed")
    print (string)
    driver.quit()

res1()
res2()
res3()
res4()
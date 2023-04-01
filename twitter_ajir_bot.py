from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests
import random
  
username = input("USER: ")
#'ajir_bot'
password = input("PASSWORD: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://twitter.com/login")
sleep(20)
print("Login to the site ....")
userinput = driver.find_element(By.NAME, "text")
userinput.send_keys(username)
userinput.send_keys(Keys.ENTER)
sleep(20)
print("Done user")
print("email submitted")

sleep(2)
passinput= driver.find_element(By.NAME, "password")
passinput.send_keys(password)
passinput.send_keys(Keys.ENTER)
print("Done password")
print("password submitted\nsuccess login")
sleep(30)
while True:
    sleep(10800) #كل 3 ساعات تغريد
    #الساعه الواحده =3600ثانيه
#######################################################################
    tweetbox = driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
    tweetbox.click()
    sleep(30)
    req = requests.get(url = 'https://ayah.nawafdev.com/api/dekr?types=t').json()
    tsbyh = (req['content'])
    ###########################################
    #أدعية قرآنية
    req1 = requests.get(url = 'https://ayah.nawafdev.com/api/dekr?types=qd').json()
    adyh = (req1['content'])
    #########################################
    req2 = requests.get(url = 'https://ayah.nawafdev.com/api/dekr').json()
    adyh2 = (req2['content'])
    number_list = [tsbyh, adyh,adyh2]
    tweetbox.send_keys(random.choice(number_list))
    sleep(30)
    button = driver.find_element(By.CSS_SELECTOR,"div[data-testid='tweetButtonInline']")
    button.click () 
    ############################################################
    sleep(20)

    
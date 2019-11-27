from time import sleep
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver import ActionChains
import string
import uuid
# options = Options()
import os

       
       
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}


chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
# chrome_options.add_argument('--no-sandbox') # Bypass OS security model
chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
# chrome_options.add_argument('start-maximized') #
# chrome_options.add_argument('disable-infobars')
# chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'/usr/local/bin/chromedriver')

# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\chromedriver.exe')
driver.implicitly_wait(50)
# driver.get("http://127.0.0.1:35555/htmlchat/123flashchat.html")
driver.get("http://www.chat.chatkaro.in/chatonlineroom/123flashchat.html")
# driver.get("http://127.0.0.1:35555/htmlchat/123flashchat.html")
# driver.get("http://127.0.0.1:35555/htmlchat/123flashchat.html?init_host_h=pars.yekparsi.ir&init_port_h=35556")

time.sleep(4)
driver.find_element_by_id("topcmm-123flashchat-loginview-username-input").send_keys("hohhoho")
driver.find_element_by_id("topcmm-123flashchat-loginview-guest-checkbox").send_keys(Keys.SPACE)

driver.find_element_by_id("topcmm-123flashchat-loginview-username-input").send_keys(Keys.ENTER)
time.sleep(4)
elem = driver.find_element_by_xpath("//*[@id='topcmm-123flashchat-roomlist-container']/div[1]")
elem.click()
time.sleep(4)
# assert 'Chat Room - Powered by 123 Flash Chat' in driver.title
print (driver.title)
# time.sleep(2)
# TASKKILL /F /IM chromedriver.exe /T
# cd /
# python C:\Users\Administrator\Desktop\pz.py

driver.execute_script("document.getElementById('topcmm-123flashchat-main-send-msg-btn').addEventListener('click', function(){document.getElementById('topcmm-123flashchat-main-message-input').value =Number.parseInt(Math.floor(Math.random() * 1000));});")
time.sleep(4)

while True:
    # time.sleep(5)
    
    
    # driver.find_element_by_id("topcmm-123flashchat-mainview-top-settings-btn").click()
    # driver.find_element_by_id("topcmm-123flashchat-settings-menuitem-signin").click()
    
    
    
    driver.execute_script("document.getElementById('topcmm-123flashchat-mainview-top-settings-btn').click();")
    # time.sleep(0.1)
    driver.execute_script("document.getElementById('topcmm-123flashchat-settings-menuitem-signin').click();")
    time.sleep(0.1)
    # driver.execute_script("document.getElementById('topcmm-123flashchat-sign-in-guest-checkbox-block').style='display: show';")
    # time.sleep(0.2)
    driver.execute_script("document.getElementById('topcmm-123flashchat-loginview-guest-checkbox').click();")
    # time.sleep(0.2)
    driver.execute_script("document.getElementById('topcmm-123flashchat-loginview-username-input').value = Math.random().toString(24).substr(2, 12);")
    # time.sleep(0.1)
    driver.execute_script("document.getElementById('topcmm-123flashchat-loginview-login-btn').click();")
    time.sleep(0.1)
    # driver.execute_script("document.getElementById('topcmm-123flashchat-main-message-input').value = Math.random().toString(24).substr(2, 2);")
    driver.execute_script("document.getElementById('topcmm-123flashchat-main-send-msg-btn').click();")
    # time.sleep(0.1)
    time.sleep(0.2)
    
    

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:33:12 2020

@author: engin aybey
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, sys

waitTime=1000
username=sys.argv[1]
paswrd=sys.argv[2]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://192.168.1.1/")
txbx = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "username"))
                )
txbx.clear()
txbx.send_keys(username)

txbx = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "userpassword"))
                )
txbx.clear()
txbx.send_keys(paswrd)
button = WebDriverWait(driver, waitTime).until(
                EC.presence_of_element_located((By.ID, "loginBtn"))
                )
driver.execute_script("arguments[0].click();", button)

try:
    button = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, "zyMenu-maintenance"))
                    )
    
    hover = ActionChains(driver)
    hover.move_to_element(button)
    hover.perform()
except:
    driver.refresh()
    button = WebDriverWait(driver, waitTime).until(
                        EC.visibility_of_element_located((By.ID, "zyMenu-maintenance"))
                        )
        
    hover = ActionChains(driver)
    hover.move_to_element(button)
    hover.perform()

button = WebDriverWait(driver, waitTime).until(
                EC.visibility_of_element_located((By.ID, "Reboot"))
                )
button.click()

driver.switch_to.frame("mainFrame")
    
button = WebDriverWait(driver, waitTime).until(
                EC.visibility_of_element_located((By.ID, "reboot_btn"))
                )
button.click()
time.sleep(10)
driver.close()
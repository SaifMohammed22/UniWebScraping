from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

USERCODE = os.getenv("USERCODE")
PASSWORD = os.getenv("PASSWORD")


# Defining my credentials
username = USERCODE
password = PASSWORD

driver = webdriver.Firefox()
driver.get("https://chreg.eng.cu.edu.eg/")

driver.find_element(By.ID, "txtUsername").send_keys(username)
driver.find_element(By.ID, "txtPassword").send_keys(password)
driver.find_element(By.ID, "ext-gen24").click()


time.sleep(4)
driver.quit()

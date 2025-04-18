from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from pprint import pprint 
import pandas as pd


options = webdriver.FirefoxOptions()
options.add_argument("- incognito")


def create_webdriver():
    return webdriver.Firefox(options=options)

try:
    print("Starting browser...")
    browser = create_webdriver()
    print("Browser started, accessing URL...")
    # browser.get("https://github.com/collections/machine-learning")
    browser.get("https://chreg.eng.cu.edu.eg/SemesterStatistics.aspx?f=3")
    print("Browser accessed successfully.")

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".application-main")))
except Exception as e:
    print(f"Error occurred: {e}")



def select(name, index):
    select_something = Select(browser.find_element(By.NAME, name))
    select_something.select_by_index(index)


select("ddl_Cyear", 1)
select("ddl_Dept", 13)
select("ddl_ClassId", 1)
select("ddl_Term", 2)

print("*" * 30)


stats = browser.find_element(By.ID, 'dgv_Statistcs')
# pprint(stats.text)

df = pd.DataFrame(stats.text)
print(df)

from os import times
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
PATH = "C:\webDrivers\bin\chromedriver"
driver = webdriver.Firefox()
driver.get("https://www.google.com")
print(driver.title)
search = driver.find_element_by_name("q")
search.send_keys("ff")
search.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rso"))
    )
    gclasses = element.find_elements_by_class_name("g")
    for gclass in gclasses:
        getext = gclass.find_element_by_tag_name("a")
        print(getext.text)
        print("________________________________________")
        
    print("________________________________________")
    print(element.text)
    print("________________________________________") 
except:
    driver.quit()
time.sleep(8)
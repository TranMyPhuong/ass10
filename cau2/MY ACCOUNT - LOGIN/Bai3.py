from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time


chrome_driver_path = "G:\seledriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
        
driver.find_element_by_link_text("My Account").click()
time.sleep(5)
email = driver.find_element_by_id("username")
email.send_keys("Nguyenv@yahoo.com")
time.sleep(5)

driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()

time.sleep(5)

driver.close()

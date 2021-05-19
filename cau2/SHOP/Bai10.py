from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time


chrome_driver_path = "G:\seledriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
        
driver.find_element_by_link_text("Shop").click()

driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/ul/li[3]/a[2]")).click()
time.sleep(2)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/ul/li[3]/a[3]")).click()
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/a")).click()
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[3]/div[2]/div/div/input[1]")).click()
time.sleep(5)


driver.close()

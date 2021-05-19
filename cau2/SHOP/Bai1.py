from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time


chrome_driver_path = "G:\seledriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
        
driver.find_element_by_link_text("Shop").click()


left = driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/aside/div[2]/form/div/div[1]/span[2]"))

actions = ActionChains(driver)
actions.click_and_hold(left).move_by_offset(-24,30).release().perform()
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/aside/div[2]/form/div/div[2]/button")).click()
time.sleep(5)


driver.close()

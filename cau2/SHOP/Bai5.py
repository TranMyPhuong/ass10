from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time


chrome_driver_path = "G:\seledriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
        
driver.find_element_by_link_text("Shop").click()

select = Select(driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/form/select")))
select.select_by_value('date')

time.sleep(5)


driver.close()

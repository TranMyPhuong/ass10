
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time


chrome_driver_path = "G:\seledriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
        
driver.find_element_by_link_text("Shop").click()

driver.find_element_by_xpath(("//img[@src='http://practice.automationtesting.in/wp-content/uploads/2017/01/color-logo-original.png']")).click()
        
count =  driver.find_elements_by_xpath("//*[@id='themify_builder_content-22']/div[2]/div/div/div/div/div[2]//div[contains(@class, 'sub_column')]")
s= len(count)
      
print("Home page has:", s, " Arrivals")

driver.find_element_by_xpath(("//a[@href='http://practice.automationtesting.in/product/selenium-ruby/']")).click()

driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div[3]/ul/li[1]/a")).click()

time.sleep(5)

driver.close()



   
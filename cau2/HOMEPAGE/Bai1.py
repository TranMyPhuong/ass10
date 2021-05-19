import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time


import time

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "G:\seledriver\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("http://practice.automationtesting.in/")
        
        driver.find_element_by_link_text("Shop").click()
        
        driver.find_element_by_xpath(("//img[@src='http://practice.automationtesting.in/wp-content/uploads/2017/01/color-logo-original.png']")).click()
        

        count =  driver.find_elements_by_xpath("//div[@id='n2-ss-6']//div[@data-slide-duration='0']") 

                  
        
        
        self.assertTrue(len(count) == 3)

        
        
if  __name__ == "__main__":
    unittest.main()
   
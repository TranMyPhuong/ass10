from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time


chrome_driver_path = "G:\seledriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
        
driver.find_element_by_link_text("My Account").click()
time.sleep(3)
email = driver.find_element_by_id("username")
email.send_keys("Nguyenv@yahoo.com")
time.sleep(3)
passs = driver.find_element_by_id("password")
passs.send_keys("3KVfE7BvLaTc@7E")
time.sleep(3)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")).click()

time.sleep(2)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/nav/ul/li[4]/a")).click()

time.sleep(2)
driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div/div[2]/header/a")).click()


firstname = driver.find_element_by_id("shipping_first_name")
firstname.send_keys("Binh")

lastname = driver.find_element_by_id("shipping_last_name")
lastname.send_keys("Nguyen")

company = driver.find_element_by_id("shipping_company")
company.send_keys("Nguyenv")


add = driver.find_element_by_id("shipping_address_1")
add.send_keys("do em biet anh dang o dau")

add2 = driver.find_element_by_id("shipping_address_2")
add2.send_keys("ok em luon")

city = driver.find_element_by_id("shipping_city")
city.send_keys("Hanoi")

note = driver.find_element_by_id("shipping_postcode")
note.send_keys("123456")

driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/form/p[10]/input[1]")).click()

time.sleep(5)

driver.close()



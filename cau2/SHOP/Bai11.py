from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

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

firstname = driver.find_element_by_id("billing_first_name")
firstname.send_keys("Binh")

lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Nguyen")

company = driver.find_element_by_id("billing_company")
company.send_keys("Nguyenv")

email = driver.find_element_by_id("billing_email")
email.send_keys("Nguyenv@yahoo.com")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("0123456789")

time.sleep(3)
add = driver.find_element_by_id("billing_address_1")
add.send_keys("do em biet anh dang o dau")

add3 = driver.find_element_by_id("billing_address_2")
add3.send_keys("do em, biet anh, dang, o dau, day")

add2 = driver.find_element_by_id("billing_postcode")
add2.send_keys("12345")

city = driver.find_element_by_id("billing_city")
city.send_keys("Hanoi")

note = driver.find_element_by_id("order_comments")
note.send_keys("do de vo")

driver.find_element_by_id("place_order").click()

time.sleep(8)

driver.close()

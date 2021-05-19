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

driver.find_element_by_xpath(("//img[@src='http://practice.automationtesting.in/wp-content/uploads/2017/01/Thinking-in-HTML-300x300.jpg']")).click()
time.sleep(2)

driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div[2]/form/button")).click()

driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div[1]/a")).click()
time.sleep(2)

driver.find_element_by_xpath(("//a[@href='http://practice.automationtesting.in/checkout/']")).click()

driver.find_element_by_xpath(("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/a")).click()

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

add = driver.find_element_by_id("billing_address_1")
add.send_keys("do em biet anh dang o dau")

add2 = driver.find_element_by_id("billing_postcode")
add2.send_keys("12345")

city = driver.find_element_by_id("billing_city")
city.send_keys("Hanoi")

note = driver.find_element_by_id("order_comments")
note.send_keys("do de vo")

driver.find_element_by_id("place_order").click()


time.sleep(8)

driver.close()

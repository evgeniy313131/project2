#                                  Shop: отображение страницы товара
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver.get("https://practice.automationtesting.in/")
My_Account = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='My Account']")))
My_Account.click()

UserName_email_Adress = driver.find_element(By.ID, "username")
UserName_email_Adress.send_keys("Evgeniy313131@gmail.con")
time.sleep(5)

password_User = driver.find_element(By.ID, "password")
password_User.send_keys("!!@@qwerty313131ZoRo<>!!!")
time.sleep(7)
My_shop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Shop']")))
My_shop.click()
time.sleep(7)

html_link = driver.find_element(By.XPATH, "//a[@href='https://practice.automationtesting.in/product-category/html/']")
html_link.click()
time.sleep(10)


book_title = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.CLASS_NAME, "product_title")))
assert book_title.text == "HTML5 Forms", f"Expected title 'HTML5 Forms' but got '{book_title.text}'"
print("Test passed: Book title is correct.")



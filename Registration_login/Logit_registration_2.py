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

My_Account = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='My Account']")))
My_Account.click()

UserName_email_Adress = driver.find_element(By.ID, "username")
UserName_email_Adress.send_keys("Evgeniy313131@gmail.con")
time.sleep(5)

password_User = driver.find_element(By.ID, "password")
password_User.send_keys("!!@@qwerty313131ZoRo<>!!!")
time.sleep(5)


# login_element = driver.find_element(By.XPATH, "//input[@name='login']")
# login_element.click()
# time.sleep(5)

logout_element = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.XPATH, "//input[@name='login']")))
assert logout_element.is_displayed(), "Logout button is not displayed"
print("Login successful. Logout button is displayed.")
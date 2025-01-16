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
My_Account = android_quick_start_guide = WebDriverWait(driver, 15).until(
 EC.visibility_of_element_located((By.XPATH, "//img[@alt='Android Quick Start Guide']")))
My_Account.click()

Register_User = driver.find_element(By.ID, "reg_email")
Register_User.send_keys("Evgeniy313131@gmail.con")
time.sleep(5)

password_User = driver.find_element(By.ID, "reg_password")
password_User.send_keys("!!@@qwerty313131ZoRo<>!!!")
time.sleep(5)

register_button = driver.find_element(By.CSS_SELECTOR, "input[value='Register']")
register_button.click()
# submit_button = driver.find_element(By.ID, "woocommerce-register-nonce")
# submit_button.click()
time.sleep(5)
driver.quit()


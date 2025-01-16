#                          Shop: сортировка товаров
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

sortirovka = WebDriverWait(driver, 20).until(
EC.visibility_of_element_located((By.CLASS_NAME, "orderby")))
select = Select(sortirovka)
default_value = select.first_selected_option.get_attribute("value")
assert default_value == "menu_order", f"{default_value}"
print("Сортировка по умолчанию.")

# сортировка
select.select_by_value("от большему к меньшему")

sort_selector_updated = WebDriverWait(driver, 20).until(
EC.visibility_of_element_located((By.CLASS_NAME, "orderby")))
select = Select(sort_selector_updated)

# Проверяе от большей к меньшей
updated_value = select.first_selected_option.get_attribute("value")
assert updated_value == "price-desc", f"{updated_value}"
print("Тест пройден")



#  Shop: отображение, скидка товара
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

# клик  Android Quick Start Guide
android_quick_start_guide = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='Android Quick Start Guide']")))
android_quick_start_guide.click()
time.sleep(7)
# Проверка старой цены
old_price = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".price")))
assert "₹600.00" in old_price.text, f" получаем цену '{old_price.text}'"
print("Test passed: Old price is correct.")

# 6. Добавьте тест, что содержимое новой цены = "₹450.00"
print("Ожидание новой цены...")
new_price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'amount')]")))

assert "₹450.00" in old_price.text, f" Получаем цену '{old_price.text}'"
print("Тест пройден.")

book_cover = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single")))
book_cover.click()

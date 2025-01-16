#                         проверка цены в корзине
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
import unittest

driver.get("https://practice.automationtesting.in/")
time.sleep(7)
My_shop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Shop']")))
My_shop.click()
# добавим книгу
element_HTMl = driver.find_element(By.XPATH, "//a[@href='/shop/?add-to-cart=182']")
element_HTMl.click()
time.sleep(10)

# количество товаров равна 1
cart_count = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".cartcontents"))
)
cart_price = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".amount")))

# Проверяем цену
Quantity = driver.find_element(By.CSS_SELECTOR,'.wpmenucart-contents>span.cartcontents')
Quantity_text = Quantity.text
Amount = driver.find_element(By.CSS_SELECTOR,'.wpmenucart-contents > span.amount')
Amount_text = Amount.text
assert Quantity_text == "1 Item"
assert Amount_text == "₹180.00"
Basket_btn = driver.find_element(By.ID,"wpmenucartli")
Basket_btn.click()
time.sleep(5)
Subtotal = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Price'] .woocommerce-Price-amount"), "₹180.00"))
Total = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹183.60"))


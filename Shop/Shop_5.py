# Shop: работа в корзине
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
# скрол 300
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(10)
# добавим два товара в корзину
element_HTMl = driver.find_element(By.XPATH, "//a[@href='/shop/?add-to-cart=182']")
element_HTMl.click()
time.sleep(10)
element_JS = driver.find_element(By.XPATH, "//a[@href='/shop/?add-to-cart=180']")
element_JS.click()
time.sleep(10)
# заходим в корзину
cartcontents = element_JS = driver.find_element(By.CLASS_NAME, "cartcontents")
cartcontents.click()
time.sleep(10)

element_One = driver.find_element(By.XPATH,  "//a[contains(@class, 'remove')]")
element_One.click()


  # Добавлено время ожидания перед Undo
time.sleep(7)
undo_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Undo')]")))  # Поиск по тексту)
time.sleep(5)

quantity_field = driver.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(1) .product-quantity input")
quantity_field.clear()  # Очистить поле
quantity_field.send_keys("3")
time.sleep(10)


# 8. Нажмите на кнопку "UPDATE BASKET"
update_button = driver.find_element(By.XPATH, "//input[@name='update_cart']")
update_button.click()

# Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
time.sleep(1)  # Необходимо, чтобы обновилась страница
updated_quantity = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']"))).get_attribute("value")

#  10. Нажмите на кнопку "APPLY COUPON"
time.sleep(5)  # Добавлено время ожидания перед нажатием
apply_coupon_button = driver.find_element(By.XPATH, "//input[@name='apply_coupon']")
apply_coupon_button.click()
time.sleep(5)
#
# # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
time.sleep(1)  # Добавлено время ожидания для появления сообщения
error_message = driver.find_element(By.CLASS_NAME, "woocommerce-error").text
assert error_message == "Please enter a coupon code.", f"Expected error message to be 'Please enter a coupon code.', but got '{error_message}'"
print("Test passed: Correct error message displayed.")


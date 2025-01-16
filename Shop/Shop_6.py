#                            Shop: цены в корзине
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
My_Account = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='My Account']")))
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
# добавим  товар в корзину
element_HTMl = driver.find_element(By.XPATH, "//a[@href='/shop/?add-to-cart=182']")
element_HTMl.click()
time.sleep(10)
# заходим в корзину
cartcontents = element_JS = driver.find_element(By.CLASS_NAME, "cartcontents")
cartcontents.click()
time.sleep(10)

#  "PROCEED TO CHECKOUT"
Proceed_Checkout = driver.find_element(By.CLASS_NAME, "wc-forward")
Proceed_Checkout.click()
# ==================================обятельные поля==============================
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billing_first_name"))).send_keys("Evgeniy")
time.sleep(10)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billing_last_name"))).send_keys("Semenov")
time.sleep(5)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billing_phone"))).send_keys("89009009000")
time.sleep(10)

Email = driver.find_element(By.ID,"billing_email")
Email.send_keys("Evgeniy313131@gmail.con")
time.sleep(5)
# ===================================================================================================
#
# =============================== Поле ввода Страна Россия=====================================
Country = driver.find_element(By.CSS_SELECTOR, ".select2-arrow>b")
Country.click()
time.sleep(5)

Country_search = driver.find_element(By.ID, "s2id_autogen1_search")
Country_search.send_keys("Russia")

Country_choose = driver.find_element(By.CSS_SELECTOR,".select2-match")
Country_choose.click()
driver.execute_script("window.scrollTo(0, 400);")
# ============================================================================
street = driver.find_element(By.XPATH, "//input[@placeholder='Street address']")
street.send_keys("Xuzangaia 7")
time.sleep(5)

City = driver.find_element(By.XPATH,"//input[@placeholder='Street address']")
City.send_keys("Cheboksari")
time.sleep(5)

State = driver.find_element(By.XPATH,"//input[@placeholder='Apartment, suite, unit etc. (optional)']")
State.send_keys("Cheboksari")
time.sleep(5)

# Zip = driver.find_element(By.ID , "billing_postcode_field")
# Zip.send_keys("420015")
# time.sleep(5)
# Zip = driver.find_element (By.TAG_NAME, "[name='billing_postcode']")
Zip = driver.find_element(By.XPATH, "//input[@name='billing_postcode']")
Zip.send_keys("111999")
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)
Check = driver.find_element(By.ID, "payment_method_cheque")
Check.click()
Place_order = driver.find_element(By.ID, "place_order")
Place_order.click()
time.sleep(5)

Order_Notes = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'),
                                     'Thank you. Your order has been received.'))
Payment_Method = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tfoot > tr:nth-child(3) > td'), 'Check Payments'))
print("автоматизация пройдена!!!")




# Order_Notes = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element(((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.')))
# Payment_Method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))
#

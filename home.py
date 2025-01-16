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
driver.execute_script("window.scrollTo(0, 600);")
time.sleep(10)
# клик на кнопку
selenium_ruby = driver.find_element(By.CSS_SELECTOR, "h3")
selenium_ruby.click()
time.sleep(10)
# вкладка "REVIEWS"
reviews = driver.find_element(By.CLASS_NAME, "reviews_tab")
reviews.click()
time.sleep(10)
# ставим звезды
star5 = driver.find_element(By.CLASS_NAME, "star-5")
star5.click()
time.sleep(10)
# пишем в поле "Review" Nice book!
review = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "comment")))
review.send_keys("Nice book!")  # Сообщение
time.sleep(5)
# Имя
name = driver.find_element(By.ID, "author")
name.send_keys("Evgeniy")  # Введите ваше имя здесь
time.sleep(5)
# Email
email = driver.find_element(By.ID, "email")
email.send_keys("Evgeniy313131@gmail.con")  # Введите ваш email здесь
time.sleep(5)
# клик
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()
time.sleep(5)
driver.quit()

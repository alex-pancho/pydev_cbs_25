# ui testing
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Chrome()

# Відкриття веб-сторінки
driver.get("http://localhost:8000")

# Робота з веб-елементами і виконання дій на сторінці
# Знаходження елемента за ID
user_field = driver.find_element(By.ID, "username")
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")
# user_field = driver.find_element(By.XPATH, "//input[@id='username']")
# pass_field = driver.find_element(By.XPATH, "//input[@id='password']")

user_field.send_keys("Hello")
# Знаходження елемента за XPath з вказанням значення
li_el2 = driver.find_element(By.XPATH, "//li[.='Елемент списку 2']")
print(li_el2.text)
# Знаходження елемента за XPath з вказанням iндексу
li_el2_idx = driver.find_element(By.XPATH, "//li[2]")
print(li_el2.text)

li_elements = driver.find_elements(By.TAG_NAME, "li")

# Пошук конкретного елемента серед отриманих
for li in li_elements:
    # пошук може бути повiльним якщо елементiв багато
    if li.text == "Елемент списку 2":
        # Знайдено потрібний елемент
        print("Знайдено елемент:", li.text)
        break

# Закриття браузера
time.sleep(2)
driver.quit()
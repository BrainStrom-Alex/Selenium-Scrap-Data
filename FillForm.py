from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

name = driver.find_element(By.NAME, value="fName")
name.send_keys("Alex")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Verma")

email = driver.find_element(By.NAME, value="email")
email.send_keys("testing.brainstrom@gmial.com")

button = driver.find_element(By.CSS_SELECTOR, value="#signup-form button")
button.click()
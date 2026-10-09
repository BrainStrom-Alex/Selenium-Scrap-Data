from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_dict = {}
for i in range(0, 5):
    event_dict[f"{i}"] = {
        "date": times[i].text,
        "name": events[i].text,
    }

print(event_dict)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/CanaKit-Raspberry-Pi-Starter-Kit/dp/B0CRSNCJ6Y/ref=sr_1_14?crid=QSXKT4BRC3SB&dib=eyJ2IjoiMSJ9.EIRWMNAsT_JPS2JI4yVop4ZMwqx-v7yNMLhIU1tW4gjb9W-qOi5simg3Psis1wrjE0OE8CqQXkNEj3QMjVQXx4pM-hWNWy77_sbubNz8QSNnhv0bBuAAzvhpvmNYT4uzDqZYyj6SgESWu6IaCtOU7zkYngIAr6mRc3Ul-cMitjTUVEYcR3cCeCanWnXHmiU487gl15a5bPS2CBFCaRCQv-Jqb3RiMWPMcHMs8v6aGrw.q6mVtlZTmN1RXFoDdZsqGEGpGriFkxrp97tBjvq_vw4&dib_tag=se&keywords=raspberry%2Bpi%2B5&qid=1791561169&sprefix=resber%2Caps%2C260&sr=8-14&th=1")

driver.get("https://www.python.org/")

# price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_paisa = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_rupee}.{price_paisa}")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.text)

button = driver.find_element(By.ID, value="submit")

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)
link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[5]/ul/li[3]/a')
print(link.text)

driver.quit()
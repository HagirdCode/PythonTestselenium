import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.flipkart.com/")

cart_button = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3RX0a-")
    )
)
cart_button.click()
time.sleep(5)

driver.quit()
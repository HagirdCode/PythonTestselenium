import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.flipkart.com/")

seller_button = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[2]/div[4]/div/a[2]")
    )
)
seller_button.click()
time.sleep(5)

driver.quit()
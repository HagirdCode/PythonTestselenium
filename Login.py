import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.flipkart.com/")


login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_1TOQfO"))
    )
login_button.click()


mobile_number_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/form/div[1]/input")
            
    )
)
mobile_number_field.clear()
mobile_number_field.send_keys("8010481331")


otp_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "LSOAQH"))
    )
otp_button.click()

    # Wait for OTP manually (automation of OTP is restricted)
time.sleep(10)

driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

STEP_DELAY = 10

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver,10)

    username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    username.send_keys("standard_user")
    time.sleep(STEP_DELAY)

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(STEP_DELAY)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(STEP_DELAY)

    wait.until(EC.url_contains("inventory"))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    print("Login passed")
    print("Current URL:", driver.current_url)

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  
    try:
        test_login(driver)

        print("Leaving browser open for observation when test is finish")
        time.sleep(10)  
    finally:
        driver.quit()

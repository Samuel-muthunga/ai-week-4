from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid login
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("correctpass")
driver.find_element(By.ID, "login-btn").click()

# Check result
assert "Dashboard" in driver.page_source

driver.quit()

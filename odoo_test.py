from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# importar wait de selenium
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Edge()
driver.get("http://localhost:8070")
#assert "Odoo" in driver.title
wait = WebDriverWait(driver, 10)

email = wait.until(EC.element_to_be_clickable((By.ID, "login")))
email.send_keys("criz-Odoo_dev@gmail.com")
password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
password.send_keys("admin")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

driver.implicitly_wait(4000)

apps_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu-xmlid='state.estate_menu_root']")))
apps_list.click()
while True: pass

driver.quit()
# Conversaciones
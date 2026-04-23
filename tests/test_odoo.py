from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pytest

@pytest.fixture
def login_odoo():
    driver = webdriver.Edge()
    driver.get("http://localhost:8070")
    wait = WebDriverWait(driver, 10)
    #assert "Odoo" in driver.title
    email = wait.until(EC.element_to_be_clickable((By.ID, "login")))
    email.send_keys("criz-Odoo_dev@gmail.com")
    password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password.send_keys("admin")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    yield driver
    driver.quit()

def test_basic_odoo(login_odoo):
    driver = login_odoo
    
    assert "Odoo" in driver.title

def test_into_real_state_module(login_odoo):
    driver = login_odoo
    wait = WebDriverWait(driver, 10)
    real_state = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu-xmlid='state.estate_menu_root']")))
    real_state.click()
    while True: pass
    assert "Real Estate" in driver.title
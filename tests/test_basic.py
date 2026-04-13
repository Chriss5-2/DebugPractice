from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture # Permite que la función "driver" pueda ser reutiliazada en otros test, evitando la repetición de código
def driver():
    driver = webdriver.Edge()
    yield driver # Da la propiedad de poner ejecutar un paso central antes de cerrarlo, es como un permiso para ejecutar un código antes del cierre
    driver.quit()
    # Linea 5: Crea una instancia del navegador Edge
    # Linea 6: Da un stop a la funcion "driver" para que ejecute algo antes de cerrarlo
    # Linea 7: Cierra la sesión del navegador, es decir, cierra el navegador

def test_visit_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title 

def test_visit_youtube(driver):
    driver.get("https://www.youtube.com")
    assert "YouTube" in driver.title


def test_visit_sandbox_and_explore_elements(driver):
    driver.get("https://testertestarudo.com/en/sandbox")
    driver.find_element(By.XPATH, "//input[@id='sb-name']")
    driver.find_element(By.CSS_SELECTOR, "input#sb-email")
    driver.find_element(By.ID, "sb-email")
    driver.find_element(By.CLASS_NAME, "Sandbox-module__X_UfkW__btnRow")
    driver.find_element(By.LINK_TEXT, "GitHub")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Terms of Serv")
    assert "Tester Testarudo | Testing Solutions for Companies – Professional QA Training" in driver.title
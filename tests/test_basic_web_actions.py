from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options

import pytest

@pytest.fixture # Permite que la función "driver" pueda ser reutiliazada en otros test, evitando la repetición de código
def driver():
    edge_options = Options() # Creamos una instancia de opciones para Edge
    # edge_options.add_argument("--headless") # El argumento --headless corre el navegador en segundo plano, sin mostrar la interfaz gráfica
    # edge_options.add_argument("--start-maximized") # El argumento --start-maximized inicia el navegador maximizado
    # edge_options.add_argument("--windows-size=920,1080") # Establece el tamaño de la ventana del navegador a 1920x1080 píxeles
    edge_options.add_argument("--incognito") # Abre el navegador en modo incógnito
    driver = webdriver.Edge(options=edge_options )
    driver.get("https://testertestarudo.com/en/sandbox")
    yield driver
    assert "Tester Testarudo | Testing Solutions for Companies – Professional QA Training" in driver.title
    driver.quit()

@pytest.fixture
def on_botones_section(driver):
    section_button = driver.find_element(By.XPATH, "//span[text()='Botones']")
    section_button.click()
    assert "Tester Testarudo | Testing Solutions for Companies – Professional QA Training" in driver.title
    return section_button

def test_basic_web_actions(driver):
    # driver.back() # Regresa a la página anterior
    # driver.forward() # Avanza a la página siguiente
    # driver.refresh() # Refresca la página actual
    # driver.close() # Cierra la pestaña actual
    # driver.quit() # Cierra el navegador completo
    # driver.add_cookie({})
    driver.refresh()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.back()
    assert "Tester Testarudo | Testing Solutions for Companies – Professional QA Training" in driver.title
    driver.forward()
    assert "Google" in driver.title
    driver.back()
    

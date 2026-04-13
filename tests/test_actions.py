from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# importar wait de selenium
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture # Permite que la función "driver" pueda ser reutiliazada en otros test, evitando la repetición de código
def driver():
    driver = webdriver.Edge()
    driver.get("https://testertestarudo.com/en/sandbox")
    yield driver # Da la propiedad de poner ejecutar un paso central antes de cerrarlo, es como un permiso para ejecutar un código antes del cierre
    driver.quit()
    # Linea 5: Crea una instancia del navegador Edge
    # Linea 6: Da un stop a la funcion "driver" para que ejecute algo antes de cerrarlo
    # Linea 7: Cierra la sesión del navegador, es decir, cierra el navegador

@pytest.fixture
def on_botones_section(driver):
    section_button = driver.find_element(By.XPATH, "//span[text()='Botones']")
    section_button.click()
    return section_button


def test_click_element(driver):
    driver.find_element(By.CSS_SELECTOR, "[data-testid='btn-reset']")
    driver.find_element(By.CLASS_NAME, "Sandbox-module__X_UfkW__btnRow")
    driver.find_element(By.LINK_TEXT, "GitHub")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Terms of Serv")
    assert "Tester Testarudo | Testing Solutions for Companies – Professional QA Training" in driver.title

def test_on_botones_section(on_botones_section,driver):
    section_button = on_botones_section
    driver.implicitly_wait(2000)
    assert section_button.is_displayed()
    assert section_button.is_enabled()

def test_click_danger_button(on_botones_section, driver):
    danger_button = driver.find_element(By.XPATH, "//button[text()='Danger']")
    danger_button.click()

    log_output = driver.find_element(By.CSS_SELECTOR, "[data-testid='click-log']")
    assert "Click: btn-danger" in log_output.text

def test_fill_form_success(driver):
    # name es un input donde se espera un texto con formato de nombre
    name_input=driver.find_element(By.XPATH, "//input[@id='sb-name']")
    name_input.send_keys("Chriz")
    # email es un input donde se espera un texto con formato de email
    email_input=driver.find_element(By.XPATH, "//input[@id='sb-email']")
    email_input.send_keys("chriz@example.com")
    # Para selección de rol tenemos el siguiente html
    # <select id="sb-role" data-testid="select-role" class="Sandbox-module__X_UfkW__select ">
    #   <option value="">— Selecciona un rol —</option>
    #   <option value="junior">QA Junior</option>
    #   <option value="semi">QA Semi-Senior</option>
    #   <option value="senior">QA Senior</option><option value="lead">QA Lead</option><option value="automation">Automation Engineer</option></select>
    # Importamos Select (Linea 4)
    # Rol en QA es un select donde se espera elegir una de las opciones disponibles
    rol_input=driver.find_element(By.ID, 'sb-role')
    select = Select(rol_input)
    select.select_by_visible_text("QA Junior")
    # Equivalentes
    # select.select_by_value("junior")
    # select.select_by_index(1)
    # Mensaje es un cuadro de texto donde se espera un texto libre
    message_input=driver.find_element(By.CLASS_NAME, "Sandbox-module__X_UfkW__textarea")
    message_input.send_keys("Hola, este es mi primera prueba de Selenium con Python y con complejidad media, espero funcioneeee")
    # La selección de notificaciones es de la forma
    # <div class="Sandbox-module__X_UfkW__formRow">
    #   <label style="margin-bottom: 8px;">Notificaciones</label>
    #       <div class="Sandbox-module__X_UfkW__checkGroup">
    #           <label class="Sandbox-module__X_UfkW__checkRow">
    #               <input data-testid="radio-email" type="radio" value="email" checked="" name="notif">Por email</label>
    #           <label class="Sandbox-module__X_UfkW__checkRow">
    #               <input data-testid="radio-sms" type="radio" value="sms" name="notif">Por SMS</label>
    #           <label class="Sandbox-module__X_UfkW__checkRow">
    #               <input data-testid="radio-none" type="radio" value="none" name="notif">Sin notificaciones</label>
    #       </div>
    # </div>
    # La variable notify será usada para elegir el método de notificación, usaremos el atributi data-testid, notify puede ser:
    # radio-email
    # radio-sms
    # radio-none
    notify='radio-sms'
    # Luego buscamos el botón que tenga el mismo atributo en data-testid que será usado para hacer click y elegir el método de notificación
    notify_input=driver.find_element(By.CSS_SELECTOR, f"[data-testid='{notify}']")
    notify_input.click()
    # Para el botón de aceptar Terminos y condiciones, su html es así
    # <div class="Sandbox-module__X_UfkW__formRow">
    #   <label class="Sandbox-module__X_UfkW__checkRow" data-testid="label-agree">
    #       <input data-testid="checkbox-agree" type="checkbox">Acepto los términos y condiciones *</label>
    # </div>
    # Buscamos el botón por su data-testid que es checkbox-agree
    checkbox_input=driver.find_element(By.CSS_SELECTOR, "input[data-testid='checkbox-agree']")
    checkbox_input.click()
    # Buscamos el botón de enviar que es un button de tipo submit
    # Su html es
    # <div class="Sandbox-module__X_UfkW__btnRow">
    #   <button type="submit" data-testid="btn-submit" class="Sandbox-module__X_UfkW__btn Sandbox-module__X_UfkW__btnPrimary">Enviar formulario</button>
    #   <button type="reset" data-testid="btn-reset" class="Sandbox-module__X_UfkW__btn Sandbox-module__X_UfkW__btnSecondary">Limpiar</button>
    # </div>
    # Usamos la opción de Enviar formulario
    # Aceptar Cookies
    try:
        cookie_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".CookieBanner-module__6xFwxG__btnPrimary")
        ))
        cookie_btn.click()
    except:
        pass

    # Esperamos a que el botón de enviar sea clickeable o mejor dicho que envie el formulario tomando los parametros ingresados
    submit_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()
    #success_message=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='form-result']")))
    # Esperamos a que nos de el resultado de clickear submit
    success_message=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='form-result']")))
    # success_message=driver.find_element(By.XPATH, "//div[@data-testid='form-result']")
    # Esperamos un tiempo para poder ver bien los campos y no se cierre el navegador tan rapido
    assert "✓ Enviado:" in success_message.text

def test_fill_form_empty(driver):

    try:
        cookie_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".CookieBanner-module__6xFwxG__btnPrimary")
        ))
        cookie_btn.click()
    except:
        pass
    # submit
    submit_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()
    # mensajes de error
    wait = WebDriverWait(driver, 10)
    name_empty_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'El nombre es obligatorio')]")))
    email_empty_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Email inválido')]")))
    rol_empty_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Selecciona un rol')]")))
    agree_empty_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Debes aceptar los términos')]")))

    assert "El nombre es obligatorio" in name_empty_message.text
    assert "Email inválido" in email_empty_message.text
    assert "Selecciona un rol" in rol_empty_message.text
    assert "Debes aceptar los términos" in agree_empty_message.text
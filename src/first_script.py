from selenium import webdriver
from selenium.webdriver.common.by import By

# Start the session
driver = webdriver.Chrome()
# Permite abrir y cerrar el navegador en una sola sesión
# Para salir de la sesión: driver.quit()

# Navigate to a webpage
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# Abre la página web especificada

# Ger browser information
title = driver.title # Obtiene el título de la página web
url = driver.current_url # Obtiene la URL actual de la página web
print(f"Title: {title}")
print(f"URL: {url}")

# Waiting Strategies
# Implicit wait
# Sirve para esperar un tiempo determinado antes de lanzar una excepción si no se encuentra un elemento

# Explicit wait
# Sirve para esperar un tiempo determinado hasta que se cumpla una condición específica, como la presencia de un elemento o la visibilidad de un elemento

# La diferencia entre ambos es que el implicit wait se aplica a todas las búsquedas de elementos, mientras que el explicit 
# wait se aplica a una búsqueda específica. El implicit wait es más general, mientras que el explicit wait es más específico y flexible.

# Aplicación de Implicit wait
# driver.implicitly_wait(2) # Espera hasta 2 segundos para encontrar un elemento antes de lanzar una excepción
# Aplicación de Explicit wait
# wait = WebDriverWait(driver, 10) # Espera hasta 10 segundos para que se cumpla una condición específica
# wait.until(lambda _ : revealed.is_displayed()) # Espera hasta que el elemento "revealed" sea visible

driver.implicitly_wait(0.5) # Espera hasta 0.5 segundos para encontrar un elemento antes de lanzar una excepción
print("Espera implícita aplicada: 0.5 segundos")

# Find an element
# Ejemplo de aplicacióón de búsqueda de elementos
# <ol id="list_1">
#   <li class="item_1.1">....
#   <li class="item_1.2">....
#   <li class="item_1.3"><span>This is item 1.3</span>...
# </ol>
# <ul id="list_2">
#   <li class="item_2.1">....
#   <li class="item_2.2">....
#   <li class="item_2.3"><span>This is item 2.3</span>...
# </ul>

# BUSCAR POR TODO EL DOCUMENTO
# find_item = driver.find_element(By.CLASS_NAME, "item_1.3") # Encuentra el primer elemento con la clase "item_1.3"

# BUSCAR POR UN SUBCONJUNTO DEL DOCUMENTO
# find_list_1 = driver.find_element(By.ID, "list_1") # Recopila todos los elementos con el id "list_1"
# find_item = find_list_1.find_element(By.CLASS_NAME, "item_1.3") # Encuentra el primer elemento con la clase "item_1.3" dentro del elemento "list_1"

# EVALUAR POR UNA SOMBRA DEL DOCUMENTO
# Esto sirve para evaluar elementos que están dentro de un shadow DOM, que es una parte del DOM que está aislada del resto del 
# documento y no se puede acceder directamente desde el documento principal.
# Requiere Selenium 4.0 o superior
# shadow_host = driver.find_element(By.CSS_SELECTOR, "#shadow_host") # Encuentra el elemento que es el host del shadow DOM
# shadow_root = shadow_host.shadow_root # Obtiene el shadow root del host
# shadow_content = shadow_root.find_element(By.CSS_SELECTOR, "#shadow_content") # Encuentra el elemento dentro del shadow DOM

# Localizados optimizado
# Mejora el rendimiento de las pruebas además de que hace el código más legible, permite buscar elementos en un solo comando
# Podemos usar CSS o XPath
# item = driver.find_element(By.CSS_SELECTOR, "#list_1 .item_1.3") # Encuentra el elemento con el selector CSS "#list_1 .item_1.3"

# Referencias todos los elementos
# Permite referencias todos los elementos que cumplen con un criterio especifico, a diferencia del primero, este devuelve todos los elementos que 
# cumplen en lugar de solo el primero, devuelve una lista de elementos
# items = driver.find_elements(By.TAG_NAME, "li") # Encuentra todos los elementos con la etiqueta "li"

text_box = driver.find_element(by=By.NAME, value="my-text") # Encuentra el elemento con el atributo name="my-text"
print("Text box encontrado: " + text_box.get_attribute("name")) # Imprime el valor del atributo "name" del elemento "text_box"
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button") # Encuentra el elemento con el selector CSS "button"
print("Submit button encontrado: " + submit_button.tag_name) # Imprime el tag name del elemento "submit_button"


# Interact with the element

# Click an element
# El click se ejecuta en el centro del elemento, si este está oculto por alguna razón, nos retornará un error
# driver.get("https://www.selenium.dev/selenium/web/inputs.html")
# check_input = driver.find_element(By.NAME, "checkbox_input") # Encuentra el elemento con el atributo name="checkbox_input"
# check_input.click() # Hace click en el elemento "check_input"

# Send keys
# Permite enviar texto a un elemento con atributo de "text" o como "content-editable", si el elemento no es editable, retornará error
# email_input = driver.find_element(By.NAME, "email_input") # Encuentra el elemento con el atributo name="email_input"
# email_input.clear() # Limpia el contenido del elemento "email_input"
# email = "example@example.com"
# email_input.send_keys(email) # Envía el texto "example@example.com" al elemento "email_input"
# El comando clear() resetea el contenido del elemento, requiere que el elemento sea editable y resetable sino retornará error

text_box.send_keys("Selenium") # Envía el texto "Selenium" al elemento "text_box"
print("Texto enviado al text box: " + text_box.get_attribute("value")) # Imprime el valor del atributo "value" del elemento "text_box"
submit_button.click() # Hace click en el elemento "submit_button"
print("Submit button clickeado")


# Información sobre elementos web

# Verificación de visibilidad
# Retorna un boolean, "true" en caso el elemento sea visible en la web, en caso contrario "false"
# driver.get("https://www.selenium.dev/selenium/web/inputs.html")
# is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()

# Verificación de habilitación
# Retorna un boolean, "true" en caso el elemento esté habilitado para interactuar, en caso contrario "false"
# is_enabled_button = driver.find_element(By.NAME, "button_input").is_enabled()

# Verificación de selección
# Retorna un boolean, "true" en caso el elemento esté seleccionado, en caso contrario "false"
# is_selected_check = driver.find_element(By.NAME, "checkbox_input").is_selected()

# Obtener el tag name de un objeto referenciado
# tag_name_inp = driver.find_element(By.NAME, "email_input").tag_name # Retorna el tag name del elemento "email_input"

# Obtener tamaño y posición de un elemento referenciado
# La data contiene
# X-axis position
# Y-axis position
# Height
# Width
# rect = driver.find_element(By.NAME, "range_input").rect # Retorna un diccionario con la información de tamaño y posición del elemento "range_input"

# Obtener valor CSS de un elemento referenciado
# css_value = driver.find_element(By.NAME, "color_input").value_of_css_property("font-size") 
# # Retorna el valor de la propiedad CSS "font-size" del elemento "color_input"

# Obtener texto de un elemento referenciado
# text = driver.find_element(By.TAG_NAME, "h1").text # Retorna el texto del elemento con la etiqueta "h1"

# Obtener atributos y propiedades de un elemento referenciado
# email_txt = driver.find_element(By.NAME, "email_input")
# value_info = email_txt.get_attribute("value") # Retorna el valor del atributo "value" del elemento "email_input"
# type_info = email_txt.get_property("type") # Retorna el valor de la propiedad

message = driver.find_element(By.ID, value="message") # Encuentra el elemento con el id "message"
text = message.text # Retorna el texto del elemento "message"
print(f"Message: {text}")

# Cerrar la sesión
driver.quit() # Cierra el navegador y termina la sesión
print("Sesión cerrada")
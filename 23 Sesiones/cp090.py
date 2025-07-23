from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ingresar a la página de sesiones
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions")

try:
    wait = WebDriverWait(driver, 10)

    # Esperar a que aparezca alguna tabla de sesiones
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))

    # Buscar todos los botones "Submit"
    submit_buttons = driver.find_elements(By.XPATH, "//button[normalize-space(text())='Submit']")

    encontrado = False
    for button in submit_buttons:
        # Revisar si está deshabilitado
        if button.get_attribute("disabled") is not None:
            print("✅ El botón 'Submit' está deshabilitado.")
            encontrado = True
            break

    if not encontrado:
        print("⚠️ El botón 'Submit' está habilitado o no se encontró.")

except Exception as e:
    print(f"❌ Error al buscar el botón Submit: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()

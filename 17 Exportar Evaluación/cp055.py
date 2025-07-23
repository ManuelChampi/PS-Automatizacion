from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar Chrome con perfil
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')
driver = webdriver.Chrome(options=options)

# URL a la página de sesiones
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions")

try:
    # Esperar a que la tabla cargue
    tabla = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )

    print("✅ Tabla cargada.")

    # Buscar todas las filas de la tabla
    filas = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

    # Buscar la fila con 'feedback IS'
    for fila in filas:
        if 'feedback IS' in fila.text:
            print("✅ Sesión 'feedback IS' encontrada.")

            # Hacer clic en el botón de menú (dropdown-toggle)
            boton_menu = fila.find_element(By.CSS_SELECTOR, "button.dropdown-toggle")
            boton_menu.click()

            # Esperar a que aparezca el botón 'Download Results' en el menú desplegado
            boton_descarga = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-download-1"))
            )
            boton_descarga.click()
            print("✅ 'Download Results' clickeado.")
            break
    else:
        print("❌ No se encontró la sesión 'feedback IS'.")

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()

# driver.quit()  # opcionalmente cerrar el navegador

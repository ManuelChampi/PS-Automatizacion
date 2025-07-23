from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al formulario de edición
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/edit?courseid=IS-2025Semestre_1&fsname=example")

try:
    # Esperar a que cargue el campo del nombre de la sesión
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "session-name"))
    )
    print("✅ Página de edición de sesión cargada correctamente.")

except Exception as e:
    print(f"❌ Error al cargar la página de edición: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()

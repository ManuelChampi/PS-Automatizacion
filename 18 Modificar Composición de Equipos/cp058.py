from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ir directamente al link del reporte
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/report?courseid=IS-2025Semestre_1&fsname=Curso_new")

try:
    # Esperar a que el botón "Expand All" esté presente
    expand_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "btn-expand-all"))
    )
    expand_btn.click()
    print("✅ Botón 'Expand All' clickeado.")

    # Verificar si alguna respuesta muestra el texto "Anonymous"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Anonymous')]"))
    )
    print("✅ Las respuestas están marcadas como 'Anonymous'.")

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()

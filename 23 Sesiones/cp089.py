from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome con perfil del instructor
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_instructor')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

# Ingresar a la vista de resultados (preview as student)
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/instructor/sessions/submission?courseid=IS-2025Semestre_1&fsname=Sesi%C3%B3n%20de%20Feedback&editingMode=true")

try:
    wait = WebDriverWait(driver, 10)

    # Esperar y capturar el div con id="closing-time"
    closing_time_element = wait.until(EC.presence_of_element_located(
        (By.ID, "closing-time")
    ))

    print("✅ Closing time:")
    print(closing_time_element.text.strip())

except Exception as e:
    print(f"❌ Error al buscar el campo Closing time: {e}")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()

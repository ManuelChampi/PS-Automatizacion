from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta al Chrome for Testing del estudiante
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\sailax\chrome_student')  # ruta de tu perfil
driver = webdriver.Chrome(options=options)

options.add_argument("--start-maximized")

# Ir al home del estudiante
driver.get("https://teammates-escarabajo-462900.uc.r.appspot.com/web/student/home")

# Esperar que el botón esté presente y visible (hasta 30s)
try:
    # Esperar explícitamente hasta que el botón esté visible
    wait = WebDriverWait(driver, 30)

    # Espera a que esté presente el botón dentro del DOM
    button = wait.until(EC.element_to_be_clickable((By.ID, "view-responses-btn-1")))

    # Clic en el botón
    button.click()

    print("✅ Clic exitoso en 'View Responses'")

except Exception as e:
    print(f"❌ Error al hacer clic en el botón: {e}")


input("Presiona ENTER para cerrar el navegador...")
driver.quit()
